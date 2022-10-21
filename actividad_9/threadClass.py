from PyQt5 import QtCore
from PyQt5 import QtTest
from random import *
#from mainwindow import *
#from main import *

class threadClass(QtCore.QThread):#la clase threadClass generará un objeto que contenga un hilo pero que ademas podamos modificar su comportamiento mediante metodos de la misma clase que serán reeimplementados
    any_signal=QtCore.pyqtSignal(int)#any_signal sera una señal que activirá los slots en los cuales se utilice el connect() similar al comportamiento de un boton, una señal dada iniciara un slot que se haya especificado en el codigo
    nextPage=QtCore.pyqtSignal(int)
    def __init__(self, parent= None, index=0):#inicializamos el objeto y damos un atributo llamado index que sera el que nos indique en que posicion del arreglo está, será una especie de ID, al inicializarlo estará en 0 pero cuando se crea una clase se puede especificar el valor.
    #vease la linea 9 de multiProgramming.py    
        super(threadClass,self).__init__(parent)
        self.index=index#se iguala el index de nuestro objeto al index que llego como parametro
        self.is_running=True#y activamos la bandera de que el hilo está corriendo
        self.terminate=False#seteamos que terminate es falso para que pueda ejecutarse de manera correcta y para despues cambiar su valor a false cuando sea necesario

    def run(self):#funcion que iniciara el proceso, en multiProgramming se utiliza desde el thread el metodo llamado start() este metodo a su vez inicializa y manda a llamar a su metodo run (que es este aunque solo que nosotros lo reeimplementamos para añadir funcionalidades extras a su comportamiento habitual, si no estuviese reeimplementado start() hubiera llamado a su metodo nativo run())
        #citando la documentacion de QT "You can reimplement this function to facilitate advanced thread management. Returning from this method will end the execution of the thread."
        #print(f"starting thread: {self.index} initial value: {self.value} ")#informacion sobre que "hilo se esta iniciando"
        cnt=0#contador en 0 para iniciar la simulacion
        random=randint(10, 500)#numero random para simular la espera entre procesos
        random2=randint(10, 500)#numero random para simular la espera entre procesos x2
        QtTest.QTest.qWait(random)#llamamos al primer numero random para la espera
        while not(self.terminate):#ciclo que controlará el envio de señales despues de ser llamado la primera vez en multiprogramming.py, como los procesos correran en un hilo independiente solo es necesario ser mandando señales a dichos hilos
            cnt=cnt+5#la barra incrementara segun lo que le sumemos al contador
            self.any_signal.emit(cnt)#emitimos otra señal para que se acumule en la barra de tareas
            QtTest.QTest.qWait(random2)#esperamos otros segundos random
            if cnt==100:#si la barra llega a 100 saldra de la subrutina del while
                self.nextPage.emit(1)
                self.stop
                

    def stop(self):
        self.terminate=True
        self.is_running=False
        print(f"stopping thread: {self.index}")