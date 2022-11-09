import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from iod import *

def init():
    widget.printButton.clicked.connect(printFile)
    widget.saveButton.clicked.connect(saveFile)
    for i in ram:
        i.setStyleSheet("background-color: gray")
    widget.slot0.setStyleSheet("background-color: purple")
    widget.ramStatus.setText("archivo cargado en RAM")
    widget.diskStatus.setText("Nada por escribir en disco")
    widget.color0.setStyleSheet("background-color: purple")
    widget.color1.setStyleSheet("background-color: cyan")
    widget.color2.setStyleSheet("background-color: pink")
    widget.process0.setText("Archivo")
    widget.process1.setText("impresion")
    widget.process2.setText("guardado")

def printFile():
    widget.printStatus.setText("imprimiendo...")
    widget.slot1.setStyleSheet("background-color: cyan")
    startThread(widget, 0)
    widget.printButton.setEnabled(False)

def saveFile():
    print("Guardando archivo")
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    ram=[widget.slot0, widget.slot1, widget.slot2]
    widget.show()
    init()
    widget.thread={}
    sys.exit(app.exec())