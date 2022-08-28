from PyQt5 import QtTest
from threadClass import threadClass
from random import *

def multiprogramming(widget):#primeramente realizaremos la asignacion de cada uno de los hilos que vayamos generando, en este caso son 5
    index=1#inciamos en la posicion 1
    random=randint(10, 500)##generamos un numero aleatorio para que haya diferencia de tiempo entre la inicializacion de los procesos
    while (index<6):#ciclo que nos ayudara a asignar en diferentes posiciones del arreglo widget.thread={} para poderlos identificarlos mas adelante
        widget.thread[index]=threadClass(parent=None, index=index)#asignamos a una posicion del arreglo un objeto de la clase threadClass que seran nuestros hilos y el objeto adquiere en su atributo index su posicion dentro del arreglo a manera de identificacion
        QtTest.QTest.qWait(random)#esperamos un determinado tiempo
        widget.thread[index].start()#señalizamos que nuestro hilo iniciara su proceso
        widget.thread[index].any_signal.connect(widget.processFunction)#emitimos una señal para nuestra funcion processFunction
        index=index+1#avanzamos en la posicion de los arreglos




