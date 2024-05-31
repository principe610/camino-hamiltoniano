

from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.app import App
from kivy.lang import Builder
import viajero1
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy_garden.graph import Graph,LinePlot,MeshLinePlot,PointPlot,ScatterPlot
from kivy.uix.slider import Slider
from math import cos,sin,sqrt,pi,acos
from viejo1 import *
from numpy import *
from viajero1 import *
import random
from matplotlib.figure import Figure
from kivy.properties import ObjectProperty, NumericProperty, StringProperty,BooleanProperty
from matplotlib.backend_bases import NavigationToolbar2
import matplotlib.pyplot as mpl




print('autor: geovanni burgos')
print('bien venido programador')
print('espera...esta sucediendo la magia...')





class p1(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        boxu=BoxLayout(orientation='horizontal')
        self.graph=Graph(
            xlabel='x',ylabel='y',
            x_grid=True,y_grid=True,
            xmin=-5,xmax=5,ymin=-5,ymax=5,
            border_color=[0,1,1,1])

        self.plot_uno=LinePlot(color=[0,1,1,1])
        self.plot_dos=LinePlot(color=[0,1,1,1])
        self.p3=LinePlot(color=[0,1,1,1])
        self.p4=LinePlot(color=[0,1,1,1])
        self.plot_uno.points=[(x,((sqrt(1-(abs(x)-1)**2)))) for x in range(-2,3) ]
        self.plot_dos.points=[(x,((acos(1-abs(x))-pi))) for x in range(-2,3)]
        
        
        tu=Label(text='Introduccion  P frente a NP:',color='#00FFFF')
        tu2=Label(text='Si es facil comprobar que la solucion a un problema\n'
            'es correcta ¿es tambien facil resolver el problema? ',color='#00FFFF')
        tu3=Label(text='esta es la tipica esencia de la pregunta P vs NP. ',color='#00FFFF')
        tu4=Label(text='Tipico de los problemas NP ',color='#00FFFF')
        tu5=Label(text='es el problema del camino hamiltoniano:\n'
                  'dadas N ciudades para visitar ¿como',color='#00FFFF')
        tu55=Label(text= 'se puede hacer esto sin visitatar una ciudad 2 veces?,',color='#00FFFF')
        tu6=Label(text='                Si me das una solucion \n'
                  'puedo comprobar facilmente que es correcta. ',color='#00FFFF')
        tu8=Label(text='pero no puedo encontrar una solucion tan facilmente.',color='#00FFFF')

        self.der=Button(text='    Este programa resuelve el problema del camino\n'
                   '      hamiltoniano:dadas N ciudades para visitar,\n'
                   '  ¿como se puede hacer esto sin visitatar una ciudad\n'
                   '  2 veces? lo unico que necesitas es la posicion (X,Y)\n'
                   '       de la ciudad,el programa se encarga de crear\n'
                   '   las distancias reales,escoge una opcion haciendo\n'
                   '           doble click en Aleatorio o Determinista',background_color=[1,0,1,1],color='#00FFFF')
        '''der3=Label(text='¿como se puede hacer esto sin visitatar una ciudad 2 veces? lo unico que necesitas es la',color=[1,0,1,1])
        der5=Label(text='posicion (X,Y) de la ciudad,el programa se encarga de crear las distancias reales,acontinuacion',color=[1,0,1,1])
        der6=Label(text='escoge una opcion Aleatorio o Determinista',color=[1,0,1,1])'''
        
        der=self.der
        self.graph.add_plot(self.plot_uno)
        self.graph.add_plot(self.plot_dos)
        self.graph.add_plot(self.p3)
        self.graph.add_plot(self.p4)
        global value
        
        
        global ui
        ui=6
        self.slider_uno=Slider(min=1,max=30,orientation="horizontal")        
        self.slider_uno.bind(value=self.valor_slider_uno)
        
        
        
        
        #boxu.add_widget(slider_dos)
        #boxu.add_widget(graph)
        self.dt5=Button(text='    estas son las 4 formas\n'
                   '      hablando para N ciudades ,\n'
                   '  que el programa omite \n'
                   '  ya que se resuelven a la vista',background_color=[1,0,1,1],color='#00FFFF')
        
        self.box=BoxLayout(orientation="vertical")
        #ggg=geovannig(mpl.gcf())
        self.titulo=Button(text="INSTRUCCIONES",background_color=[0,1,1,1],color='#00FFFF')#,color='#00FFFF')	
        der.bind(on_press=self.pas1)
        self.b=Button(text="Salir",background_color=[0,255,0],color=[0,0,255])
        b=self.b
        b.bind(on_press=self.un)
        bd=Button(text='          DETERMINISTA;\n'
                  '         el usuario genera\n'
                  '              las ciudades',center_x=True,background_color=[0,0,255])#,color=[0,255,0])
        bd.bind(on_press=self.ipd)
        ba=Button(
            text='          ALEATORIO:\n'
            '   el programa genera las\n'
            '          ciudades al azar',center_x=True,
            background_color=[0,0,255])#,      
            #color=[0,0,255])
        ba.bind(on_press=self.ipa)
        self.btt=Button(text="TITULO",font_size=30,background_color=[0,0,255])#,color='pink',text_size=33,background_color='#00FFFF')
        self.btt.bind(on_press=self.u)
        l=Label(text="bienvenido programador")
        t1=TextInput()
        b3=BoxLayout(orientation='vertical',size_hint_y=.30)
        b4=BoxLayout(size_hint_y=.22)
        self.b5=BoxLayout(size_hint_y=.21)
        b1=Button(text="imprimir",background_color='yellow')
        
        b3.add_widget(tu)
        b3.add_widget(tu2)
        b3.add_widget(tu3)
        b3.add_widget(tu4)
        b3.add_widget(tu5)
        b3.add_widget(tu55)
        b3.add_widget(tu6)
        
        b3.add_widget(tu8)
        b44=BoxLayout(orientation='vertical',size_hint_y=.2)
        self.b444=BoxLayout(size_hint_y =.07)
        
        b4.add_widget(ba)
        b44.add_widget(der)
        
        #b44.add_widget(der3)
        
        
        #b44.add_widget(der5)
        #b44.add_widget(der6)
        
   
        
        b4.add_widget(bd)
        self.cx=0
        self.b5.add_widget(b)
        #b5.add_widget(slider_dos)
        
        
        self.b5.add_widget(self.graph)
        self.b5.add_widget(self.slider_uno)
        self.box.add_widget(b3)
        self.box.add_widget(b44)
        self.box.add_widget(b4)
        self.box.add_widget(self.b5)
        

        self.add_widget(self.box)
		
		
        
    def u(self,*args):
        
        exit()
    def un(self,*args):

        
        a=self.slider_uno.value
        if a>9.5 and a<11:
            self.slider_uno.max=60                   
            self.b.disabled=True

        else:
            exit()
    def ipa(self,*args):
        self.manager.current='p22'

    def ipd(self,*args):
        self.manager.current='p3'

    
    def vr(self,*args):


        
        self.cx +=1
        if self.cx==3:
            print('llegaste')
        

    def valor_slider_uno(self,instance,value):
        print(value)

        if value>58:
            
            self.b5.remove_widget(self.slider_uno)
            
            self.b5.remove_widget(self.graph)
            frt2=Button(text='multi-boton')
            frt2.bind(on_press=self.vr)
            self.b5.add_widget(frt2)           
            
        else:            
            self.p3.points=[(x,((sqrt(1-(abs(x)-1)**2)/(value*.1)))) for x in range(-2,3) ]
        
            self.p4.points=[(x,((acos(1-abs(x))-pi)/(value*.1))) for x in range(-2,3)]



    def pas1(self,*args):
        a=self.slider_uno.value
        
        print('hlaaaaa')

        if a>=5:
            self.slider_uno.max=15        
            
            self.der.disabled=True
class p3(Screen):#dt
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.xp=[]
        self.yp=[]
        self.listaxy=[]
        self.listax=[]
        self.listax2=[]
        self.lista_cd=[]
        self.lista_cd3=[]
        self.lista_cdnodo=[]
        self.lista_cds=[]
        self.lista_cdnodo3=[]
        self.lista_cds3=[]
        self.listay=[]
        self.listaf44=[]
        self.ffa=[]
        self.listay2=[]
        self.fig1= mpl.figure()
        self.fig1,self.ax=mpl.subplots()
        self.bvb33=True
        self.bvb333=True

        self.ax.plot(self.listax,self.listay,'o')
        self.ax.grid()
        mpl.title('Agregando Ciudades',fontsize=18,color='green')
        
        
        self.b=BoxLayout(orientation='vertical')
        self.bn=Button(text='Pantalla principal',background_color=[1,0,1,1])
        bn=self.bn
        bn.bind(on_press=self.cambiar)
        l1=Label(text='bien_venido_programador',color='#00FFFF')
        la1=Label(text='ingresa\n'
                  'valor X:',color='#00FFFF',size_hint_x=.2)
        la2=Label(text='ingresa\n'
                  'valor Y:',color='#00FFFF',size_hint_x=.2)

        self.l2=FigureCanvasKivy(self.fig1)
        
        
        
        
        
        
        
        
        l222222222=Label(text='esta es la pantalla 2')
        self.t1= TextInput(multiline=False,size_hint_x=.1,hint_text='  X',input_filter='int')
        self.t2= TextInput(multiline=False,size_hint_x=.1,hint_text='  Y',input_filter='int')
        self.bn2=Button(text='Agregar punto',size_hint_x=.4,background_color=[1,0,1,1])
        bn2=self.bn2
        bn2.bind(on_press=self.onpr)
        self.c1=BoxLayout(size_hint_y=.6,orientation='vertical')
        self.c2=BoxLayout(orientation='horizontal',size_hint_y=.1)
        self.c3=BoxLayout()
        c3=self.c3
        self.f5=BoxLayout(orientation='horizontal',size_hint_y=.1)
        #self.c1.add_widget(self.toolbar)
        self.c1.add_widget(self.l2)
        
        self.gtu=Button(text='ingresa el valor de X and Y en las casillas en blanco\n'
                   'posteriormente preciona agregar punto,el boton\n'
                   'resolver estara disponible al agregar 2 puntos',background_color=[0,255,0],color=[255,0,0])
        gtu=self.gtu
        self.f5.add_widget(gtu)
        self.c2.add_widget(la1)
        self.c2.add_widget(self.t1)
        self.c2.add_widget(bn2)
        self.c2.add_widget(la2)
        self.c2.add_widget(self.t2)
        self.contador=0
        self.contador2=0
        
        
        
        
        self.br2=Button(text='Limpiar',background_color= [1,0,1,1],disabled=True)
        br2=self.br2
        br2.bind(on_press=self.tito_y_su_burrito)
        self.br=Button(text='Resolver',background_color=[255,0,0],disabled=True)
        br=self.br
        br.bind(on_press=self.pre)
        
        
        c3.add_widget(bn)
        c3.add_widget(br)
        
        c3.add_widget(br2)
        self.c8p=BoxLayout(orientation='horizontal',size_hint_y=.2)
        self.c8p.add_widget(c3)
        


        
        self.b.add_widget(self.c1)
        self.b.add_widget(self.f5)
        self.b.add_widget(self.c2)
        self.b.add_widget(self.c8p)
        self.add_widget(self.b)

    def cambiar(self,*args):
        self.manager.current='p11'


    def pre(self,*args):
        fig1= mpl.figure()
        fig1,self.ax=mpl.subplots()
        self.ax.grid()
                
        listaxy=self.listaxy
        listax=self.listax
        listax2=self.listax2
        lista_cd=self.lista_cd
        lista_cd3=self.lista_cd3
        lista_cdnodo=self.lista_cdnodo
        lista_cds=self.lista_cds
        lista_cdnodo3=self.lista_cdnodo3
        lista_cds3=self.lista_cds3
        listay=self.listay
        listaf44=self.listaf44
        ffa=self.ffa
        listay2=self.listay2
        ur55=lista_igual(listax)
        ur555=lista_igual(listay)
        if (len(listax)==1 and len(listay)==1):
            self.br.disabled=True
            print('solo confia en mi')
            
        elif (ur555==True):
            self.bn2.disabled=True

            mpl.plot(self.listax,self.listay,'o')
            for grrr4,f,g in zip(ffa,listax,listay):
                
                mpl.text(f,g,str(grrr4),fontsize=12)
            mpl.plot(self.listax,self.listay)

            
            self.c1.remove_widget(self.l2)
            self.l2=FigureCanvasKivy(mpl.gcf())
            self.c1.add_widget(self.l2)
            self.br.disabled=True
            mpl.close()

        elif (ur55==True):
            self.bn2.disabled=True
            for grrr4,f,g in zip(ffa,listax,listay):
                
                mpl.text(f,g,str(grrr4),fontsize=12)

            mpl.plot(self.listax,self.listay,'o')
            
            

            
            self.c1.remove_widget(self.l2)
            self.l2=FigureCanvasKivy(mpl.gcf())
            self.c1.add_widget(self.l2)
            self.br.disabled=True
            mpl.close()

        elif (listax==listay):
            self.bn2.disabled=True
            for grrr4,f,g in zip(ffa,listax,listay):
                
                mpl.text(f,g,str(grrr4),fontsize=12)

            mpl.plot(self.listax,self.listay,'o')
            
            mpl.plot(self.listax,self.listay)

            
            self.c1.remove_widget(self.l2)
            self.l2=FigureCanvasKivy(mpl.gcf())
            self.c1.add_widget(self.l2)
            self.br.disabled=True
            mpl.close()

        

        else:
            
            
        
            for x,y,z in zip(listax,listay,ffa):
                tt7=nodo(x,y)
                grpunto(tt7)
                mpl.text(x,y,z,color='b',fontsize=12)
            ux=menor(listax)
            wx=mayor(listax)
            vy=menor(listay)
            my=mayor(listay)
            k= nodo(ux,vy)#(1,6)
            t=nodo(wx,vy)#(2,6)
            j=nodo(wx,my)
            I=nodo(ux,my)

            l1=distancia2p(k,t)
            gggg=wx+10
            ggg=ux-10
            #mpl.xlim((ggg),(gggg))
            #mpl.ylim((vy-50),(my+50))

            l2=distancia2p(t,j)

            p1=((l1/3)+ux)
            pz=(l1/20)
            p2=((2*(l1/3))+ux)
            pm=(l2/2)+vy+.23
            pm1=nodo(ux,(pm))
            pm2=nodo(wx,(pm))

            p11=nodo((p1),vy)
            p12=nodo((p1),my)
            p21=nodo((p2),vy)

            p22=nodo((p2),my)


            def empezar(cd33):
                cd33=nodo(cd33.x,cd33.y)
                wqqq=cd33.id
                for x,y,z in zip(listax,listay,ffa):
                    if cd33.x==x and cd33.y==y:
                        global prin
                        global prin2
                        prin=str('ubica el nodo '+str(z)+' esta en ('+str(x)+','+str(y)+')')

                global nuevo_nodo
                nuevo_nodo=cd33
                        
                
                """lq=[]
                lgq=[]
                ff=0
                gfd=[]
                gfds=[]
                po=[]
                po2=[]
                for xo,yo in zip(listax,listay):
                    if xo==cd3.x:
                        if yo<pm and yo>cd3.y:
                            ui=nodo(xo,yo)
                            gfd.append(ui)
                            sa=distancia2p(cd3,ui)
                            gfds.append(sa)
                    if xo<cd3.x and yo<pm:
                        v6677= nodo(xo,yo)
                        lq.append(v6677)
                        geo6677=distancia(cd3,v6677)
                        lgq.append(geo6677)            
                    ff +=1
                    
                try:        
                    nb19=menor(gfds)
                    lk=0
                    for x8o in gfds:
                        if x8o==nb19:
                            uut22=gfd[lk]
                            for xmn,ymn,zmn in zip(listax,listay,ffa):
                                if cd3.x==xmn and cd3.y==ymn:
                                    for xu,yu,u2 in zip(listax,listay,ffa):
                                        if uut22.x==xu and uut22.y==yu:
                                            parp=u2
                                    gio2=distancia2p(cd3,uut22)
                                    #print(z,'->',parp,'distancia=',gio2)
                                    lista_cd.append(zmn)
                                    lista_cds.append(parp)
                                    lista_cdnodo.append(gio2)

                                    
                            nuevo_nodo=uut22
                            grrecta(cd3,uut22)
                            mostrar(cd3,uut22)
                            

                        lk+=1
                                
                except:
                    try:
                        men46=menor(lgq)            
                        j5=0
                        for x,y in zip(lgq,lq):
                            if x==men46:
                                po.append(y)
                                fff33=distancia2p(cd3,y)
                                po2.append(fff33)

                        zzz2=menor(po2)
                        contador22=0
                        for x,y in zip(po,po2):
                                if zzz2==y:
                                    contador22+=1
                                    if contador22==1:
                                        n558=(x)
                                        for x,y,z in zip(listax,listay,ffa):
                                            if cd3.x==x and cd3.y==y:
                                                for x,y,u in zip(listax,listay,ffa):
                                                    if n558.x==x and n558.y==y:
                                                        parp2=u
                                                gio3=distancia2p(cd3,n558)
                                                #print(z,'->',parp,'distancia=',gio3)
                                                lista_cd.append(z)
                                                lista_cds.append(parp2)
                                                lista_cdnodo.append(gio3)
                                        nuevo_nodo=n558
                                        #print('la ciudad es',nuevo_nodo)
                                        grrecta(cd3,n558)
                                        mostrar(cd3,n558)
                            
                    except:
                        nuevo_nodo=cd3"""


            def avanzarg(cd4):
                global nuevo_nodo
                
                   
                cd4=nodo(cd4.x,cd4.y)
                d1=0
                lq1=[]
                lq2=[]
                lq3=[]
                lq4=[]
                lq5=[]
                lq6=[]
                gj=[]
                jj=[]
                ff=0
                
                for y,x in zip(listay,listax):
                    if y<pm:
                        if x==cd4.x :                
                            if y<cd4.y and y<pm:
                                v77= nodo(x,y)
                                lq1.append(v77)
                                geo=distancia2p(cd4,v77)
                                lq2.append(geo)            
                            if y>cd4.y and y<pm:
                                v25= nodo(x,y)
                                lq3.append(v25)
                                geo2=distancia2p(cd4,v25)
                                lq4.append(geo2)
                                                
                        if x<cd4.x and y<pm:
                            v555= nodo(x,y)
                            lq5.append(v555)
                            geo3333=distancia(cd4,v555)
                            lq6.append(geo3333)            
                    
                #aqui hay un error de codigo
                try:
                    ce=menor(lq2)
                    lk=0
                    for cr in lq2:
                        if cr==ce:
                            uut=lq1[lk]
                            for x,y,z in zip(listax,listay,ffa):
                                if cd4.x==x and cd4.y==y:
                                    for x99,y99,u99 in zip(listax,listay,ffa):
                                        if uut.x==x99 and uut.y==y99:
                                            parp3=u99
                                            
                                    gio4=distancia2p(cd4,uut)
                                    #print(z,'->',parp3,'distancia=',gio4)
                                    lista_cd.append(z)
                                    lista_cds.append(parp3)
                                    lista_cdnodo.append(gio4)       
                            
                            nuevo_nodo=uut

                            #print('el nuevo nodo es',nuevo_nodo)
                            grrecta(cd4,uut)
                            mostrar(cd4,uut)
                            h=0
                            for w,q,z in zip(listax,listay,ffa):
                                if cd4.x==w and cd4.y==q:
                                    ffa.pop(h)
                                    listax.pop(h)
                                    listay.pop(h)
                                h +=1
                                           
                        lk+=1
                                
                except:
                    try:            
                        men=menor(lq4)
                        j5=0
                        for x in lq4:                
                            if x==men:
                                tw=lq3[j5]
                                for x,y,z in zip(listax,listay,ffa):
                                    if cd4.x==x and cd4.y==y:
                                        for x,y,u in zip(listax,listay,ffa):
                                            if tw.x==x and tw.y==y:
                                                parp4=u
                                        gio5=distancia2p(cd4,tw)
                                        #print(z,'->',parp4,'distancia=',gio5)
                                        lista_cd.append(z)
                                        lista_cds.append(parp4)
                                        lista_cdnodo.append(gio5)  
                                nuevo_nodo=tw
                                #print('el nuevo nodo es',nuevo_nodo)
                                grrecta(cd4,tw)
                                mostrar(cd4,tw)
                                hr=0
                                for w,q,mm in zip(listax,listay,ffa):
                                    if cd4.x==w and cd4.y==q:
                                        listax.pop(hr)
                                        ffa.pop(hr)
                                        listay.pop(hr)
                                    hr +=1
                                                  
                            j5+=1
                            
                    except:
                        try:
                            
                            
                            mn=menor(lq6)
                            for x,y in zip(lq6,lq5):                    
                                if x==mn:
                                    gj.append(y)
                                    fff=distancia2p(cd4,y)
                                    jj.append(fff)

                            zzz=menor(jj)
                            contador=0
                            for x,y in zip(gj,jj):
                                if zzz==y:
                                    contador+=1
                                    if contador==1:
                                        n55=(x)
                                        for x,y,z in zip(listax,listay,ffa):
                                            if cd4.x==x and cd4.y==y:
                                                for x,y,u in zip(listax,listay,ffa):
                                                    if n55.x==x and n55.y==y:
                                                        parp5=u
                                                gio6=distancia2p(cd4,n55)
                                                #print(z,'->',parp5,'distancia=',gio6)
                                                lista_cd.append(z)
                                                lista_cds.append(parp5)
                                                lista_cdnodo.append(gio6)
                                        nuevo_nodo=n55
                                        #print('la ciudad es',nuevo_nodo)
                                        grrecta(cd4,n55)
                                        mostrar(cd4,n55)
                                        hry=0
                                        for w,q,nbaaa in zip(listax,listay,ffa):
                                            if cd4.x==w and cd4.y==q:
                                                listax.pop(hry)
                                                ffa.pop(hry)
                                                listay.pop(hry)
                                            hry +=1

                                        
                                                     
                                
                        except:
                            print('geovanni')

                
            def avanzar2(cd):
                global nuevo_nodo
                   
                cd=nodo(cd.x,cd.y)
                d1=0
                lq12=[]
                lq22=[]
                lq32=[]
                lq42=[]
                lq52=[]
                lq62=[]
                ff=0    
                
                for y,x in zip(listay,listax):
                    if y>=pm:
                        if x==cd.x and y>=pm:            
                            if y>(cd.y) and y<=my:
                                v= nodo(x,y)
                                lq12.append(v)
                                geo=distancia2p(cd,v)
                                lq22.append(geo)                    
                            if y<(cd.y) and y>=(pm):
                                v2= nodo(x,y)
                                lq32.append(v2)
                                geo2=distancia2p(cd,v2)
                                lq42.append(geo2)
                                            
                        if x>cd.x and y>=pm :
                            v66= nodo(x,y)
                            lq52.append(v66)
                            geo66=distancia(cd,v66)
                            lq62.append(geo66)                                    
                    ff +=1

                try:
                    nb66=menor(lq22)
                    lk=0
                    for x in lq22:            
                        if x==nb66:
                            uut44=lq12[lk]
                            for x,y,z in zip(listax,listay,ffa):
                                if cd.x==x and cd.y==y:
                                    for x,y,u in zip(listax,listay,ffa):
                                        if uut44.x==x and uut44.y==y:
                                            parp6=u
                                    gio7=distancia2p(cd,uut44)
                                    #print(z,'->',parp6,'distancia=',gio7)
                                    lista_cd3.append(z)
                                    lista_cds3.append(parp6)
                                    lista_cdnodo3.append(gio7)
                            
                            nuevo_nodo=uut44
                            #print('la ciudad  es',nuevo_nodo)
                            grrecta(cd,uut44)
                            mostrar(cd,uut44)
                            hr2=0
                            for w,q,mn in zip(listax,listay,ffa):
                                if cd.x==w and cd.y==q:
                                    listax.pop(hr2)
                                    ffa.pop(hr2)
                                    listay.pop(hr2)
                                hr2 +=1
                            
                        lk+=1
                                
                except:
                    try:
                        men55=menor(lq42)
                        j5=0
                        for x in lq42:                
                            if x==men55:                    
                                tw44=lq32[j5]
                                for x,y,z in zip(listax,listay,ffa):
                                    if cd.x==x and cd.y==y:
                                        for x,y,u in zip(listax,listay,ffa):
                                            if tw44.x==x and tw44.y==y:
                                                parp7=u
                                        gio8=distancia2p(cd,tw44)
                                        #print(z,'->',parp7,'distancia=',gio8)
                                        lista_cd3.append(z)
                                        lista_cds3.append(parp7)
                                        lista_cdnodo3.append(gio8)
                                nuevo_nodo=tw44
                                #print('el nuevo nodo es',nuevo_nodo)
                                grrecta(cd,tw44)
                                mostrar(cd,tw44)
                                hr3=0
                                for w,q,nnm in zip(listax,listay,ffa):
                                    if cd.x==w and cd.y==q:
                                        listax.pop(hr3)
                                        ffa.pop(hr3)
                                        listay.pop(hr3)
                                    hr3 +=1
                                
                            j5+=1

                    except:
                        try:
                            gj=0
                            mn33=menor(lq62)
                            qq=[]
                            ww=[]
                            for x,y in zip(lq62,lq52):                    
                                if x==mn33:
                                    qq.append(y)
                                    ss=distancia2p(cd,y)
                                    ww.append(ss)


                            dd=menor(ww)
                            con=0
                            for x,y in zip(ww,qq):
                                if x== dd:
                                    if con==0:
                                        n552=y
                                        for x,y,z in zip(listax,listay,ffa):
                                            if cd.x==x and cd.y==y:
                                                for x,y,u in zip(listax,listay,ffa):
                                                    if n552.x==x and n552.y==y:
                                                        parp8=u
                                                gio9=distancia2p(cd,n552)
                                                #print(z,'->',parp8,'distancia=',gio9)
                                                lista_cd3.append(z)
                                                lista_cds3.append(parp8)
                                                lista_cdnodo3.append(gio9)
                                        nuevo_nodo=n552
                                        #print('el nuevo nodo es',nuevo_nodo)
                                        grrecta(cd,n552)
                                        mostrar(cd,n552)
                                        hr4=0
                                        for w,q,sq in zip(listax,listay,ffa):
                                            if cd.x==w and cd.y==q:
                                                listax.pop(hr4)
                                                ffa.pop(hr4)
                                                listay.pop(hr4)
                                            hr4 +=1
                                        con+=1
                                                       
                                gj +=1
                                
                        except:
                            print('burgos')
                            
            def dentro_funcion(fs,funcion):
                global nuevo_nodo
                r=funcion(fs)
                return r

            uo=0
            uo1=0
            l88=[]
            l99=[]
            lista_arrivax=[]
            lista_arrivay=[]
            lista_abajox=[]
            lista_abajoy=[]
            lista_2p=[]
            lista_nodo=[]
            lista_2p2=[]
            lista_nodo2=[]
            llll=[]
            llll2=[]
            llll3=[]

            for y in listay2:
                x=listax2[uo]
                if y>=pm:
                    lista_arrivay.append(y)
                    lista_arrivax.append(x)
                uo+=1

            for y in listay2:
                x=listax2[uo1]
                if y<pm:
                    lista_abajoy.append(y)
                    lista_abajox.append(x)
                uo1+=1

            q1=menor(lista_arrivax)

            q3=menor(lista_abajox)
            q2=mayor(lista_abajox)
            q4=mayor(lista_arrivax)
            ao=0
            kfc=[]
            kf2=[]
            kf3=[]
            kf4=[]
            kf5=[]

            ppo=[]
            ppo1=[]
            ppo2=[]
            ppo3=[]
            uppo=[]
            uppo1=[]
            uppo2=[]
            uppo3=[]
            
            for x,y in zip(lista_arrivax,lista_arrivay):
                if x==q1:
                    kfc.append(y)
                    ao+=1

                    
            if ao==1:
                for x,y in zip(lista_arrivax,lista_arrivay):
                    if x==q1:
                        gt2=nodo(x,y)

            kfc3=mayor(kfc)            
            if ao>1:
                for x,y in zip(lista_arrivax,lista_arrivay):
                    if x==q1 and y==kfc3:
                        gt2=nodo(x,y)
                        
                
                        
            a=0
            
            for x,y in zip(lista_abajox,lista_abajoy):
                if x==q3:
                    kf2.append(y)
                    a+=1

            if a==1:
                for x,y in zip(lista_abajox,lista_abajoy):
                    if x==q3:
                        gf=nodo(x,y)
                        
            k45=menor(kf2)            
            if a>1:
                for x,y in zip(lista_abajox,lista_abajoy):
                    if x==q3 and y==k45:
                        gf=nodo(x,y)            
             


            aob=0
            
            for x,y in zip(lista_abajox,lista_abajoy):
                if x==q2:
                    kf3.append(y)
                    aob+=1

            if aob==1:
                for x,y in zip(lista_abajox,lista_abajoy):
                    if x==q2:
                        gar=nodo(x,y)
                        
            dffa=menor(kf3)
            if aob>1:
                for x,y in zip(lista_abajox,lista_abajoy):
                    if x==q2 and y==dffa:
                        gar=nodo(x,y)
                

                        
            ab=0
            
            for x,y in zip(lista_arrivax,lista_arrivay):
                if x==q4:
                    kf4.append(y)
                    ab+=1
                    
            if ab==1:   
                for xm,ym in zip(lista_arrivax,lista_arrivay):
                    if xm==q4:
                        gar2=nodo(xm,ym)
                        

            asqd=mayor(kf4)
            if ab>1:
                for xpp,ypp in zip(lista_arrivax,lista_arrivay):
                    if xpp==q4 and ypp==asqd:
                        gar2=nodo(xpp,ypp)

            el_ojo_ke_todo_LOVE=dispr(gar2,gf,gt2)
            gracias_gracias_gracias=dispr(gt2,gar2,gar)
            if gracias_gracias_gracias <=0 and gt2.x<gar2.x and gt2.x>gar.x:
                gt2=gar2
                
            if el_ojo_ke_todo_LOVE <=0 and gar2.x<gf.x and gar2.x>gt2.x:
                gar2=gt2

            

            for x,y in zip(listax,listay):
                if (x>=gar.x and x<=gar2.x) or (x<=gar.x and x>=gar2.x):
                    if (y>gar.y and y<gar2.y) :
                        ppp4=nodo(x,y)
                        rww4= dispr(ppp4,gar,gar2)
                        
                    
                        
                        if rww4>=0:
                            #print('el nodo agregado es',ppp4)
                            wwee4=distancia2p(gar2,ppp4)
                            lista_nodo2.append(ppp4)
                            lista_2p2.append(wwee4)



            zzzz=len(lista_nodo2)
            if zzzz==0:
                for xu,yu,zu in zip(listax,listay,ffa):
                    if gar.x==x and gar.y==y:
                        for x334,y66,uhj in zip(listax,listay,ffa):
                            if gar2.x==x334 and gar2.y==y66:
                                par77k=uhj
                                gi8=distancia2p(gar,gar2)
                        #print(z,'->',par7,'distancia=',gi8)
                                ppo.append(par77k)
                                ppo1.append(zu)
                                ppo2.append(gi8)
                grrecta(gar,gar2)
                mostrar(gar,gar2)

            if zzzz==1:
                for xk in lista_nodo2:
                    grrecta(gar2,xk)
                    mostrar(gar2,xk)
                    grrecta(xk,gar)
                    mostrar(xk,gar)

                    kkwq4=0       
                    for x22,y33,f88 in zip(listax,listay,ffa):
                        if x22==xk.x and y33==xk.y:
                            ppo1.append(f88)
                            listax.pop(kkwq4)
                            listay.pop(kkwq4)
                            ffa.pop(kkwq4)                        
                        kkwq4+=1
                            
                        if x22==gar.x and y33==gar.y:
                            ppo.append(f88)
                            g90=distancia2p(xk,gar)
                            ppo2.append(g90)
                    
                    for x21,y31,f81 in zip(listax,listay,ffa):
                        if x21==gar2.x and y31==gar2.y:
                            ppo.append(f81)
                            gi86=distancia2p(gar2,xk)
                            ppo2.append(gi86)
                    

            else:
                while len(lista_nodo2)>1:        
                    ccxx4=menor(lista_2p2)
                    vbb4=0
                    for xt,yt in zip(lista_nodo2,lista_2p2):
                        if yt==ccxx4:
                            coi4=0
                            for x4,y4,z34h in zip(listax,listay,ffa):
                                if xt.x==x4 and xt.y==y4:
                                    grrecta(gar2,xt)
                                    mostrar(gar2,xt)
                                    ppo1.append(z34h)
                                    for x6j,y6j,uj in zip(listax,listay,ffa):
                                        if gar2.x==x6j and gar2.y==y6j:                                
                                            ppo.append(uj)
                                            ppo2.append(yt)
                                    gar2=xt
                                    listax.pop(coi4)
                                    listay.pop(coi4)
                                    ffa.pop(coi4)
                                coi4+=1

                            lista_nodo2.pop(vbb4)
                            lista_2p2.pop(vbb4)
                        
                        vbb4+=1
                    len(lista_nodo2)

                    if len(lista_nodo2)==1:
                        for x in lista_nodo2:
                            grrecta(gar2,x)
                            mostrar(gar2,x)
                            grrecta(x,gar)
                            mostrar(x,gar)
                            kwq4=0
                            for x21,y31,f81 in zip(listax,listay,ffa):
                                if x21==gar2.x and y31==gar2.y:
                                    ppo.append(f81)
                                    gi86=distancia2p(gar2,x)
                                    ppo2.append(gi86)
                                    
                            for x22,y33,f88 in zip(listax,listay,ffa):
                                if x22==x.x and y33==x.y:
                                    ppo1.append(f88)
                                    listax.pop(kwq4)
                                    listay.pop(kwq4)
                                    ffa.pop(kwq4)                        
                                kwq4+=1
                                    
                                if x22==gar.x and y33==gar.y:
                                    ppo.append(f88)
                                    g90=distancia2p(x,gar)
                                    ppo2.append(g90)        
                
            for x,y in zip(listax,listay):
                if (x>=gf.x and x<=gt2.x) or (x<=gf.x and x>=gt2.x):
                    if (y>gf.y and y<gt2.y) :
                        ppp22=nodo(x,y)
                        rww= dispr(ppp22,gt2,gf)

                        
                        if rww>=0:
                            
                            wwee1=distancia2p(gf,ppp22)
                            lista_nodo.append(ppp22)
                            lista_2p.append(wwee1)

                        if rww<0 and ppp22.y<pm and ppp22.x==gf.x and ppp22.y != gf.y:
                            
                            wwee11=distancia2p(gf,ppp22)
                            lista_nodo.append(ppp22)
                            lista_2p.append(wwee11)

            if len(lista_nodo)==0:
                for xh,yh,zh in zip(listax,listay,ffa):
                    if gf.x==xh and gf.y==yh:
                        uppo.append(zh)
                        for xd,ydf,uq in zip(listax,listay,ffa):
                            if gt2.x==xd and gt2.y==ydf:
                                par6767=uq
                                uppo1.append(par6767)
                        gip8=distancia2p(gf,gt2)
                        #print(z,'->',par7,'distancia=',gi8)            
                        uppo2.append(gip8)
                grrecta(gf,gt2)
                mostrar(gf,gt2)


            if len(lista_nodo)==1:
                
                for xkw in lista_nodo:
                    grrecta(gt2,xkw)
                    mostrar(gt2,xkw)
                    grrecta(xkw,gf)
                    mostrar(xkw,gf)

                    k4=0       
                    for x2211,y3311,f88h in zip(listax,listay,ffa):
                        if x2211==xkw.x and y3311==xkw.y:
                            uppo1.append(f88h)
                            listax.pop(k4)
                            listay.pop(k4)
                            ffa.pop(k4)                        
                        k4+=1
                            
                        if x2211==gf.x and y3311==gf.y:
                            uppo.append(f88h)
                            g900=distancia2p(xkw,gf)
                            uppo2.append(g900)
                    
                    for x2111,y3111,f8111 in zip(listax,listay,ffa):
                        if x2111==gt2.x and y3111==gt2.y:
                            uppo.append(f8111)
                            gi8611=distancia2p(gt2,xkw)
                            uppo2.append(gi8611)
            else:
                while len(lista_nodo)>1:        
                    ccxx=menor(lista_2p)
                    v4=0
                    for xt5,yt5 in zip(lista_nodo,lista_2p):
                        if yt5==ccxx:
                            ci4=0
                            for x45,y45,z45 in zip(listax,listay,ffa):
                                if xt5.x==x45 and xt5.y==y45:
                                    grrecta(gf,xt5)
                                    mostrar(gf,xt5)
                                    uppo1.append(z45)
                                    for x6j,y6j,uj in zip(listax,listay,ffa):
                                        if gf.x==x6j and gf.y==y6j:                                
                                            uppo.append(uj)
                                            uppo2.append(yt5)
                                    gf=xt5
                                    listax.pop(ci4)
                                    listay.pop(ci4)
                                    ffa.pop(ci4)
                                ci4+=1

                            lista_nodo.pop(v4)
                            lista_2p.pop(v4)
                        
                        v4+=1
                    len(lista_nodo)

                    if len(lista_nodo)==1:
                        for x in lista_nodo:
                            grrecta(gt2,x)
                            mostrar(gt2,x)
                            grrecta(x,gf)
                            mostrar(x,gf)
                            kwq4=0
                            for x21,y31,f81 in zip(listax,listay,ffa):
                                if x21==gt2.x and y31==gt2.y:
                                    uppo.append(f81)
                                    gi86=distancia2p(gt2,x)
                                    uppo2.append(gi86)
                                    
                            for x22,y33,f88 in zip(listax,listay,ffa):
                                if x22==x.x and y33==x.y:
                                    uppo1.append(f88)
                                    listax.pop(kwq4)
                                    listay.pop(kwq4)
                                    ffa.pop(kwq4)                        
                                kwq4+=1
                                    
                                if x22==gf.x and y33==gf.y:
                                    uppo.append(f88)
                                    g90=distancia2p(x,gf)
                                    uppo2.append(g90) 

                    
            global nuevo_nodo               
            empezar(gar)
            for y in lista_abajox:
                try:            
                    dentro_funcion(nuevo_nodo,avanzarg)
                                
                except:
                    print('tu solo confia en mi')




            nuevo_nodo=gt2



            for y in lista_arrivax:
                try:
                    dentro_funcion(nuevo_nodo,avanzar2)

                except:
                    print('gracias,gracias,gracias')
            print('********************************************************')
            print('********************************************************')
            print ('te devuelvo la lista en orden con sus distancia reales')
            print(prin)
            print('lo usaremos como punto de partida y punto final')

            for x,y,z in zip(uppo,uppo1,uppo2):
                lista_cd.append(x)
                lista_cds.append(y)
                lista_cdnodo.append(z)

                
            for x,y,z in zip(lista_cd3,lista_cds3,lista_cdnodo3):
                lista_cd.append(x)
                lista_cds.append(y)
                lista_cdnodo.append(z)
                


                
            for x,y,z in zip(ppo,ppo1,ppo2):
                lista_cd.append(x)
                lista_cds.append(y)
                lista_cdnodo.append(z)
            a=0
            ay=[]
            print('esta es la lista ordenada:')
            for x,y in zip(lista_cd,lista_cds):
                print(x)

                
            print(lista_cds[-1])
            print('nuevamente->',lista_cd[0])
            print('*********************************************************')
            print('esta es la lista ordenada con distancias:')


            for x,y,z in zip(lista_cd,lista_cds,lista_cdnodo):
                print('(',x,'->',y,')','distancia=',z)

            
            
            mpl.title('Camino Hamiltoniano resuelto',fontsize=18,color=[1,0,1,1])
            mpl.grid()
        
            
            self.c1.remove_widget(self.l2)
            self.c1.remove_widget(self.box1)
            mpl.grid()
            
            self.box1=BoxLayout(size_hint_y=.1)
            box1=self.box1   
            self.l2=FigureCanvasKivy(mpl.gcf())

            self.tol=NavigationToolbar2(self.l2)
            tol=self.tol
            for text, tooltip_text, image_file, callback in tol.toolitems:
                if text is None:
                    #actionview.add_widget(ActionSeparator())
                    continue
                #fname = os.path.join(basedir, image_file + '.png')
                if text in ['Pan', 'Zoom','Save','Subplots','Home','Forward','Back']:
                    if text == 'Subplots':
                        pass

                        action_button4 = Button(text=text)

                    if text == 'Home':
                        action_button45 = Button(text='Original',background_color=[0,255,9],color=[0,0,255])

                        action_button45.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button45)
                        #print(callback)
                    if text == 'Back':
                        action_button42 = Button(text='Atras',background_color=[0,255,9],color=[0,0,255])


                        action_button42.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button42)
                        #print(callback)

                   
                    if text == 'Forward':
                        action_button2 = Button(text='Adelante',background_color=[0,255,9],color=[0,0,255])
                
                        action_button2.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button2)
                        #print(callback)
                    if text == 'Pan':
                        action_button46 = Button(text='mover',background_color=[0,255,9],color=[0,0,255])


                        action_button46.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button46)
                        #print(callback)

                   

                    if text == 'Zoom':
                        self.btn11 = Button(text='Zoom',background_color=[0,255,0],color=[0,0,255])


                        self.btn11.bind(on_press=self.callback311)
                        self.btn11.bind(on_press=getattr(tol, callback))
                        self.box1.add_widget(self.btn11)
                        
                    if text == 'Save':
                        self.acn3 = Button(text='Guardar',background_color=[0,255,9],color=[0,0,255])
                
                        self.acn3.bind(on_press=self.guardar11)
                        self.box1.add_widget(self.acn3)
                        


                else:
                    action_button = text
                    action_button = Button(text=text)


                    try:
                        action_button.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button)
                        
                    except:
                        pass
            
            
         
            self.b.remove_widget(self.f5)
            self.c1.add_widget(self.l2)
            #
            self.c1.add_widget(self.box1)
            #self.c1.size_hint_y=.7

            #self.bzo=Button(text='zoom',background_color=[0,255,255],color=(255,0,0))
            #bzo=self.bzo
            #self.bgu=Button(text='guardar imagen',background_color=[0,255,255],color=[255,0,0])
            #self.bgu.bind(on_press=self.guardar)
            #self.c1.add_widget(box1)
            #self.f5.add_widget(box1)
            #bzo.bind(on_press=self.zzom)
            
            """self.listax.clear()
            self.listay.clear()
            self.xp.clear()
            self.yp.clear()
            self.listaxy.clear()
            self.listax.clear()
            self.listax2.clear()
            self.lista_cd.clear()
            self.lista_cd3.clear()
            self.lista_cdnodo.clear()
            self.lista_cds.clear()
            self.lista_cdnodo3.clear()
            self.lista_cds3.clear()
            self.listay.clear()
            self.listaf44.clear()
            self.ffa.clear()
            self.listay2.clear()"""
            self.contador2=0
            self.br.disabled=True
            self.bn2.disabled=True

            
            #mpl.close()
    
    
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path):
        c=random.randint(1,1000)
        
        geovani_te_ama='geo'+str(c)+'.png'
        filename=geovani_te_ama#mpl.savefig(geovani_te_ama)

        self.l2.export_to_png(os.path.join(path, filename))
        self.dismiss_popup()
        print('path',path)
        print('filename',filename)

    def sa(self, *args):
        self.show_save()

    

    def guardar11(self,*args):
        self.acn3.background_color='green'    

        self.acn3.color='white'    
        cy=random.randint(1,1000)
        #mpl.grid()
        mpl.draw()
        geovani_te_ama='camino_hamiltoniano'+str(cy)+'.png'
        mpl.savefig(geovani_te_ama)
        print('se guardo la imagen')
        print('geovani_te_ama',geovani_te_ama)
        #self.acn3.background_color=[0,255,9]
    
    def guardar12(self,*args):
        self.acn33.background_color='green' 
        self.acn33.color='white'    

        cy=random.randint(1,1000)
        #mpl.grid()
        mpl.draw()
        geovani_te_ama='camino_hamiltoniano'+str(cy)+'.png'
        self.l2.export_to_png(geovani_te_ama)
        print('se guardo la imagen')
        print('geovani_te_ama',geovani_te_ama)
        #self.acn33.background_color=[0,255,9]
    def zzom(self,*args):
        mpl.grid()
        self.bn.disabled=True
        self.br2.disabled=True
        self.bzo.disabled=True
        self.bgu.disabled=True
        #self.bn.disabled=True
        
        self.ins=Button(text='usa la imagen de arriva',size_hint_y=.17,background_color=[255,0,255])#,disabled=True)#\n'
        self.ins2=Button(text='la puedes ampliar,rotar,mover...',size_hint_y=.17,background_color=[255,0,255])#,disabled=True)
        self.ins3=Button(text='presiona salir del zoom para regresar',size_hint_y=.17,background_color=[255,0,255])#,disabled=True)
        ins=self.ins
        #self.c8p.add_widget(self.ins)
        dfigu=FigureCanvasKivy(mpl.gcf())
        self.fla=ScatterLayout(size_hint_y=.8,pos_hint={'top':1},auto_bring_to_front=False)
        fla=self.fla
        sc=Scatter()
        self.bu8700=Button(text='salir del zoom',background_color=(255,0,0),size_hint_y=.49)
        bu8700=self.bu8700
        bu8700.bind(on_press=self.uitar)
        
        fla.add_widget(dfigu)
        self.ghi=BoxLayout(orientation='vertical',size_hint_y=.2)
        
        self.ghi.add_widget(ins)
        self.ghi.add_widget(self.ins2)
        self.ghi.add_widget(self.ins3)
        self.ghi.add_widget(bu8700)
        self.add_widget(fla)        
        self.add_widget(self.ghi)


    def uitar(self,*args):
        self.bn.disabled=False
        self.br2.disabled=False
        self.bzo.disabled=False
        self.bgu.disabled=False
        self.remove_widget(self.fla)
        self.remove_widget(self.ghi)
        
        
        #self.bn.disabled=False
    
    def tito_y_su_burrito(self,*args):
        #self.f5.remove_widget(self.bzo)
        #self.f5.remove_widget(self.bgu)
        #self.c1.size_hint_y=.6
        #self.b.add_widget(self.f5)
        self.listaxy.clear()
        self.listax.clear()
        self.listax2.clear()
        self.lista_cd.clear()
        self.lista_cd3.clear()
        self.lista_cdnodo.clear()
        self.lista_cds.clear()
        self.lista_cdnodo3.clear()
        self.lista_cds3.clear()
        self.listay.clear()
        self.listaf44.clear()
        self.ffa.clear()
        self.listay2.clear()
        
        self.fig1= mpl.figure()
        self.fig1,self.ax=mpl.subplots()
        self.ax.plot(self.listax,self.listay,'x')
        try:
            self.b.add_widget(self.f5)
            self.b.remove_widget(self.f5)
            self.b.remove_widget(self.c1)
            self.b.remove_widget(self.c2)
            self.b.remove_widget(self.c8p)
            self.b.add_widget(self.c1)
            self.b.add_widget(self.f5)
            self.b.add_widget(self.c2)
            self.b.add_widget(self.c8p)
        except:
            pass
        mpl.title('Agregando Ciudades',fontsize=18,color='orange')
        self.ax.grid()
        self.c1.remove_widget(self.l2)
        self.c1.remove_widget(self.box1)
        self.l2=FigureCanvasKivy(self.fig1)
        self.c1.add_widget(self.l2)
        self.contador2=0
        self.bn2.disabled=False
        self.br2.disabled=True
        
        mpl.close()
        

    def callback311(self,*args):

        print('The button callbac3' )
        if self.bvb33==False:
            self.btn11.background_color=[0,255,0]
            self.btn11.color='white'
            self.bvb33=True
        else:
            self.btn11.background_color='green'
            
            self.btn11.color='white'
            self.bvb33=False
            
    def callback322(self,*args):
        print('The button callbac3' )
        if self.bvb333==False:
            self.btn22.background_color=[0,255,0]
            self.btn22.color='white'
            self.bvb333=True
        else:
            self.btn22.background_color='green'
            
            self.btn22.color='white'
            self.bvb333=False

    def resize2(self,*args):
        mpl.autoscale(enable=True)
        self.l2.draw()

                
    def onpr(self,*args):
        self.contador2 +=1
        g=0
        
        listax=self.listax

        

        if (len(listax)>0 ):
            self.br.disabled=False
            print('bienvenido_programador')

        if (self.t1.text=='' or self.t2.text==''):
            print('bienvenido_programador')

        
            
        else:
            
            f33='ciudad'+str(self.contador2)
            
            xi=float(str(self.t1.text))
            
            yi=float(str(self.t2.text))
            f34=nodo(xi,yi)
                
            self.ax.text(xi,yi,f33,color='b',fontsize=12)
            self.ffa.append(f33)
            self.listaxy.append(self.ffa)
            self.listay.append(f34.y)
            self.listay2.append(f34.y)
            self.listax.append(f34.x)
            self.listax2.append(f34.x)
        
            
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
                                on_release: root.save(filechooser.path)
                '''))
            
            
            try:
                self.c1.remove_widget(self.box1)
            except:
                pass
            self.box1=BoxLayout(size_hint_y=.1)
            box1=self.box1
            mpl.title('Ciudades/Nodos',fontsize=18,color='green')
            self.ax.plot(xi,yi,'x')
            mpl.border_color=[0,1,1,1]
            try:
                self.l2.draw()
            
            except:
                self.c1.remove_widget(self.l2)
                self.l2=FigureCanvasKivy(self.fig1)
                self.c1.add_widget(self.l2)
                pass
            
            
            self.tol=NavigationToolbar2(self.l2)
            tol=self.tol
            for text, tooltip_text, image_file, callback in tol.toolitems:
                if text is None:
                    #actionview.add_widget(ActionSeparator())
                    continue
                #fname = os.path.join(basedir, image_file + '.png')
                if text in ['Pan', 'Zoom','Save','Subplots','Home','Forward','Back']:
                    if text == 'Subplots':
                        pass

                        action_button4 = Button(text=text)

                    if text == 'Home':
                        action_button41 = Button(text='Original',background_color=[0,255,9],color=[0,0,255])


                        action_button41.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button41)
                        #print(callback)
                    if text == 'Back':
                        action_button42 = Button(text='Atras',background_color=[0,255,9],color=[0,0,255])


                        action_button42.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button42)
                        #print(callback)

                   
                    if text == 'Forward':
                        action_button45 = Button(text='Adelante',background_color=[0,255,9],color=[0,0,255])


                        action_button45.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button45)
                        #print(callback)
                    if text == 'Pan':
                        action_button46 = Button(text='mover',background_color=[0,255,9],color=[0,0,255])


                        
                        action_button46.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button46)
                        #print(callback)

                   

                    if text == 'Zoom':
                        self.btn22 = Button(text='Zoom',background_color=[0,255,0],color=[0,0,255])
                
                        self.btn22.bind(on_press=self.callback322)
                        self.btn22.bind(on_press=getattr(tol, callback))
                        self.box1.add_widget(self.btn22)
                        
                    if text == 'Save':
                        self.acn33 = Button(text='Guardar',background_color=[0,255,9],color=[0,0,255])
                
                        self.acn33.bind(on_press=self.guardar12)
                        self.box1.add_widget(self.acn33)
                        


                else:
                    action_button = text
                    action_button = Button(text=text)


                    try:
                        action_button.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button)
                        
                    except:
                        pass
            
            
           
            self.c1.add_widget(self.box1)
            mpl.close()
            self.t1.text=''
            self.t2.text=''
            self.br2.disabled=False

class p2(Screen):#p2
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lkx=[]
        self.lkx=lkx
        self.listaxy=[]
        self.listax=[]
        self.listax2=[]
        self.lista_cd=[]
        self.lista_cd3=[]
        self.lista_cdnodo=[]
        self.lista_cds=[]
        self.lista_cdnodo3=[]
        self.lista_cds3=[]
        self.listay=[]
        self.listaf44=[]
        self.ffa=[]
        self.listay2=[]
        
        self.lky=[]
        self.bvb3=True
        self.fig3= mpl.figure()
        self.fig3,self.ax2=mpl.subplots()
        self.fig3.suptitle('Agregando Ciudades',fontsize=18)

        self.ax2.plot(lkx,self.lky,'o')
        self.ax2.grid()
        self.b=BoxLayout(orientation='vertical')
        self.bn=Button(text='Crear',background_color=[0,255,0],color=[0,0,255])
        bn=self.bn
        self.bnuu=Button(text='Resolver',background_color=[255,0,0],disabled=True)
        bnuu=self.bnuu
        bnuu.bind(on_press=self.sd5)
        self.bn7=Button(text='Limpiar',background_color=[0,255,0],disabled=True,color=[0,0,255])
        bn7=self.bn7
        bn.bind(on_press=self.imprimir)
        self.bn2=Button(text='Pantalla principal',background_color=[0,255,0],color=[0,0,255])
        bn2=self.bn2
        bn2.bind(on_press=self.cambiar)
        l1=Label(text=' Ingresa\n' ' numero\n' ' de Ciudades:',color='#00FFFF')
        self.fgg=TextInput(hint_text='  aqui \n'
                           '# de ciudades',input_filter='int',multiline=False)
        l2=Label(text='visitas la pantalla 3')
        self.bb1=BoxLayout(orientation='horizontal',size_hint_y=.1)
        self.bb2=BoxLayout(orientation='horizontal')
        self.bb=BoxLayout(orientation='vertical',size_hint_y=.5)
        self.g54=FigureCanvasKivy(self.fig3)
        self.bb.add_widget(self.g54)
        mpl.close()
        self.fdd=Button(text=' En la casilla en blanco ingresa\n'
                        ' el numero de ciudades/nodos ,\n'
                   ' presiona el boton crear  y espera que cambie de color\n'
                   ' ahora presiona resolver y\n' ' espera que cambie de color\n'
                    ' presiona limpiar para volver a empezar',background_color=[1,0,1,1],color='white')
        fdd=self.fdd
        self.bb1.add_widget(l1)
        self.bb1.add_widget(self.fgg)
        self.bb1.add_widget(bn)
        bn7.bind(on_press=self.ni4)

        
        self.bb2.add_widget(bn2)
        
        self.bb2.add_widget(bnuu)
        self.bb2.add_widget(bn7)
        self.gg2u=BoxLayout(size_hint_y=.15)
        self.gg2u.add_widget(self.bb2)
        self.ftdd=BoxLayout(size_hint_y=.15)
        self.ftdd.add_widget(fdd)
    
        
        
        self.b.add_widget(self.bb)
        self.b.add_widget(self.ftdd)
        self.b.add_widget(self.bb1)
        self.b.add_widget(self.gg2u)
        
        
        
        self.add_widget(self.b)

    def imprimir(self,*args):
        gio=random.randint(0,1)
        es=random.randint(0,1)
        un_genio=random.randint(0,1)
        self.bn.background_color=[gio,es,un_genio]
        
        g=0
        
        if (self.fgg.text=='' or self.fgg.text==0):
            print('bienvenido_programador')

        

        if (self.fgg.text !='' ):
            g=int(str(self.fgg.text))
            print('bienvenido_programador')

        if (g>1):
            self.bnuu.disabled=False
            self.fig3= mpl.figure()
            self.fig3,self.ax2=mpl.subplots()
    

            lkx=self.lkx
            self.listaxy=[]
            self.listax=[]
            self.listax2=[]
            self.lista_cd=[]
            self.lista_cd3=[]
            self.lista_cdnodo=[]
            self.lista_cds=[]
            self.lista_cdnodo3=[]
            self.lista_cds3=[]
            self.listay=[]
            self.listaf44=[]
            self.ffa=[]
            self.listay2=[]
            i224=0
            i=1
            cvcx=[91,92,90,98,37,43,22,25,28,96,47,87,60,70,30,37]
            cvcy=[198,215,174,248,80,174,254,200,148,251,59,249,215,174,130,243]
            for i in range(g):
            
                f33='ciudad'+str(i)
                fr= g*10
                xi=float(random.randint(1,fr))
                yi=float(random.randint(1,fr))
                print(f33,'se creo en',xi,yi)
                f34=nodo(xi,yi)
                self.ffa.append(f33)
                
                
                self.ax2.text(xi,yi,f33,color='b',fontsize=12)
                self.listaxy.append(self.ffa)
                self.listaf44.append(f33)
                self.listay.append(f34.y)
                self.listay2.append(f34.y)
                self.listax.append(f34.x)
                self.listax2.append(f34.x)
                i +=1


            #print('esta es la lista como la ingresast')
            #for x,y,z in zip(listax,listay,ffa):
             #   tt7=nodo(x,y)
              #  print(z,'posicion(',x,',',y,')')
            self.ax2.grid()
            self.ax2.plot(self.listax,self.listay,'x')
            self.ftdd.size_hint_y=.02
            self.ftdd.remove_widget(self.fdd)
            self.box1=BoxLayout(size_hint_y=.1)
            self.fig3.suptitle('Ciudades creadas',fontsize=18,color='blue')
            box1=self.box1
            self.bb.remove_widget(self.g54)
            self.g54=FigureCanvasKivy(self.fig3)
            self.bb.size_hint_y=.7
            self.bb.add_widget(self.g54)
            self.tol=NavigationToolbar2(self.g54)
            tol=self.tol
            for text, tooltip_text, image_file, callback in tol.toolitems:
                if text is None:
                    #actionview.add_widget(ActionSeparator())
                    continue
                #fname = os.path.join(basedir, image_file + '.png')
                if text in ['Pan', 'Zoom','Save','Subplots','Home','Forward','Back']:
                    if text == 'Subplots':
                        pass

                        action_button4 = Button(text=text)

                    if text == 'Home':
                        action_button41 = Button(text='Original',background_color=[0,255,9],color=[0,0,255])


                        action_button41.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button41)
                        #print(callback)
                    if text == 'Back':
                        action_button42 = Button(text='Atras',background_color=[0,255,9],color=[0,0,255])#,color=[0,0,255])


                        action_button42.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button42)
                        #print(callback)

                   
                    if text == 'Forward':
                        action_button45 = Button(text='Adelante',background_color=[0,255,9],color=[0,0,255])#,color=[0,0,255])


                        action_button45.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button45)
                        #print(callback)
                    if text == 'Pan':
                        action_button46 = Button(text='mover',background_color=[0,255,9],color=[0,0,255])#,color=[0,0,255])


                        action_button46.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button46)
                        #print(callback)

                   

                    if text == 'Zoom':
                        self.btn2 = Button(text='Zoom',background_color=[0,0,255])
                
                        self.btn2.bind(on_press=self.callback32)
                
                        self.btn2.bind(on_press=getattr(tol, callback))
                        self.box1.add_widget(self.btn2)
                        
                    if text == 'Save':
                        self.an3 = Button(text='Guardar',background_color=[0,255,9],color=[0,0,255])#,color=[0,0,255])
                
                        self.an3.bind(on_press=self.guardar5)
                        self.box1.add_widget(self.an3)
                        


                else:
                    action_button = text
                    action_button = Button(text=text)


                    try:
                        action_button.bind(on_press=getattr(tol, callback))
                        box1.add_widget(action_button)
                        
                    except:
                        pass
            
            

            #self.ftdd.remove_widget(self.fdd)
            
            self.bb.add_widget(self.box1)
            mpl.close()
            self.fgg.text=''
            self.bn7.disabled=False
            self.bn.disabled=True

        else:
            print('99')
            



    def ni4(self,*args):
        gio=0
        es=255
        un_genio=0
        
        self.bn.background_color=[0,255,0]
        #self.bb.remove_widget(self.box1)
        #self.ftdd.remove_widget(self.bgu5)
        mpl.close()
        self.ftdd.size_hint_y=.17
        self.ftdd.add_widget(self.fdd)
        self.listax.clear()
        self.listay.clear()
        
        self.listaxy.clear()
        self.listax.clear()
        self.listax2.clear()
        self.lista_cd.clear()
        self.lista_cd3.clear()
        self.lista_cdnodo.clear()
        self.lista_cds.clear()
        self.lista_cdnodo3.clear()
        self.lista_cds3.clear()
        self.listay.clear()
        self.listaf44.clear()
        self.ffa.clear()
        self.listay2.clear()
        self.fig3= mpl.figure()
        self.fig3,self.ax2=mpl.subplots()
        self.ax2.plot(self.listax,self.listay,'x')
        self.ax2.grid()
        mpl.title('Agregando Ciudades',fontsize=18,color='purple')
        
        
        
        
        
        
        self.bb.remove_widget(self.g54)
        self.bb.remove_widget(self.box1)#
        self.g54=FigureCanvasKivy(self.fig3)
        
        
       # self.bb
        self.bb.add_widget(self.g54)
        self.bn.disabled=False
        self.bnuu.disabled=True
        self.bn7.disabled=True
        
        mpl.close()


    def sd5(self,*args):
        
        
        gio=random.randint(0,1)
        es=random.randint(0,1)
        un_genio=random.randint(0,1)
        self.bnuu.background_color=[gio,es,un_genio]
        mpl.close()
        figg1=mpl.figure()
        figg1,self.current_agx=mpl.subplots()
        
        
        listaxy=self.listaxy
        listax=self.listax
        listax2=self.listax2
        lista_cd=self.lista_cd
        lista_cd3=self.lista_cd3
        lista_cdnodo=self.lista_cdnodo
        lista_cds=self.lista_cds
        lista_cdnodo3=self.lista_cdnodo3
        lista_cds3=self.lista_cds3
        listay=self.listay
        listaf44=self.listaf44
        ffa=self.ffa
        listay2=self.listay2
        print('imprimir')

        

        for x,y,z in zip(listax,listay,ffa):
            tt7=nodo(x,y)
            grpunto(tt7)
            mpl.text(x,y,z,color='b',fontsize=22)
        ux=menor(listax)
        wx=mayor(listax)
        vy=menor(listay)
        my=mayor(listay)
        k= nodo(ux,vy)#(1,6)
        t=nodo(wx,vy)#(2,6)
        j=nodo(wx,my)
        I=nodo(ux,my)

        l1=distancia2p(k,t)
        gggg=wx+10
        ggg=ux-10
        #mpl.xlim((ggg),(gggg))
        #mpl.ylim((vy-50),(my+50))

        l2=distancia2p(t,j)

        p1=((l1/3)+ux)
        pz=(l1/20)
        p2=((2*(l1/3))+ux)
        pm=(l2/2)+vy+.23
        pm1=nodo(ux,(pm))
        pm2=nodo(wx,(pm))

        p11=nodo((p1),vy)
        p12=nodo((p1),my)
        p21=nodo((p2),vy)

        p22=nodo((p2),my)

        #global
        
        def empezar(cd3):
            cd3=nodo(cd3.x,cd3.y)
            wqqq=cd3.id
            for x,y,z in zip(listax,listay,ffa):
                if cd3.x==x and cd3.y==y:
                    global prin
                    global prin2
                    prin=str('ubica el nodo '+str(z)+' esta en ('+str(x)+','+str(y)+')')

            global nuevo_nodo
            nuevo_nodo=cd3
                    
            
            """lq=[]
            lgq=[]
            ff=0
            gfd=[]
            gfds=[]
            po=[]
            po2=[]
            for xo,yo in zip(listax,listay):
                if xo==cd3.x:
                    if yo<pm and yo>cd3.y:
                        ui=nodo(xo,yo)
                        gfd.append(ui)
                        sa=distancia2p(cd3,ui)
                        gfds.append(sa)
                if xo<cd3.x and yo<pm:
                    v6677= nodo(xo,yo)
                    lq.append(v6677)
                    geo6677=distancia(cd3,v6677)
                    lgq.append(geo6677)            
                ff +=1
                
            try:        
                nb19=menor(gfds)
                lk=0
                for x8o in gfds:
                    if x8o==nb19:
                        uut22=gfd[lk]
                        for xmn,ymn,zmn in zip(listax,listay,ffa):
                            if cd3.x==xmn and cd3.y==ymn:
                                for xu,yu,u2 in zip(listax,listay,ffa):
                                    if uut22.x==xu and uut22.y==yu:
                                        parp=u2
                                gio2=distancia2p(cd3,uut22)
                                #print(z,'->',parp,'distancia=',gio2)
                                lista_cd.append(zmn)
                                lista_cds.append(parp)
                                lista_cdnodo.append(gio2)

                                
                        nuevo_nodo=uut22
                        grrecta(cd3,uut22)
                        mostrar(cd3,uut22)
                        

                    lk+=1
                            
            except:
                try:
                    men46=menor(lgq)            
                    j5=0
                    for x,y in zip(lgq,lq):
                        if x==men46:
                            po.append(y)
                            fff33=distancia2p(cd3,y)
                            po2.append(fff33)

                    zzz2=menor(po2)
                    contador22=0
                    for x,y in zip(po,po2):
                            if zzz2==y:
                                contador22+=1
                                if contador22==1:
                                    n558=(x)
                                    for x,y,z in zip(listax,listay,ffa):
                                        if cd3.x==x and cd3.y==y:
                                            for x,y,u in zip(listax,listay,ffa):
                                                if n558.x==x and n558.y==y:
                                                    parp2=u
                                            gio3=distancia2p(cd3,n558)
                                            #print(z,'->',parp,'distancia=',gio3)
                                            lista_cd.append(z)
                                            lista_cds.append(parp2)
                                            lista_cdnodo.append(gio3)
                                    nuevo_nodo=n558
                                    #print('la ciudad es',nuevo_nodo)
                                    grrecta(cd3,n558)
                                    mostrar(cd3,n558)
                        
                except:
                    nuevo_nodo=cd3"""


        def avanzarg(cd4):
            global nuevo_nodo
            
               
            cd4=nodo(cd4.x,cd4.y)
            d1=0
            lq1=[]
            lq2=[]
            lq3=[]
            lq4=[]
            lq5=[]
            lq6=[]
            gj=[]
            jj=[]
            ff=0
            
            for y,x in zip(listay,listax):
                if y<pm:
                    if x==cd4.x :                
                        if y<cd4.y and y<pm:
                            v77= nodo(x,y)
                            lq1.append(v77)
                            geo=distancia2p(cd4,v77)
                            lq2.append(geo)            
                        if y>cd4.y and y<pm:
                            v25= nodo(x,y)
                            lq3.append(v25)
                            geo2=distancia2p(cd4,v25)
                            lq4.append(geo2)
                                            
                    if x<cd4.x and y<pm:
                        v555= nodo(x,y)
                        lq5.append(v555)
                        geo3333=distancia(cd4,v555)
                        lq6.append(geo3333)            
                
            #aqui hay un error de codigo
            try:
                ce=menor(lq2)
                lk=0
                for cr in lq2:
                    if cr==ce:
                        uut=lq1[lk]
                        for x,y,z in zip(listax,listay,ffa):
                            if cd4.x==x and cd4.y==y:
                                for x99,y99,u99 in zip(listax,listay,ffa):
                                    if uut.x==x99 and uut.y==y99:
                                        parp3=u99
                                        
                                gio4=distancia2p(cd4,uut)
                                #print(z,'->',parp3,'distancia=',gio4)
                                lista_cd.append(z)
                                lista_cds.append(parp3)
                                lista_cdnodo.append(gio4)       
                        
                        nuevo_nodo=uut

                        #print('el nuevo nodo es',nuevo_nodo)
                        grrecta(cd4,uut)
                        mostrar(cd4,uut)
                        h=0
                        for w,q,z in zip(listax,listay,ffa):
                            if cd4.x==w and cd4.y==q:
                                ffa.pop(h)
                                listax.pop(h)
                                listay.pop(h)
                            h +=1
                                       
                    lk+=1
                            
            except:
                try:            
                    men=menor(lq4)
                    j5=0
                    for x in lq4:                
                        if x==men:
                            tw=lq3[j5]
                            for x,y,z in zip(listax,listay,ffa):
                                if cd4.x==x and cd4.y==y:
                                    for x,y,u in zip(listax,listay,ffa):
                                        if tw.x==x and tw.y==y:
                                            parp4=u
                                    gio5=distancia2p(cd4,tw)
                                    #print(z,'->',parp4,'distancia=',gio5)
                                    lista_cd.append(z)
                                    lista_cds.append(parp4)
                                    lista_cdnodo.append(gio5)  
                            nuevo_nodo=tw
                            #print('el nuevo nodo es',nuevo_nodo)
                            grrecta(cd4,tw)
                            mostrar(cd4,tw)
                            hr=0
                            for w,q,mm in zip(listax,listay,ffa):
                                if cd4.x==w and cd4.y==q:
                                    listax.pop(hr)
                                    ffa.pop(hr)
                                    listay.pop(hr)
                                hr +=1
                                              
                        j5+=1
                        
                except:
                    try:
                        
                        
                        mn=menor(lq6)
                        for x,y in zip(lq6,lq5):                    
                            if x==mn:
                                gj.append(y)
                                fff=distancia2p(cd4,y)
                                jj.append(fff)

                        zzz=menor(jj)
                        contador=0
                        for x,y in zip(gj,jj):
                            if zzz==y:
                                contador+=1
                                if contador==1:
                                    n55=(x)
                                    for x,y,z in zip(listax,listay,ffa):
                                        if cd4.x==x and cd4.y==y:
                                            for x,y,u in zip(listax,listay,ffa):
                                                if n55.x==x and n55.y==y:
                                                    parp5=u
                                            gio6=distancia2p(cd4,n55)
                                            #print(z,'->',parp5,'distancia=',gio6)
                                            lista_cd.append(z)
                                            lista_cds.append(parp5)
                                            lista_cdnodo.append(gio6)
                                    nuevo_nodo=n55
                                    #print('la ciudad es',nuevo_nodo)
                                    grrecta(cd4,n55)
                                    mostrar(cd4,n55)
                                    hry=0
                                    for w,q,nbaaa in zip(listax,listay,ffa):
                                        if cd4.x==w and cd4.y==q:
                                            listax.pop(hry)
                                            ffa.pop(hry)
                                            listay.pop(hry)
                                        hry +=1

                                    
                                                 
                            
                    except:
                        print('geovanni')

            
        def avanzar2(cd):
            global nuevo_nodo
               
            cd=nodo(cd.x,cd.y)
            d1=0
            lq12=[]
            lq22=[]
            lq32=[]
            lq42=[]
            lq52=[]
            lq62=[]
            ff=0    
            
            for y,x in zip(listay,listax):
                if y>=pm:
                    if x==cd.x and y>=pm:            
                        if y>(cd.y) and y<=my:
                            v= nodo(x,y)
                            lq12.append(v)
                            geo=distancia2p(cd,v)
                            lq22.append(geo)                    
                        if y<(cd.y) and y>=(pm):
                            v2= nodo(x,y)
                            lq32.append(v2)
                            geo2=distancia2p(cd,v2)
                            lq42.append(geo2)
                                        
                    if x>cd.x and y>=pm :
                        v66= nodo(x,y)
                        lq52.append(v66)
                        geo66=distancia(cd,v66)
                        lq62.append(geo66)                                    
                ff +=1

            try:
                nb66=menor(lq22)
                lk=0
                for x in lq22:            
                    if x==nb66:
                        uut44=lq12[lk]
                        for x,y,z in zip(listax,listay,ffa):
                            if cd.x==x and cd.y==y:
                                for x,y,u in zip(listax,listay,ffa):
                                    if uut44.x==x and uut44.y==y:
                                        parp6=u
                                gio7=distancia2p(cd,uut44)
                                #print(z,'->',parp6,'distancia=',gio7)
                                lista_cd3.append(z)
                                lista_cds3.append(parp6)
                                lista_cdnodo3.append(gio7)
                        
                        nuevo_nodo=uut44
                        #print('la ciudad  es',nuevo_nodo)
                        grrecta(cd,uut44)
                        mostrar(cd,uut44)
                        hr2=0
                        for w,q,mn in zip(listax,listay,ffa):
                            if cd.x==w and cd.y==q:
                                listax.pop(hr2)
                                ffa.pop(hr2)
                                listay.pop(hr2)
                            hr2 +=1
                        
                    lk+=1
                            
            except:
                try:
                    men55=menor(lq42)
                    j5=0
                    for x in lq42:                
                        if x==men55:                    
                            tw44=lq32[j5]
                            for x,y,z in zip(listax,listay,ffa):
                                if cd.x==x and cd.y==y:
                                    for x,y,u in zip(listax,listay,ffa):
                                        if tw44.x==x and tw44.y==y:
                                            parp7=u
                                    gio8=distancia2p(cd,tw44)
                                    #print(z,'->',parp7,'distancia=',gio8)
                                    lista_cd3.append(z)
                                    lista_cds3.append(parp7)
                                    lista_cdnodo3.append(gio8)
                            nuevo_nodo=tw44
                            #print('el nuevo nodo es',nuevo_nodo)
                            grrecta(cd,tw44)
                            mostrar(cd,tw44)
                            hr3=0
                            for w,q,nnm in zip(listax,listay,ffa):
                                if cd.x==w and cd.y==q:
                                    listax.pop(hr3)
                                    ffa.pop(hr3)
                                    listay.pop(hr3)
                                hr3 +=1
                            
                        j5+=1

                except:
                    try:
                        gj=0
                        mn33=menor(lq62)
                        qq=[]
                        ww=[]
                        for x,y in zip(lq62,lq52):                    
                            if x==mn33:
                                qq.append(y)
                                ss=distancia2p(cd,y)
                                ww.append(ss)


                        dd=menor(ww)
                        con=0
                        for x,y in zip(ww,qq):
                            if x== dd:
                                if con==0:
                                    n552=y
                                    for x,y,z in zip(listax,listay,ffa):
                                        if cd.x==x and cd.y==y:
                                            for x,y,u in zip(listax,listay,ffa):
                                                if n552.x==x and n552.y==y:
                                                    parp8=u
                                            gio9=distancia2p(cd,n552)
                                            #print(z,'->',parp8,'distancia=',gio9)
                                            lista_cd3.append(z)
                                            lista_cds3.append(parp8)
                                            lista_cdnodo3.append(gio9)
                                    nuevo_nodo=n552
                                    #print('el nuevo nodo es',nuevo_nodo)
                                    grrecta(cd,n552)
                                    mostrar(cd,n552)
                                    hr4=0
                                    for w,q,sq in zip(listax,listay,ffa):
                                        if cd.x==w and cd.y==q:
                                            listax.pop(hr4)
                                            ffa.pop(hr4)
                                            listay.pop(hr4)
                                        hr4 +=1
                                    con+=1
                                                   
                            gj +=1
                            
                    except:
                        print('burgos')
                        
        def dentro_funcion(fs,funcion):
            global nuevo_nodo
            r=funcion(fs)
            return r

        uo=0
        uo1=0
        l88=[]
        l99=[]
        lista_arrivax=[]
        lista_arrivay=[]
        lista_abajox=[]
        lista_abajoy=[]
        lista_2p=[]
        lista_nodo=[]
        lista_2p2=[]
        lista_nodo2=[]
        llll=[]
        llll2=[]
        llll3=[]

        for y in listay2:
            x=listax2[uo]
            if y>=pm:
                lista_arrivay.append(y)
                lista_arrivax.append(x)
            uo+=1

        for y in listay2:
            x=listax2[uo1]
            if y<pm:
                lista_abajoy.append(y)
                lista_abajox.append(x)
            uo1+=1

        q1=menor(lista_arrivax)

        q3=menor(lista_abajox)
        q2=mayor(lista_abajox)
        q4=mayor(lista_arrivax)
        ao=0
        kfc=[]
        kf2=[]
        kf3=[]
        kf4=[]
        kf5=[]

        ppo=[]
        ppo1=[]
        ppo2=[]
        ppo3=[]
        uppo=[]
        uppo1=[]
        uppo2=[]
        uppo3=[]
        
        for x,y in zip(lista_arrivax,lista_arrivay):
            if x==q1:
                kfc.append(y)
                ao+=1

                
        if ao==1:
            for x,y in zip(lista_arrivax,lista_arrivay):
                if x==q1:
                    gt2=nodo(x,y)

        kfc3=mayor(kfc)            
        if ao>1:
            for x,y in zip(lista_arrivax,lista_arrivay):
                if x==q1 and y==kfc3:
                    gt2=nodo(x,y)
                    
            
                    
        a=0
        
        for x,y in zip(lista_abajox,lista_abajoy):
            if x==q3:
                kf2.append(y)
                a+=1

        if a==1:
            for x,y in zip(lista_abajox,lista_abajoy):
                if x==q3:
                    gf=nodo(x,y)
                    
        k45=menor(kf2)            
        if a>1:
            for x,y in zip(lista_abajox,lista_abajoy):
                if x==q3 and y==k45:
                    gf=nodo(x,y)            
         


        aob=0
        
        for x,y in zip(lista_abajox,lista_abajoy):
            if x==q2:
                kf3.append(y)
                aob+=1

        if aob==1:
            for x,y in zip(lista_abajox,lista_abajoy):
                if x==q2:
                    gar=nodo(x,y)
                    
        dffa=menor(kf3)
        if aob>1:
            for x,y in zip(lista_abajox,lista_abajoy):
                if x==q2 and y==dffa:
                    gar=nodo(x,y)
            

                    
        ab=0
        
        for x,y in zip(lista_arrivax,lista_arrivay):
            if x==q4:
                kf4.append(y)
                ab+=1
                
        if ab==1:   
            for xm,ym in zip(lista_arrivax,lista_arrivay):
                if xm==q4:
                    gar2=nodo(xm,ym)
                    

        asqd=mayor(kf4)
        if ab>1:
            for xpp,ypp in zip(lista_arrivax,lista_arrivay):
                if xpp==q4 and ypp==asqd:
                    gar2=nodo(xpp,ypp)

        el_ojo_ke_todo_LOVE=dispr(gar2,gf,gt2)
        gracias_gracias_gracias=dispr(gt2,gar2,gar)
        if gracias_gracias_gracias <=0 and gt2.x<gar2.x and gt2.x>gar.x:
            gt2=gar2
            
        if el_ojo_ke_todo_LOVE <=0 and gar2.x<gf.x and gar2.x>gt2.x:
            gar2=gt2

        

        for x,y in zip(listax,listay):
            if (x>=gar.x and x<=gar2.x) or (x<=gar.x and x>=gar2.x):
                if (y>gar.y and y<gar2.y) :
                    ppp4=nodo(x,y)
                    rww4= dispr(ppp4,gar,gar2)
                    
                
                    
                    if rww4>=0:
                        #print('el nodo agregado es',ppp4)
                        wwee4=distancia2p(gar2,ppp4)
                        lista_nodo2.append(ppp4)
                        lista_2p2.append(wwee4)



        zzzz=len(lista_nodo2)
        if zzzz==0:
            for xu,yu,zu in zip(listax,listay,ffa):
                if gar.x==x and gar.y==y:
                    for x334,y66,uhj in zip(listax,listay,ffa):
                        if gar2.x==x334 and gar2.y==y66:
                            par77k=uhj
                            gi8=distancia2p(gar,gar2)
                    #print(z,'->',par7,'distancia=',gi8)
                            ppo.append(par77k)
                            ppo1.append(zu)
                            ppo2.append(gi8)
            grrecta(gar,gar2)
            mostrar(gar,gar2)

        if zzzz==1:
            for xk in lista_nodo2:
                grrecta(gar2,xk)
                mostrar(gar2,xk)
                grrecta(xk,gar)
                mostrar(xk,gar)

                kkwq4=0       
                for x22,y33,f88 in zip(listax,listay,ffa):
                    if x22==xk.x and y33==xk.y:
                        ppo1.append(f88)
                        listax.pop(kkwq4)
                        listay.pop(kkwq4)
                        ffa.pop(kkwq4)                        
                    kkwq4+=1
                        
                    if x22==gar.x and y33==gar.y:
                        ppo.append(f88)
                        g90=distancia2p(xk,gar)
                        ppo2.append(g90)
                
                for x21,y31,f81 in zip(listax,listay,ffa):
                    if x21==gar2.x and y31==gar2.y:
                        ppo.append(f81)
                        gi86=distancia2p(gar2,xk)
                        ppo2.append(gi86)
                

        else:
            while len(lista_nodo2)>1:        
                ccxx4=menor(lista_2p2)
                vbb4=0
                for xt,yt in zip(lista_nodo2,lista_2p2):
                    if yt==ccxx4:
                        coi4=0
                        for x4,y4,z34h in zip(listax,listay,ffa):
                            if xt.x==x4 and xt.y==y4:
                                grrecta(gar2,xt)
                                mostrar(gar2,xt)
                                ppo1.append(z34h)
                                for x6j,y6j,uj in zip(listax,listay,ffa):
                                    if gar2.x==x6j and gar2.y==y6j:                                
                                        ppo.append(uj)
                                        ppo2.append(yt)
                                gar2=xt
                                listax.pop(coi4)
                                listay.pop(coi4)
                                ffa.pop(coi4)
                            coi4+=1

                        lista_nodo2.pop(vbb4)
                        lista_2p2.pop(vbb4)
                    
                    vbb4+=1
                len(lista_nodo2)

                if len(lista_nodo2)==1:
                    for x in lista_nodo2:
                        grrecta(gar2,x)
                        mostrar(gar2,x)
                        grrecta(x,gar)
                        mostrar(x,gar)
                        kwq4=0
                        for x21,y31,f81 in zip(listax,listay,ffa):
                            if x21==gar2.x and y31==gar2.y:
                                ppo.append(f81)
                                gi86=distancia2p(gar2,x)
                                ppo2.append(gi86)
                                
                        for x22,y33,f88 in zip(listax,listay,ffa):
                            if x22==x.x and y33==x.y:
                                ppo1.append(f88)
                                listax.pop(kwq4)
                                listay.pop(kwq4)
                                ffa.pop(kwq4)                        
                            kwq4+=1
                                
                            if x22==gar.x and y33==gar.y:
                                ppo.append(f88)
                                g90=distancia2p(x,gar)
                                ppo2.append(g90)        
            
        for x,y in zip(listax,listay):
            if (x>=gf.x and x<=gt2.x) or (x<=gf.x and x>=gt2.x):
                if (y>gf.y and y<gt2.y) :
                    ppp22=nodo(x,y)
                    rww= dispr(ppp22,gt2,gf)

                    
                    if rww>=0:
                        
                        wwee1=distancia2p(gf,ppp22)
                        lista_nodo.append(ppp22)
                        lista_2p.append(wwee1)

                    if rww<0 and ppp22.y<pm and ppp22.x==gf.x and ppp22.y != gf.y:
                        
                        wwee11=distancia2p(gf,ppp22)
                        lista_nodo.append(ppp22)
                        lista_2p.append(wwee11)

        if len(lista_nodo)==0:
            for xh,yh,zh in zip(listax,listay,ffa):
                if gf.x==xh and gf.y==yh:
                    uppo.append(zh)
                    for xd,ydf,uq in zip(listax,listay,ffa):
                        if gt2.x==xd and gt2.y==ydf:
                            par6767=uq
                            uppo1.append(par6767)
                    gip8=distancia2p(gf,gt2)
                    #print(z,'->',par7,'distancia=',gi8)            
                    uppo2.append(gip8)
            grrecta(gf,gt2)
            mostrar(gf,gt2)


        if len(lista_nodo)==1:
            
            for xkw in lista_nodo:
                grrecta(gt2,xkw)
                mostrar(gt2,xkw)
                grrecta(xkw,gf)
                mostrar(xkw,gf)

                k4=0       
                for x2211,y3311,f88h in zip(listax,listay,ffa):
                    if x2211==xkw.x and y3311==xkw.y:
                        uppo1.append(f88h)
                        listax.pop(k4)
                        listay.pop(k4)
                        ffa.pop(k4)                        
                    k4+=1
                        
                    if x2211==gf.x and y3311==gf.y:
                        uppo.append(f88h)
                        g900=distancia2p(xkw,gf)
                        uppo2.append(g900)
                
                for x2111,y3111,f8111 in zip(listax,listay,ffa):
                    if x2111==gt2.x and y3111==gt2.y:
                        uppo.append(f8111)
                        gi8611=distancia2p(gt2,xkw)
                        uppo2.append(gi8611)
        else:
            while len(lista_nodo)>1:        
                ccxx=menor(lista_2p)
                v4=0
                for xt5,yt5 in zip(lista_nodo,lista_2p):
                    if yt5==ccxx:
                        ci4=0
                        for x45,y45,z45 in zip(listax,listay,ffa):
                            if xt5.x==x45 and xt5.y==y45:
                                grrecta(gf,xt5)
                                mostrar(gf,xt5)
                                uppo1.append(z45)
                                for x6j,y6j,uj in zip(listax,listay,ffa):
                                    if gf.x==x6j and gf.y==y6j:                                
                                        uppo.append(uj)
                                        uppo2.append(yt5)
                                gf=xt5
                                listax.pop(ci4)
                                listay.pop(ci4)
                                ffa.pop(ci4)
                            ci4+=1

                        lista_nodo.pop(v4)
                        lista_2p.pop(v4)
                    
                    v4+=1
                len(lista_nodo)

                if len(lista_nodo)==1:
                    for x in lista_nodo:
                        grrecta(gt2,x)
                        mostrar(gt2,x)
                        grrecta(x,gf)
                        mostrar(x,gf)
                        kwq4=0
                        for x21,y31,f81 in zip(listax,listay,ffa):
                            if x21==gt2.x and y31==gt2.y:
                                uppo.append(f81)
                                gi86=distancia2p(gt2,x)
                                uppo2.append(gi86)
                                
                        for x22,y33,f88 in zip(listax,listay,ffa):
                            if x22==x.x and y33==x.y:
                                uppo1.append(f88)
                                listax.pop(kwq4)
                                listay.pop(kwq4)
                                ffa.pop(kwq4)                        
                            kwq4+=1
                                
                            if x22==gf.x and y33==gf.y:
                                uppo.append(f88)
                                g90=distancia2p(x,gf)
                                uppo2.append(g90) 

                
        global nuevo_nodo               
        empezar(gar)
        for y in lista_abajox:
            try:            
                dentro_funcion(nuevo_nodo,avanzarg)
                            
            except:
                print('tu solo confia en mi')




        nuevo_nodo=gt2



        for y in lista_arrivax:
            try:
                dentro_funcion(nuevo_nodo,avanzar2)

            except:
                print('gracias,gracias,gracias')
        print('********************************************************')
        print('********************************************************')
        print ('te devuelvo la lista en orden con sus distancia reales')
        print(prin)
        print('lo usaremos como punto de partida y punto final')

        for x,y,z in zip(uppo,uppo1,uppo2):
            lista_cd.append(x)
            lista_cds.append(y)
            lista_cdnodo.append(z)

            
        for x,y,z in zip(lista_cd3,lista_cds3,lista_cdnodo3):
            lista_cd.append(x)
            lista_cds.append(y)
            lista_cdnodo.append(z)
            


            
        for x,y,z in zip(ppo,ppo1,ppo2):
            lista_cd.append(x)
            lista_cds.append(y)
            lista_cdnodo.append(z)
        a=0
        ay=[]
        print('esta es la lista ordenada:')
        for x,y in zip(lista_cd,lista_cds):
            print(x)

            
        print(lista_cds[-1])
        print('nuevamente->',lista_cd[0])
        print('*********************************************************')
        print('esta es la lista ordenada con distancias:')


        for x,y,z in zip(lista_cd,lista_cds,lista_cdnodo):
            print('(',x,'->',y,')','distancia=',z)

        
        
        mpl.title('Camino Hamiltoniano resuelto',color='orange',fontsize=18)
        mpl.xlabel('Eje X',color='orange')
        mpl.ylabel('Eje Y',color='orange')
        
        
        self.bb.remove_widget(self.box1)
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
                            on_release: root.save(filechooser.path)
            '''))
        mpl.title('Camino Hamiltoniano resuelto',fontsize=18)
        mpl.grid()
        self.box1=BoxLayout(size_hint_y=.1,orientation='horizontal')
        box1=self.box1#self.b.remove_widget(self.fdd)
        self.bb.remove_widget(self.g54)
        self.g54=FigureCanvasKivy(mpl.gcf())
        self.bb.size_hint_y=.7
        self.tol=NavigationToolbar2(self.g54)
        tol=self.tol
        for text, tooltip_text, image_file, callback in tol.toolitems:
            if text is None:
                    #actionview.add_widget(ActionSeparator())
                continue
                #fname = os.path.join(basedir, image_file + '.png')
            if text in ['Pan', 'Zoom','Save','Subplots','Home','Forward','Back']:
                if text == 'Subplots':
                    pass

                    action_button4 = Button(text=text)

                if text == 'Home':
                    action_button41 = Button(text='Original',background_color=[0,255,9],color=[0,0,255])


                    action_button41.bind(on_press=getattr(tol, callback))
                    box1.add_widget(action_button41)
                        #print(callback)
                if text == 'Back':
                    action_button42 = Button(text='Atras',background_color=[0,255,9],color=[0,0,255])


                    action_button42.bind(on_press=getattr(tol, callback))
                    box1.add_widget(action_button42)
                        #print(callback)

                   
                if text == 'Forward':
                    action_button45 = Button(text='Adelante',background_color=[0,255,9],color=[0,0,255])


                    action_button45.bind(on_press=getattr(tol, callback))
                    box1.add_widget(action_button45)
                        #print(callback)
                if text == 'Pan':
                    action_button46 = Button(text='mover',background_color=[0,255,9],color=[0,0,255])


                    action_button46.bind(on_press=getattr(tol, callback))
                    box1.add_widget(action_button46)
                        #print(callback)

                   

                if text == 'Zoom':
                    self.btn1 = Button(text='Zoom',background_color=[0,0,255])
                
                    self.btn1.bind(on_press=self.callback31)
                    self.btn1.bind(on_press=getattr(tol, callback))
                    self.box1.add_widget(self.btn1)
                    
                    
                    
                if text == 'Save':
                    self.an33 = Button(text='Guardar',background_color=[0,255,9],color=[0,0,255])
                
                    self.an33.bind(on_press=self.guardar4)
                    self.box1.add_widget(self.an33)
                    


            else:
                action_button = text
                action_button = Button(text=text)


                try:
                    action_button.bind(on_press=getattr(tol, callback))
                    box1.add_widget(action_button)
                    
                except:
                    pass
            
            

        #self.ftdd.remove_widget(self.fdd)
        
        self.bb.add_widget(self.box1)
        self.bb.add_widget(self.g54)
        #self.bzo5=Button(text='zoom',background_color=[0,255,255],color=(255,0,0))
        #bzo5=self.bzo5
        #self.bgu5=Button(text='guardar imagen',background_color=[0,255,255],color=[255,0,0])
        #self.bgu5.bind(on_press=self.guardar4)
        #self.ftdd.size_hint_y=.1
        #self.ftdd.add_widget(bzo5)
        #bzo5.bind(on_press=self.zzom4)
        
        """self.listax.clear()
        self.listay.clear()
        
        self.listaxy.clear()
        self.listax.clear()
        self.listax2.clear()
        self.lista_cd.clear()
        self.lista_cd3.clear()
        self.lista_cdnodo.clear()
        self.lista_cds.clear()
        self.lista_cdnodo3.clear()
        self.lista_cds3.clear()
        self.listay.clear()
        self.listaf44.clear()
        self.ffa.clear()
        self.listay2.clear()
        
        mpl.close()"""
        self.bnuu.disabled=True

    def callback31(self,*args):

        print('The button callbac3' )
        if self.bvb3==False:
            self.btn1.background_color=[0,0,255]
            self.btn1.color='white'
            self.bvb3=True
        else:
            self.btn1.background_color=[10,100,255]
            
            self.btn1.color='blue'
            self.bvb3=False
            
    def callback32(self,*args):
        print('The button callbac3' )
        if self.bvb3==False:
            self.btn2.background_color=[0,0,255]
            self.btn2.color='white'
            self.bvb3=True
        else:
            self.btn2.background_color=[10,100,255]
            
            self.btn2.color='blue'
            self.bvb3=False


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path):
        c=random.randint(1,1000)
        
        geovani_te_ama='geo'+str(c)+'.png'
        filename=geovani_te_ama#mpl.savefig(geovani_te_ama)

        self.g54.export_to_png(os.path.join(path, filename))
        self.dismiss_popup()
        print('path',path)
        print('filename',filename)

    def sa(self, *args):
        self.show_save()

    def guardar4(self,*args):
        self.an33.background_color='green'
        self.an33.color='white'
        cy=random.randint(1,1000)
        #mpl.grid()
        mpl.draw()
        geovani_te_ama='camino_hamiltoniano'+str(cy)+'.png'
        mpl.savefig(geovani_te_ama)
        print('se guardo la imagen')
        print('geovani_te_ama',geovani_te_ama)

   
    def guardar5(self,*args):

        self.an3.background_color='green'
        self.an3.color='white'
        cy=random.randint(1,1000)
        #mpl.grid()
        #mpl.draw()
        geovani_te_ama='camino_hamiltoniano'+str(cy)+'.png'
        self.g54.export_to_png(geovani_te_ama)
        print('se guardo la imagen')
        print('geovani_te_ama',geovani_te_ama)

    def zzom4(self,*args):
        mpl.grid()
        self.bn7.disabled=True
        self.bn2.disabled=True
        self.bzo5.disabled=True
        self.bgu5.disabled=True
        #self.bn.disabled=True
        #self.gg2u.remove_widget(self.bb2)
        self.ins5=Label(text='usa la imagen pequeña de la\n'
                       'esquina inferior izquierda\n'
                       'la puedes ampliar,rotar,mover...\n'
                       'presiona salir del zoom para regresar,\n'
                       'primero debes mover la imagen para salir',center_y=True,center_x=True,color='#00FFFF')
        #self.gg2u.add_widget(self.ins5)
        self.ins11=Button(text='usa la imagen de arriva',size_hint_y=.17,background_color=[255,0,255])#,disabled=True)#\n'
        self.ins22=Button(text='la puedes ampliar,rotar,mover...',size_hint_y=.17,background_color=[255,0,255])#,disabled=True)
        self.ins33=Button(text='presiona salir del zoom para regresar',size_hint_y=.17,background_color=[255,0,255])#,disabled=True)
        
        mpl.grid()
        dfigu=FigureCanvasKivy(mpl.gcf())
        self.fla=ScatterLayout(size_hint_y=.9,pos_hint={'top':1},auto_bring_to_front=False)
        sc=Scatter()
        self.bu8700=Button(text='salir del zoom',background_color=(255,0,0),size_hint_y=.4)
        self.bu8700.bind(on_press=self.uitar5)
        self.gb=BoxLayout(size_hint_y=.2,orientation='vertical')
        self.fla.add_widget(dfigu)
        #sc.add_widget(fla)
        #self.add_widget(bu8700)
        #self.gbo.add_widget(sc)
        
        #self.b.add_widget(self.gbo)
        self.gb.add_widget(self.ins11)
        self.gb.add_widget(self.ins22)
        self.gb.add_widget(self.ins33)
        self.gb.add_widget(self.bu8700)
        self.add_widget(self.fla)
        
        self.add_widget(self.gb)


    def uitar5(self,*args):
        self.bn7.disabled=False
        self.bn2.disabled=False
        self.bzo5.disabled=False
        #self.bgu5.disabled=False
        #self.remove_widget(self.fla)
        #self.remove_widget(self.gb)
        
        #self.bn.disabled=False
    
    

        


    def cambiar(self,*args):
        self.manager.current='p11'

class app(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(p1(name='p11'))
        sm.add_widget(p2(name='p22'))
        sm.add_widget(p3(name='p3'))

        return sm

app().run()

#(x**(2/3))+(.9*((3.3-(x**2)**((1/2)*sin(value*pi*x)))))

                      
    
