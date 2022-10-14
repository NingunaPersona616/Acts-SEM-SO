from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    semaforo=0#no está escribiendo
    #0 esta leyendo
    #1 esta escribiendo
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"form.ui", self)

    def task(self, counter):#processFunction recibira como parametro un contador que sera el que se cargará en la barra de progreso
            cnt=counter#lo igualamos a una variable local
            index=self.sender().index#cachamos el index del thread para saber que barra llenar haciendo match entre barra e hilo
            #esta funcion será llamada varias veces mediante señales y es la que generará la carga visual de las barras segun el hilo que emita la señal
            self.bar_0.setValue(cnt)
    def end(self, flag):
        if(flag==0):
            self.semaforo=0
    def enable(self, flag):
        if(flag==0):
            self.write.setEnabled(True)
            self.available.setText("Si")

