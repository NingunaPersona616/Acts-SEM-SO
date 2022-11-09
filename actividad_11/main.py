import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtTest
from iod import *
import os

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
    f = open("doc.txt", "r")
    text=f.read() 
    widget.buffer.setText(f"{text}")
    f.close()

def printFile():
    widget.printStatus.setText("imprimiendo...")
    widget.slot1.setStyleSheet("background-color: cyan")
    startThread(widget, 0)
    widget.printButton.setEnabled(False)

def saveFile():
    widget.saveButton.setEnabled(False)
    widget.diskStatus.setText("Escribiendo en disco...")
    widget.slot2.setStyleSheet("background-color: pink")
    text=widget.buffer.toPlainText()
    file = open("doc.txt", "w")
    file.write(f"{text}")
    file.close()
    QtTest.QTest.qWait(2000)
    fileName = "doc.txt"
    fileStats = os.stat(fileName)
    widget.fileName.setText("doc.txt")
    widget.fileSize.setText(f"{fileStats.st_size} KiB")
    QtTest.QTest.qWait(3000)
    widget.saveButton.setEnabled(True)
    widget.diskStatus.setText("Nada por escribir en disco")
    widget.slot2.setStyleSheet("background-color: gray")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    ram=[widget.slot0, widget.slot1, widget.slot2]
    widget.show()
    init()
    widget.thread={}
    sys.exit(app.exec())