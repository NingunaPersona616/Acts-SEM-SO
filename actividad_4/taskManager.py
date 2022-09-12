from concurrent.futures import process
from threadClass import threadClass
from PyQt5 import QtTest
from random import *


# def startAll(widget):
#     index=0
#     random=randint(10, 500)##generamos un numero aleatorio para que haya diferencia de tiempo entre la inicializacion de los procesos
#     while(index<5):
#         widget.thread[index]=threadClass(parent=None, index=index)#asignamos a una posicion del arreglo un objeto de la clase threadClass que seran nuestros hilos y el objeto adquiere en su atributo index su posicion dentro del arreglo a manera de identificacion
#         QtTest.QTest.qWait(random)#esperamos un determinado tiempo
#         widget.thread[index].start()#señalizamos que nuestro hilo iniciara su proceso
#         widget.thread[index].any_signal.connect(widget.taskManager)#emitimos una señal para nuestra funcion processFunction
#         index=index+1#avanzamos en la posicion de los arreglos
#         widget.status_1.setText("Corriendo")
#         widget.status_2.setText("Corriendo")
#         widget.status_3.setText("Corriendo")
#         widget.status_4.setText("Corriendo")

# def stopAll(widget):
#     index=1
#     while(index<5):
#         widget.thread[index].stop()
#         index=index+1

def stopThread(widget, index):
    widget.thread[index].stop()

def currentValues(widget, index):
    bars = [widget.bar_0,
            widget.bar_1,
            widget.bar_2,
            widget.bar_3]
    value=bars[index].value()
    return value

def startThread(widget, index):
    random=randint(10, 500)
    value=currentValues(widget, index)
    widget.thread[index]=threadClass(parent=None, index=index, value=value)#asignamos a una posicion del arreglo un objeto de la clase threadClass que seran nuestros hilos y el objeto adquiere en su atributo index su posicion dentro del arreglo a manera de identificacion
    QtTest.QTest.qWait(random)#esperamos un determinado tiempo
    widget.thread[index].start()#señalizamos que nuestro hilo iniciara su proceso
    widget.thread[index].any_signal.connect(widget.taskManager)#

    
