import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
import numpy as np 


def producers ():
    cont=0
    index=0
    for i in process:
        i.setText(names[cont])
        use=ramUsage[cont]
        
        while(use>0):
            ram[index].setStyleSheet(f"background-color: {colors[cont]}")
            
            index=index+1
            use=use-1
        colorProcess[cont].setStyleSheet(f"background-color: {colors[cont]}")
        cont=cont+1


def setColor():
    for i in ram:
        i.setStyleSheet("background-color: gray")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    #arreglos para poder manejar mejor los slots de memoria y el display del nombre de los procesos
    process=[widget.process_0, widget.process_1, widget.process_2, widget.process_3, widget.process_4, widget.process_5]
    colorProcess=[widget.color_0, widget.color_1, widget.color_2, widget.color_3, widget.color_4, widget.color_5]
    ram=[widget.slot_0, widget.slot_1, widget.slot_2, widget.slot_3, widget.slot_4, widget.slot_5, widget.slot_6, widget.slot_7]
    #inicializa los colores de la ram para que se ponga en gris para dar a entender que no está en uso
    names=["photoshop", "edge", "ableton", "vs-code", "krita", "qemu"]
    ramUsage=[2, 1, 2, 1, 1, 1]
    colors=["purple", "gree", "red", "blue", "yellow", "cyan"]
    setColor()
    
    widget.show()
    producers()
    widget.thread={}
    sys.exit(app.exec())
