from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
VERDE = 1
ROJO = 0

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"form.ui", self)
        self.semStatus = VERDE

    def taskManager(self, counter):#processFunction recibira como parametro un contador que sera el que se cargará en la barra de progreso
            cnt=counter#lo igualamos a una variable local
            index=self.sender().index#cachamos el index del thread para saber que barra llenar haciendo match entre barra e hilo
            #esta funcion será llamada varias veces mediante señales y es la que generará la carga visual de las barras segun el hilo que emita la señal
            #if index==0:
            self.bar_0.setValue(cnt)

    #Se supondria que todo lo relacionado a SEM sea una clase pero se hace lo que se puede
    def semaforo(self, semSignal):
        if(semSignal==VERDE):
            self.light_status.setStyleSheet("background-color: rgb(0, 255, 0)")
            self.semStatus=VERDE

        elif(semSignal == ROJO):
            self.light_status.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.semStatus=ROJO

