import sys
from mainwindow import MainWindow
from batchProcessing import *
from PyQt5.QtWidgets import QApplication

def startButton():#funcion que controla como se comportará el boton
    setProgressInterface(widget)#llamamos a la funcion que comienza el procesamiento
    widget.startButton.setEnabled(True)#al finalizar el procesamiento volvera a estar habilitado el boton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.startButton.clicked.connect(startButton)#declaracion de que hara el boton si es presionado
    sys.exit(app.exec())#esta funcion hace que se termine el programa cuando la interfaz sea cerrada