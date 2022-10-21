
from threadClass import threadClass
from PyQt5 import QtTest
from random import *

def ramSetter(widget, fslots, vslots, split, slots):
    index=0
    while(index<6):
        vslots[slots[index]].setText(f"{split[index]}")
        vslots[slots[index]].setStyleSheet("background-color: pink")
        index=index+1
    for i in range(4):
        fslots[i].setText(f"{vslots[slots[i]].text()}")
        fslots[i].setStyleSheet("background-color: pink")
        
        widget.page.setText(f"{vslots[slots[i]].text()}")
        widget.frame.setText(f"{i}")
        QtTest.QTest.qWait(1000)
        startThread(widget, i)
        widget.cont=widget.cont+1



def stopThread(widget, index):
    widget.thread[index].stop()


def startThread(widget, index):
    random=randint(10, 500)
    widget.thread[index]=threadClass(parent=None, index=index)#asignamos a una posicion del arreglo un objeto de la clase threadClass que seran nuestros hilos y el objeto adquiere en su atributo index su posicion dentro del arreglo a manera de identificacion
    QtTest.QTest.qWait(random)#esperamos un determinado tiempo
    widget.thread[index].start()#señalizamos que nuestro hilo iniciara su proceso
    widget.thread[index].any_signal.connect(widget.bar)#
    widget.thread[index].nextPage.connect(widget.nextPage)#


    