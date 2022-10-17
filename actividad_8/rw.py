
from threadClass import threadClass
from PyQt5 import QtTest
from random import *


def stopThread(widget, index):
    widget.thread[index].stop()

def stopAll(widget):
    index=0
    if(len(widget.thread)>1):
        while(index<2):
            widget.thread[index].stop()
            index=index+1
    else:
        pass



def startThread(widget, index, id):
    random=randint(10, 500)
    widget.thread[index]=threadClass(parent=None, index=index, id=id)#asignamos a una posicion del arreglo un objeto de la clase threadClass que seran nuestros hilos y el objeto adquiere en su atributo index su posicion dentro del arreglo a manera de identificacion
    QtTest.QTest.qWait(random)#esperamos un determinado tiempo
    widget.thread[index].start()#señalizamos que nuestro hilo iniciara su proceso
    widget.thread[index].any_signal.connect(widget.task)#
    widget.thread[index].semaforo.connect(widget.end)#
    widget.thread[index].enable.connect(widget.enable)#



