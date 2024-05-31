
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import six
import os
import matplotlib
import matplotlib.transforms as transforms
from matplotlib._pylab_helpers import Gcf
from matplotlib.backend_bases import RendererBase, GraphicsContextBase,\
    FigureManagerBase, FigureCanvasBase, NavigationToolbar2, TimerBase
from matplotlib.figure import Figure
from matplotlib.transforms import Bbox, Affine2D
from matplotlib.backend_bases import ShowBase, Event
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.mathtext import MathTextParser
from matplotlib import rcParams
from hashlib import md5
from matplotlib import _path

try:
    import kivy
except ImportError:
    raise ImportError("this backend requires Kivy to be installed.")

from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.actionbar import ActionBar, ActionView, \
                                ActionButton, ActionToggleButton, \
                                ActionPrevious, ActionOverflow, ActionSeparator
from kivy.base import EventLoop
from kivy.core.text import Label as CoreLabel
from kivy.core.image import Image
from kivy.graphics import Color, Line
from kivy.graphics import Rotate, Translate
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics.tesselator import Tesselator
from kivy.graphics.context_instructions import PopMatrix, PushMatrix
from kivy.graphics import StencilPush, StencilPop, StencilUse,\
                                StencilUnUse
from kivy.logger import Logger
from kivy.graphics import Mesh
from kivy.resources import resource_find
from kivy.uix.stencilview import StencilView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.clock import Clock
from distutils.version import LooseVersion
_mpl_ge_1_5 = LooseVersion(matplotlib.__version__) >= LooseVersion('1.5.0')
_mpl_ge_2_0 = LooseVersion(matplotlib.__version__) >= LooseVersion('2.0.0')


import numpy as np
import io
import textwrap
import uuid
import numbers
from functools import partial
from math import cos, sin, pi

kivy.require('1.9.1')

toolbar = None
my_canvas = None


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class MPLKivyApp(App):

    figure = ObjectProperty(None)
    toolbar = ObjectProperty(None)

    def build(self):
        EventLoop.ensure_window()
        layout = FloatLayout()
        if self.figure:
            self.figure.size_hint_y = 0.9
            layout.add_widget(self.figure)
        if self.toolbar:
            self.toolbar.size_hint_y = 0.1
            layout.add_widget(self.toolbar)
        return layout


def draw_if_interactive():

    if matplotlib.is_interactive():
        figManager = Gcf.get_active()
        if figManager:
            figManager.canvas.draw_idle()


class Show(ShowBase):

    def mainloop(self):
        app = App.get_running_app()
        if app is None:
            app = MPLKivyApp(figure=my_canvas, toolbar=toolbar)
            app.run()

show = Show()


def new_figure_manager(num, *args, **kwargs):
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, thisFig)


def new_figure_manager_given_figure(num, figure):
 
    canvas = FigureCanvasKivy(figure)
    manager = FigureManagerKivy(canvas, num)
    global my_canvas
    global toolbar
    toolbar = manager.toolbar.actionbar if manager.toolbar else None
    my_canvas = canvas
    return manager


class RendererKivy(RendererBase):

    def __init__(self, widget):
        super(RendererKivy, self).__init__()
        self.widget = widget
        self.dpi = widget.figure.dpi
        self._markers = {}
        #  Can be enhanced by using TextToPath matplotlib, textpath.py
        self.mathtext_parser = MathTextParser("path")
        self.list_goraud_triangles = []
        self.clip_rectangles = []
        self.labels_inside_plot = []

    def contains(self, widget, x, y):
    
        left = widget.x
        bottom = widget.y
        top = widget.y + widget.height
        right = widget.x + widget.width
        return (left <= x <= right and
                bottom <= y <= top)

    def handle_clip_rectangle(self, gc, x, y):

        x = self.widget.x + x
        y = self.widget.y + y
        collides = self.collides_with_existent_stencil(x, y)
        if collides > -1:
            return collides
        new_bounds = gc.get_clip_rectangle()
        if new_bounds:
            x = self.widget.x + int(new_bounds.bounds[0])
            y = self.widget.y + int(new_bounds.bounds[1])
            w = int(new_bounds.bounds[2])
            h = int(new_bounds.bounds[3])
            collides = self.collides_with_existent_stencil(x, y)
            if collides == -1:
                cliparea = StencilView(pos=(x, y), size=(w, h))
                self.clip_rectangles.append(cliparea)
                self.widget.add_widget(cliparea)
                return len(self.clip_rectangles) - 1
            else:
                return collides
        else:
            return -2

    def draw_path_collection(self, gc, master_transform, paths, all_transforms,
        offsets, offsetTrans, facecolors, edgecolors,
        linewidths, linestyles, antialiaseds, urls,
        offset_position):

        len_path = len(paths[0].vertices) if len(paths) > 0 else 0
        uses_per_path = self._iter_collection_uses_per_path(
            paths, all_transforms, offsets, facecolors, edgecolors)
      
        should_do_optimization = \
            len_path + uses_per_path + 5 < len_path * uses_per_path
        if not should_do_optimization:
            return RendererBase.draw_path_collection(
                self, gc, master_transform, paths, all_transforms,
                offsets, offsetTrans, facecolors, edgecolors,
                linewidths, linestyles, antialiaseds, urls,
                offset_position)
        # Generate an array of unique paths with the respective transformations
        path_codes = []
        for i, (path, transform) in enumerate(self._iter_collection_raw_paths(
            master_transform, paths, all_transforms)):
            transform = Affine2D(transform.get_matrix()).scale(1.0, -1.0)
            if _mpl_ge_2_0:
                polygons = path.to_polygons(transform, closed_only=False)
            else:
                polygons = path.to_polygons(transform)
            path_codes.append(polygons)
   
        for xo, yo, path_poly, gc0, rgbFace in self._iter_collection(
            gc, master_transform, all_transforms, path_codes, offsets,
            offsetTrans, facecolors, edgecolors, linewidths, linestyles,
            antialiaseds, urls, offset_position):
            list_canvas_instruction = self.get_path_instructions(gc0, path_poly,
                                    closed=True, rgbFace=rgbFace)
            for widget, instructions in list_canvas_instruction:
                widget.canvas.add(PushMatrix())
                widget.canvas.add(Translate(xo, yo))
                widget.canvas.add(instructions)
                widget.canvas.add(PopMatrix())

    def collides_with_existent_stencil(self, x, y):
       
        idx = -1
        for cliparea in self.clip_rectangles:
            idx += 1
            if self.contains(cliparea, x, y):
                return idx
        return -1

    def get_path_instructions(self, gc, polygons, closed=False, rgbFace=None):
    
        instructions_list = []
        points_line = []
        for polygon in polygons:
            for x, y in polygon:
                x = x + self.widget.x
                y = y + self.widget.y
                points_line += [float(x), float(y), ]
            tess = Tesselator()
            tess.add_contour(points_line)
            if not tess.tesselate():
                Logger.warning("Tesselator didn't work :(")
                return
            newclip = self.handle_clip_rectangle(gc, x, y)
            if newclip > -1:
                instructions_list.append((self.clip_rectangles[newclip],
                        self.get_graphics(gc, tess, points_line, rgbFace,
                                          closed=closed)))
            else:
                instructions_list.append((self.widget,
                        self.get_graphics(gc, tess, points_line, rgbFace,
                                          closed=closed)))
        return instructions_list

    def get_graphics(self, gc, polygons, points_line, rgbFace, closed=False):
   
        instruction_group = InstructionGroup()
        if isinstance(gc.line['dash_list'], tuple):
            gc.line['dash_list'] = list(gc.line['dash_list'])
        if rgbFace is not None:
            if len(polygons.meshes) != 0:
                instruction_group.add(Color(*rgbFace))
                for vertices, indices in polygons.meshes:
                    instruction_group.add(Mesh(
                        vertices=vertices,
                        indices=indices,
                        mode=str("triangle_fan")
                    ))
        instruction_group.add(Color(*gc.get_rgb()))
        if _mpl_ge_1_5 and (not _mpl_ge_2_0) and closed:
            points_poly_line = points_line[:-2]
        else:
            points_poly_line = points_line
        if gc.line['width'] > 0:
            instruction_group.add(Line(points=points_poly_line,
                width=int(gc.line['width'] / 2),
                dash_length=gc.line['dash_length'],
                dash_offset=gc.line['dash_offset'],
                dash_joint=gc.line['join_style'],
                dash_list=gc.line['dash_list']))
        return instruction_group

    def draw_image(self, gc, x, y, im):
      
        # Clip path to define an area to mask.
        clippath, clippath_trans = gc.get_clip_path()
        # Normal coordinates calculated and image added.
        x = self.widget.x + x
        y = self.widget.y + y
        bbox = gc.get_clip_rectangle()
        if bbox is not None:
            l, b, w, h = bbox.bounds
        else:
            l = 0
            b = 0
            w = self.widget.width
            h = self.widget.height
        h, w = im.get_size_out()
        rows, cols, image_str = im.as_rgba_str()
        texture = Texture.create(size=(w, h))
        texture.blit_buffer(image_str, colorfmt='rgba', bufferfmt='ubyte')
        if clippath is None:
            with self.widget.canvas:
                Color(1.0, 1.0, 1.0, 1.0)
                Rectangle(texture=texture, pos=(x, y), size=(w, h))
        else:
            if _mpl_ge_2_0:
                polygons = clippath.to_polygons(clippath_trans, closed_only=False)
            else:
                polygons = clippath.to_polygons(clippath_trans)
            list_canvas_instruction = self.get_path_instructions(gc, polygons,
                                                rgbFace=(1.0, 1.0, 1.0, 1.0))
            for widget, instructions in list_canvas_instruction:
                widget.canvas.add(StencilPush())
                widget.canvas.add(instructions)
                widget.canvas.add(StencilUse())
                widget.canvas.add(Color(1.0, 1.0, 1.0, 1.0))
                widget.canvas.add(Rectangle(texture=texture,
                                            pos=(x, y), size=(w, h)))
                widget.canvas.add(StencilUnUse())
                widget.canvas.add(StencilPop())

    def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):

        if mtext:
            transform = mtext.get_transform()
            ax, ay = transform.transform_point(mtext.get_position())

            angle_rad = mtext.get_rotation() * np.pi / 180.
            dir_vert = np.array([np.sin(angle_rad), np.cos(angle_rad)])

            if mtext.get_rotation_mode() == "anchor":
                # if anchor mode, rotation is undone first
                v_offset = np.dot(dir_vert, [(x - ax), (y - ay)])
                ax = ax + v_offset * dir_vert[0]
                ay = ay + v_offset * dir_vert[1]

            w, h, d = self.get_text_width_height_descent(s, prop, ismath)
            ha, va = mtext.get_ha(), mtext.get_va()
            if ha == "center":
                ax -= w / 2
            elif ha == "right":
                ax -= w
            if va == "top":
                ay -= h
            elif va == "center":
                ay -= h / 2

            if mtext.get_rotation_mode() != "anchor":
                # if not anchor mode, rotation is undone last
                v_offset = np.dot(dir_vert, [(x - ax), (y - ay)])
                ax = ax + v_offset * dir_vert[0]
                ay = ay + v_offset * dir_vert[1]

            x, y = ax, ay

        x += self.widget.x
        y += self.widget.y

        if ismath:
            self.draw_mathtext(gc, x, y, s, prop, angle)
        else:
            font = resource_find(prop.get_name() + ".ttf")
            color = gc.get_rgb()
            if font is None:
                plot_text = CoreLabel(font_size=prop.get_size_in_points(), color=color)
            else:
                plot_text = CoreLabel(font_size=prop.get_size_in_points(),
                                font_name=prop.get_name(), color=color)
            plot_text.text = six.text_type("{}".format(s))
            if prop.get_style() == 'italic':
                plot_text.italic = True
            if self.weight_as_number(prop.get_weight()) > 500:
                plot_text.bold = True
            plot_text.refresh()
            with self.widget.canvas:
                if isinstance(angle, float):
                    PushMatrix()
                    Rotate(angle=angle, origin=(int(x), int(y)))
                    Rectangle(pos=(int(x), int(y)), texture=plot_text.texture,
                              size=plot_text.texture.size)
                    PopMatrix()
                else:
                    Rectangle(pos=(int(x), int(y)), texture=plot_text.texture,
                              size=plot_text.texture.size)

    def draw_mathtext(self, gc, x, y, s, prop, angle):

        ftimage, depth = self.mathtext_parser.parse(s, self.dpi, prop)
        w = ftimage.get_width()
        h = ftimage.get_height()
        texture = Texture.create(size=(w, h))
        if _mpl_ge_1_5:
            texture.blit_buffer(ftimage.as_rgba_str()[0][0], colorfmt='rgba',
                                bufferfmt='ubyte')
        else:
            texture.blit_buffer(ftimage.as_rgba_str(), colorfmt='rgba',
                                bufferfmt='ubyte')
        texture.flip_vertical()
        with self.widget.canvas:
            Rectangle(texture=texture, pos=(x, y), size=(w, h))

    def draw_path(self, gc, path, transform, rgbFace=None):
  
        if _mpl_ge_2_0:
            polygons = path.to_polygons(transform, self.widget.width,
                                        self.widget.height, closed_only=False)
        else:
            polygons = path.to_polygons(transform, self.widget.width,
                                        self.widget.height)
        list_canvas_instruction = self.get_path_instructions(gc, polygons,
                                    closed=True, rgbFace=rgbFace)
        for widget, instructions in list_canvas_instruction:
            widget.canvas.add(instructions)

    def draw_markers(self, gc, marker_path, marker_trans, path,
        trans, rgbFace=None):
 
        if not len(path.vertices):
            return
        # get a string representation of the path
        path_data = self._convert_path(
            marker_path,
            marker_trans + Affine2D().scale(1.0, -1.0),
            simplify=False)
        # get a string representation of the graphics context and rgbFace.
        style = str(gc._get_style_dict(rgbFace))
        dictkey = (path_data, str(style))
        # check whether this marker has been created before.
        list_instructions = self._markers.get(dictkey)
        # creating a list of instructions for the specific marker.
        if list_instructions is None:
            if _mpl_ge_2_0:
                polygons = marker_path.to_polygons(marker_trans, closed_only=False)
            else:
                polygons = marker_path.to_polygons(marker_trans)
            self._markers[dictkey] = self.get_path_instructions(gc,
                                        polygons, rgbFace=rgbFace)
        # Traversing all the positions where a marker should be rendered
        for vertices, codes in path.iter_segments(trans, simplify=False):
            if len(vertices):
                x, y = vertices[-2:]
                for widget, instructions in self._markers[dictkey]:
                    widget.canvas.add(PushMatrix())
                    widget.canvas.add(Translate(x, y))
                    widget.canvas.add(instructions)
                    widget.canvas.add(PopMatrix())

    def flipy(self):
        return False

    def _convert_path(self, path, transform=None, clip=None, simplify=None,
                      sketch=None):
        if clip:
            clip = (0.0, 0.0, self.width, self.height)
        else:
            clip = None
        if _mpl_ge_1_5:
            return _path.convert_to_string(
                path, transform, clip, simplify, sketch, 6,
                [b'M', b'L', b'Q', b'C', b'z'], False).decode('ascii')
        else:
            return _path.convert_to_svg(path, transform, clip, simplify, 6)

    def get_canvas_width_height(self):

        return self.widget.width, self.widget.height

    def get_text_width_height_descent(self, s, prop, ismath):
 
        if ismath:
            ftimage, depth = self.mathtext_parser.parse(s, self.dpi, prop)
            w = ftimage.get_width()
            h = ftimage.get_height()
            return w, h, depth
        font = resource_find(prop.get_name() + ".ttf")
        if font is None:
            plot_text = CoreLabel(font_size=prop.get_size_in_points())
        else:
            plot_text = CoreLabel(font_size=prop.get_size_in_points(),
                            font_name=prop.get_name())
        plot_text.text = six.text_type("{}".format(s))
        plot_text.refresh()
        return plot_text.texture.size[0], plot_text.texture.size[1], 1

    def new_gc(self):
        return GraphicsContextKivy(self.widget)

    def points_to_pixels(self, points):
        return points / 72.0 * self.dpi
		
    def weight_as_number(self, weight):
        # Return if number
        if isinstance(weight, numbers.Number):
            return weight
        # else use the mapping of matplotlib 2.2
        elif weight == 'ultralight':
            return 100
        elif weight == 'light':
            return 200
        elif weight == 'normal':
            return 400
        elif weight == 'regular':
            return 400
        elif weight == 'book':
            return 500
        elif weight == 'medium':
            return 500
        elif weight == 'roman':
            return 500
        elif weight == 'semibold':
            return 600
        elif weight == 'demibold':
            return 600
        elif weight == 'demi':
            return 600
        elif weight == 'bold':
            return 700
        elif weight == 'heavy':
            return 800
        elif weight == 'extra bold':
            return 800
        elif weight == 'black':
            return 900
        else:
            raise ValueError('weight ' + weight + ' not valid')


class NavigationToolbar2Kivy(NavigationToolbar2):
    def __init__(self, canvas, **kwargs):
        self.actionbar = ActionBar(pos_hint={'top': 1.0})
        super(NavigationToolbar2Kivy, self).__init__(canvas)
        self.rubberband_color = (1.0, 0.0, 0.0, 1.0)
        self.lastrect = None
        self.save_dialog = Builder.load_string(textwrap.dedent('''\
            <SaveDialog>:
                text_input: text_input
                BoxLayout:
                    size: root.size
                    pos: root.pos
                    orientation: "vertical"
                    FileChooserListView:
                        id: filechooser
                        on_selection: text_input.text = self.selection and\
                        self.selection[0] or ''

                    TextInput:
                        id: text_input
                        size_hint_y: None
                        height: 30
                        multiline: False

                    BoxLayout:
                        size_hint_y: None
                        height: 30
                        Button:
                            text: "Cancel"
                            on_release: root.cancel()

                        Button:
                            text: "Save"
                            on_release: root.save(filechooser.path,\
                            text_input.text)
            '''))

    def _init_toolbar(self):

        basedir = os.path.join(rcParams['datapath'], 'images')
        actionview = ActionView()
        actionprevious = ActionPrevious(title="Navigation", with_previous=False)
        actionoverflow = ActionOverflow()
        actionview.add_widget(actionprevious)
        actionview.add_widget(actionoverflow)
        actionview.use_separator = True
        self.actionbar.add_widget(actionview)
        id_group = uuid.uuid4()
        for text, tooltip_text, image_file, callback in self.toolitems:
            if text is None:
                actionview.add_widget(ActionSeparator())
                continue
            fname = os.path.join(basedir, image_file + '.png')
            if text in ['Pan', 'Zoom']:
                action_button = ActionToggleButton(text=text, icon=fname,
                                                   group=id_group)
            else:
                action_button = ActionButton(text=text, icon=fname)
            action_button.bind(on_press=getattr(self, callback))
            actionview.add_widget(action_button)

    def configure_subplots(self, *largs):
        pass

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path, filename):
        self.canvas.export_to_png(os.path.join(path, filename))
        self.dismiss_popup()

    def save_figure(self, *args):
        self.show_save()

    def draw_rubberband(self, event, x0, y0, x1, y1):
        w = abs(x1 - x0)
        h = abs(y1 - y0)
        rect = [int(val)for val in (min(x0, x1) + self.canvas.x, min(y0, y1)
                        + self.canvas.y, w, h)]
        if self.lastrect is None:
            self.canvas.canvas.add(Color(*self.rubberband_color))
        else:
            self.canvas.canvas.remove(self.lastrect)
        self.lastrect = InstructionGroup()
        self.lastrect.add(Line(rectangle=rect, width=1.0, dash_length=5.0,
                dash_offset=5.0))
        self.lastrect.add(Color(1.0, 0.0, 0.0, 0.2))
        self.lastrect.add(Rectangle(pos=(rect[0], rect[1]),
                                    size=(rect[2], rect[3])))
        self.canvas.canvas.add(self.lastrect)

    def release_zoom(self, event):
        self.lastrect = None
        return super(NavigationToolbar2Kivy, self).release_zoom(event)

def lista_igual(fdu):
    return len(set(fdu))<=1

class GraphicsContextKivy(GraphicsContextBase, object):
    _capd = {
        'butt': 'square',
        'projecting': 'square',
        'round': 'round',
    }
    line = {}

    def __init__(self, renderer):
        super(GraphicsContextKivy, self).__init__()
        self.renderer = renderer
        self.line['cap_style'] = self.get_capstyle()
        self.line['join_style'] = self.get_joinstyle()
        self.line['dash_offset'] = None
        self.line['dash_length'] = None
        self.line['dash_list'] = []

    def set_capstyle(self, cs):
        GraphicsContextBase.set_capstyle(self, cs)
        self.line['cap_style'] = self._capd[self._capstyle]

    def set_joinstyle(self, js):
        GraphicsContextBase.set_joinstyle(self, js)
        self.line['join_style'] = js

    def set_dashes(self, dash_offset, dash_list):
        GraphicsContextBase.set_dashes(self, dash_offset, dash_list)
        if dash_list is not None:
            self.line['dash_list'] = dash_list
        if dash_offset is not None:
            self.line['dash_offset'] = int(dash_offset)

    def set_linewidth(self, w):
        GraphicsContextBase.set_linewidth(self, w)
        self.line['width'] = w

    def _get_style_dict(self, rgbFace):
        attrib = {}
        forced_alpha = self.get_forced_alpha()
        if rgbFace is None:
            attrib['fill'] = 'none'
        else:
            if tuple(rgbFace[:3]) != (0, 0, 0):
                attrib['fill'] = str(rgbFace)
            if len(rgbFace) == 4 and rgbFace[3] != 1.0 and not forced_alpha:
                attrib['fill-opacity'] = str(rgbFace[3])

        if forced_alpha and self.get_alpha() != 1.0:
            attrib['opacity'] = str(self.get_alpha())

        offset, seq = self.get_dashes()
        if seq is not None:
            attrib['line-dasharray'] = ','.join(['%f' % val for val in seq])
            attrib['line-dashoffset'] = six.text_type(float(offset))

        linewidth = self.get_linewidth()
        if linewidth:
            rgb = self.get_rgb()
            attrib['line'] = str(rgb)
            if not forced_alpha and rgb[3] != 1.0:
                attrib['line-opacity'] = str(rgb[3])
            if linewidth != 1.0:
                attrib['line-width'] = str(linewidth)
            if self.get_joinstyle() != 'round':
                attrib['line-linejoin'] = self.get_joinstyle()
            if self.get_capstyle() != 'butt':
                attrib['line-linecap'] = _capd[self.get_capstyle()]
        return attrib


class TimerKivy(TimerBase):
    def _timer_start(self):
        # Need to stop it, otherwise we potentially leak a timer id that will
        # never be stopped.
        self._timer_stop()
        self._timer = Clock.schedule_interval(self._on_timer, self._interval / 1000.0)

    def _timer_stop(self):
        if self._timer is not None:
            Clock.unschedule(self._timer)
            self._timer = None

    def _timer_set_interval(self):
        # Only stop and restart it if the timer has already been started
        if self._timer is not None:
            self._timer_stop()
            self._timer_start()

    def _on_timer(self, dt):
        super(TimerKivy, self)._on_timer()


class FigureCanvasKivy(FocusBehavior, Widget, FigureCanvasBase):
    '''FigureCanvasKivy class. See module documentation for more information.
    '''

    def __init__(self, figure, **kwargs):
        Window.bind(mouse_pos=self._on_mouse_pos)
        self.bind(size=self._on_size_changed)
        self.bind(pos=self._on_pos_changed)
        self.entered_figure = True
        self.figure = figure
        super(FigureCanvasKivy, self).__init__(figure=self.figure, **kwargs)

    def draw(self):
        self.clear_widgets()
        self.canvas.clear()
        self._renderer = RendererKivy(self)
        self.figure.draw(self._renderer)

    def on_touch_down(self, touch):
        newcoord = self.to_widget(touch.x, touch.y, relative=True)
        x = newcoord[0]
        y = newcoord[1]

        if super(FigureCanvasKivy, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos):
            self.motion_notify_event(x, y, guiEvent=None)

            touch.grab(self)
            if 'button' in touch.profile and touch.button in ("scrollup", "scrolldown",):
                self.scroll_event(x, y, 5, guiEvent=None)
            else:
                self.button_press_event(x, y, self.get_mouse_button(touch),
                                        dblclick=False, guiEvent=None)
            if self.entered_figure:
                self.enter_notify_event(guiEvent=None, xy=None)
        else:
            if not self.entered_figure:
                self.leave_notify_event(guiEvent=None)
        return False

    def on_touch_move(self, touch):
        newcoord = self.to_widget(touch.x, touch.y, relative=True)
        x = newcoord[0]
        y = newcoord[1]
        inside = self.collide_point(touch.x, touch.y)
        if inside:
            self.motion_notify_event(x, y, guiEvent=None)
        if not inside and not self.entered_figure:
            self.leave_notify_event(guiEvent=None)
            self.entered_figure = True
        elif inside and self.entered_figure:
            self.enter_notify_event(guiEvent=None, xy=(x, y))
            self.entered_figure = False
        return False

    def get_mouse_button(self, touch):

        if 'button' in touch.profile:
            if touch.button == "left":
                return 1
            elif touch.button == "middle":
                return 2
            elif touch.button == "right":
                return 3
        return 1

    def on_touch_up(self, touch):

        newcoord = self.to_widget(touch.x, touch.y, relative=True)
        x = newcoord[0]
        y = newcoord[1]
        if touch.grab_current is self:
            if 'button' in touch.profile and touch.button in ("scrollup", "scrolldown",):
                self.scroll_event(x, y, 5, guiEvent=None)
            else:
                self.button_release_event(x, y, self.get_mouse_button(touch), guiEvent=None)
            touch.ungrab(self)
        else:
            return super(FigureCanvasKivy, self).on_touch_up(touch)
        return False

    def keyboard_on_key_down(self, window, keycode, text, modifiers):

        self.key_press_event(keycode[1], guiEvent=None)
        return super(FigureCanvasKivy, self).keyboard_on_key_down(window,
                                                    keycode, text, modifiers)

    def keyboard_on_key_up(self, window, keycode):

        self.key_release_event(keycode[1], guiEvent=None)
        return super(FigureCanvasKivy, self).keyboard_on_key_up(window, keycode)

    def _on_mouse_pos(self, *args):

        pos = args[1]
        newcoord = self.to_widget(pos[0], pos[1], relative=True)
        x = newcoord[0]
        y = newcoord[1]
        inside = self.collide_point(*pos)
        if inside:
            self.motion_notify_event(x, y, guiEvent=None)
        if not inside and not self.entered_figure:
            self.leave_notify_event(guiEvent=None)
            self.entered_figure = True
        elif inside and self.entered_figure:
            self.enter_notify_event(guiEvent=None, xy=(pos[0], pos[1]))
            self.entered_figure = False

    def enter_notify_event(self, guiEvent=None, xy=None):
        event = Event('figure_enter_event', self, guiEvent)
        self.callbacks.process('figure_enter_event', event)

    def leave_notify_event(self, guiEvent=None):
        event = Event('figure_leave_event', self, guiEvent)
        self.callbacks.process('figure_leave_event', event)

    def _on_pos_changed(self, *args):
        self.draw()

    def _on_size_changed(self, *args):

        w, h = self.size
        dpival = self.figure.dpi
        winch = float(w) / dpival
        hinch = float(h) / dpival
        self.figure.set_size_inches(winch, hinch, forward=False)
        self.resize_event()
        self.draw()

    def callback(self, *largs):
        self.draw()

    def blit(self, bbox=None):

        self.blitbox = bbox

    filetypes = FigureCanvasBase.filetypes.copy()
    filetypes['png'] = 'Portable Network Graphics'

    def print_png(self, filename, *args, **kwargs):

        fig = FigureCanvasAgg(self.figure)
        FigureCanvasAgg.draw(fig)

        l, b, w, h = self.figure.bbox.bounds
        texture = Texture.create(size=(w, h))
        texture.blit_buffer(bytes(fig.get_renderer().buffer_rgba()),
                                colorfmt='rgba', bufferfmt='ubyte')
        texture.flip_vertical()
        img = Image(texture)
        img.save(filename)

    def get_default_filetype(self):
        return 'png'

    def new_timer(self, *args, **kwargs):
        return TimerKivy(*args, **kwargs)


class FigureManagerKivy(FigureManagerBase):
    def __init__(self, canvas, num):
        super(FigureManagerKivy, self).__init__(canvas, num)
        self.canvas = canvas
        self.toolbar = self._get_toolbar()

    def show(self):
        pass

    def get_window_title(self):
        return Window.title

    def set_window_title(self, title):
        Window.title = title

    def resize(self, w, h):
        if (w > 0) and (h > 0):
            Window.size = w, h

    def _get_toolbar(self):
        if rcParams['toolbar'] == 'toolbar2':
            toolbar = NavigationToolbar2Kivy(self.canvas)
        else:
            toolbar = None
        return toolbar


global gio
gio=FigureCanvasKivy

FigureCanvas = FigureCanvasKivy
FigureManager = FigureManagerKivy
NavigationToolbar = NavigationToolbar2Kivy
import matplotlib.pyplot as mpl

def geovannif(g):
    g= Figure()
    e= FigureCanvasKivy(g)
    return e

def geovannig(ge):
    ge= mpl.gcf()
    eo= FigureCanvasKivy(ge)
    return eo

class geovanni(FigureCanvasKivy):
    def __init__(self,**kwargs):
        geovanni=FigureCanvasKivy()

        return geovanni

print('final')






