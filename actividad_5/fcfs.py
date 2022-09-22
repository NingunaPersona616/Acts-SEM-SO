from concurrent.futures import process
from threadClass import threadClass
from PyQt5 import QtTest
from random import *


def stopThread(widget, index):
    widget.thread[index].stop()


def startThread(widget, index):
    random=randint(10, 500)
    widget.thread[index]=threadClass(parent=None, index=index)#asignamos a una posicion del arreglo un objeto de la clase threadClass que seran nuestros hilos y el objeto adquiere en su atributo index su posicion dentro del arreglo a manera de identificacion
    QtTest.QTest.qWait(random)#esperamos un determinado tiempo
    widget.thread[index].start()#señalizamos que nuestro hilo iniciara su proceso
    widget.thread[index].any_signal.connect(widget.fcfs)
