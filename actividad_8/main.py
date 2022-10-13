from concurrent.futures import thread
import sys
from tracemalloc import start
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from rw import *


def fillLabels():
    cont=0
    for i in readers:
        i.setText(f"Lector {cont}")
        cont=cont+1
    widget.writer_0.setText("Escritor 0")

def linkButtons():
    widget.read.clicked.connect(read)
    widget.write.clicked.connect(write)


def read():
    
    if widget.semaforo==0:
        index=0
        counter=0
        while (index<2):
            startThread(widget, index, 0)
            index=index+1
        for i in used_by:
            i.setText(readers[counter].text())
            counter=counter+1
        widget.status.setText("En lectura")
        widget.available.setText("No")
        widget.read.setEnabled(False)
        widget.write.setEnabled(True)
    else:
        widget.alert.setText("el recurso esta siendo utilizado\npor el Escritor por favor espere...")
        

def write():
    stopAll(widget)
    widget.semaforo=1
    widget.status.setText("En escritura")
    widget.available.setText("No")
    widget.read.setEnabled(True)
    widget.write.setEnabled(False)
    widget.used_by_0.setText("Escritor")
    widget.used_by_1.setText("")
    startThread(widget, 1, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    readers=[widget.reader_0, widget.reader_1]
    used_by=[widget.used_by_0, widget.used_by_1]
    widget.show()
    fillLabels()
    linkButtons()
    widget.status.setText("Libre")
    widget.available.setText("si")
    widget.used_by_0.setText("Nadie")
    widget.thread={}
    sys.exit(app.exec())
