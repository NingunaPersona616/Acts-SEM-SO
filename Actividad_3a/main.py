import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from multiProgramming import *

def startButton():#el boton llamará a la funcion que inicia el proceso de simulacion de la multiprogramacion
    widget.startButton.setEnabled(False)#Se desactiva el boton para no bugear la interfaz
    multiprogramming(widget)#mandamos como parametro a la interfaz para que puedan ser manipulados sus elementos en las funciones
    QtTest.QTest.qWait(10100)
    widget.startButton.setEnabled(True)#al finalizar el procesamiento volvera a estar habilitado el boton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()#creamos el objeto
    widget.thread={}#le asignamos a thread la caracteristica de que pueda almacenar varios en un arreglo
    widget.show()#lo mostramos
    widget.startButton.clicked.connect(startButton)#especificamos que hará el boton en caso de ser presionado
    sys.exit(app.exec())
    