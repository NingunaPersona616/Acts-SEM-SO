from PyQt5 import QtCore
from PyQt5 import QtTest
from random import *
from mainwindow import *
from main import *

VERDE = 1
ROJO = 0

class threadClass(QtCore.QThread):#la clase threadClass generará un objeto que contenga un hilo pero que ademas podamos modificar su comportamiento mediante metodos de la misma clase que serán reeimplementados
    any_signal=QtCore.pyqtSignal(int)#any_signal sera una señal que activirá los slots en los cuales se utilice el connect() similar al comportamiento de un boton, una señal dada iniciara un slot que se haya especificado en el codigo
    sem_signal = QtCore.pyqtSignal(int) #Sem_Signal señal del semaforo

    def __init__(self, parent= None, index=0, value=0):#inicializamos el objeto y damos un atributo llamado index que sera el que nos indique en que posicion del arreglo está, será una especie de ID, al inicializarlo estará en 0 pero cuando se crea una clase se puede especificar el valor.
    #vease la linea 9 de multiProgramming.py    
        super(threadClass,self).__init__(parent)
        self.index=index#se iguala el index de nuestro objeto al index que llego como parametro
        self.value=value
        self.is_running=True#y activamos la bandera de que el hilo está corriendo
        self.terminate=False#seteamos que terminate es falso para que pueda ejecutarse de manera correcta y para despues cambiar su valor a false cuando sea necesario

    def run(self):#funcion que iniciara el proceso, en multiProgramming se utiliza desde el thread el metodo llamado start() este metodo a su vez inicializa y manda a llamar a su metodo run (que es este aunque solo que nosotros lo reeimplementamos para añadir funcionalidades extras a su comportamiento habitual, si no estuviese reeimplementado start() hubiera llamado a su metodo nativo run())
        #citando la documentacion de QT "You can reimplement this function to facilitate advanced thread management. Returning from this method will end the execution of the thread."
        print(f"starting thread: {self.index} initial value: {self.value} ")#informacion sobre que "hilo se esta iniciando"
        cnt=self.value#contador en 0 para iniciar la simulacion
        #random=randint(10, 500)#numero random para simular la espera entre procesos
        #random2=randint(10, 500)#numero random para simular la espera entre procesos x2
        #QtTest.QTest.qWait(random)#llamamos al primer numero random para la espera

        self.sem_signal.emit(ROJO)

        while not(self.terminate):#ciclo que controlará el envio de señales despues de ser llamado la primera vez en multiprogramming.py, como los procesos correran en un hilo independiente solo es necesario ser mandando señales a dichos hilos
            cnt=cnt+5#la barra incrementara segun lo que le sumemos al contador
            self.any_signal.emit(cnt)#emitimos otra señal para que se acumule en la barra de tareas
            QtTest.QTest.qWait(500)#esperamos otros segundos random
            if cnt==100:#si la barra llega a 100 saldra de la subrutina del while
                self.any_signal.emit(cnt)
                self.stop()
                self.sem_signal.emit(VERDE)
                

    def stop(self):
        self.terminate=True
        self.is_running=False
        print(f"stopping thread: {self.index}")

def stopThread(widget, index):
    widget.thread[index].stop()

def currentValues(widget, index):
    value=widget.bar_0.value()
    return value

def startThread(widget, index):
    print('De perdida entra aqui?')
    random=randint(10, 500)
    value=currentValues(widget, index)
    widget.thread[index]=threadClass(parent=None, index=index, value=value)#asignamos a una posicion del arreglo un objeto de la clase threadClass que seran nuestros hilos y el objeto adquiere en su atributo index su posicion dentro del arreglo a manera de identificacion
    QtTest.QTest.qWait(random)#esperamos un determinado tiempo
    widget.thread[index].start()#señalizamos que nuestro hilo iniciara su proceso
    widget.thread[index].any_signal.connect(widget.taskManager)#
    widget.thread[index].sem_signal.connect(widget.semaforo)
