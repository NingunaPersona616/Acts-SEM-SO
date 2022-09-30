# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"form.ui", self)




    def taskManager(self, counter):#processFunction recibira como parametro un contador que sera el que se cargará en la barra de progreso
            cnt=counter#lo igualamos a una variable local
            index=self.sender().index#cachamos el index del thread para saber que barra llenar haciendo match entre barra e hilo
            #esta funcion será llamada varias veces mediante señales y es la que generará la carga visual de las barras segun el hilo que emita la señal
            if index==0:
                self.bar_0.setValue(cnt)
            if index==1:
                self.bar_1.setValue(cnt)
            if index==2:
                self.bar_2.setValue(cnt)
            #if index==3:
                #self.bar_3.setValue(cnt)
