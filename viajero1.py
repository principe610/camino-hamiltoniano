


from matplotlib import pyplot as mpl
import math

class Point(object):#creas la clase point,q es un objeto(en este caso un punto
    def __init__(self,xx,yy):#self de cajon y tus entradas en este caso xx,yy
        self.x= xx#almacenas tu entrada
        self.y= yy#almacenas tu entrada

        
class nodo(Point):#esto que ases aqui se llama heredar una clase a otra o llamar una clase    
    numnodo=0 
    def __init__(self,xx,yy):
        self.x= (xx)
        self.y=(yy)
        global u
        u=(self.x,self.y)
        super(nodo,self).__init__(xx,yy)#usaras la palabra nodo para llamarlo y entraran (v,k)
        
        self.id= nodo.numnodo#le das valor del contador al id
        nodo.numnodo +=1#agregas uno al contador    


    
    
    
    def __str__(self):
        return '({0},{1})'.format(self.x,self.y)

    


    



def grpunto(c):
    
    c= nodo(c.x,c.y)
    u34= mpl.plot(c.x,c.y,'o')
    return u34



def agrenodo(u):
    u= nodo(u.x,u.y)
    u=(u.x,u.y)
    return u
        








def grrecta(g,e):
    g= nodo(g.x,g.y)
    e= nodo(e.x,e.y)
    
    u464= mpl.plot([g.x,e.x],[g.y,e.y],'g-')
    
    return u464

def mostrar(g4,e5):
    g4= nodo(g4.x,g4.y)
    e5= nodo(e5.x,e5.y)
    asd=(e5.y+g4.y)/2
    asd2=(e5.x+g4.x)/2
    yex2=round((distancia2p(g4,e5)),2)
    yex=str(yex2)
    u464h= mpl.text(asd2,asd,yex+'u',color='purple',fontsize=12)
    
    return u464h



def distancia(a,b):
    
        a=nodo(a.x,a.y)
        b=nodo(b.x,b.y)
        d2=math.sqrt((a.x - b.x)**2)
        return d2

def distanciay(a,b):
    
        a=nodo(a.x,a.y)
        b=nodo(b.x,b.y)
        d210=math.sqrt((a.y - b.y)**2)
        return d210

def distancia2p(a,b):
    
        a=nodo(a.x,a.y)
        b=nodo(b.x,b.y)
        d22=math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
        return d22
    
def mayor(lista):
    max=lista[0]
    for x in lista:
        if x > max:
            max=x
    return max


def menor(lista):
    min=lista[0]
    for n in lista:
        if n < min:
            min= n
    return min

#pendiente m=(yf2-yi1)/(xf2-xi1)

def pendiente(aaaaa,bbbbb):
    aaaaa=nodo(aaaaa.x,aaaaa.y)
    bbbbb=nodo(bbbbb.x,bbbbb.y)
    m=(bbbbb.y-aaaaa.y)/(bbbbb.x-aaaaa.x)
    return m

def calb(eee,mmmm):
    eee=nodo(eee.x,eee.y)
    bb=eee.y-(mmmm*eee.x)
    return bb

#ec. de la recta y= m*x +b

def erecta(ttt,mmm,bbb):
    ttt=nodo(ttt.x,ttt.y)
    ddd= (mmm*ttt.x) +bbb
    print('y=',ddd)
    print('y=',mmm,'X +',bbb)

def erecta2p(cf,vh):
    cf=nodo(cf.x,cf.y)
    vh=nodo(vh.x,vh.y)
    m=((vh.y-cf.y)/(vh.x-cf.x))
    b=cf.y-(m*cf.x)
    #print('y=',m,'X +',b)
    i3=nodo(m,b)
    return i3


    
    
    
def dispr(punto,pub1,pub2):
    pub1=nodo(pub1.x,pub1.y)
    pub2=nodo(pub2.x,pub2.y)
    kk=(pub2.y-pub1.y)
    tt=(pub2.x-pub1.x)
    A=kk
    B= tt
    C=((kk*pub2.x)-(tt*pub2.y))

    punto=nodo(punto.x,punto.y)
    dpl=(((A*punto.x)-(B*punto.y)-(C))/(math.sqrt((A**2)+(B**2))))
    return dpl
    












        

    
    








