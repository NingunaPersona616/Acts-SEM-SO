from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):#generamos la clase mainwindow para que esta adquiera como atributos los elementos de la ventana
    def __init__(self, parent=None):#inicializamos la ventana y todos sus elementos para que el objeto generado las conozca y podamos manipularlas mediante la creacion de un objeto
        super().__init__(parent)
        uic.loadUi(r"form.ui", self)#cargamos los elementos de la interfaz
        
    def processFunction(self, counter):#processFunction recibira como parametro un contador que sera el que se cargará en la barra de progreso
        cnt=counter#lo igualamos a una variable local
        index=self.sender().index#cachamos el index del thread para saber que barra llenar haciendo match entre barra e hilo
        #esta funcion será llamada varias veces mediante señales y es la que generará la carga visual de las barras segun el hilo que emita la señal
        if index==1:
            self.bar_1.setValue(cnt)
        if index==2:
            self.bar_2.setValue(cnt)
        if index==3:
            self.bar_3.setValue(cnt)
        if index==4:
            self.bar_4.setValue(cnt)
        if index==5:
            self.bar_5.setValue(cnt)
        



