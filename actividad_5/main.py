import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from fcfs import *
import numpy as np


def start():
    list=np.random.permutation(3)[:3].tolist()
    index=0
    f=open("task.txt", "r")
    for i in arrival:
        i.setText(str(list[index]))
        names[list[index]].setText(f.readline()) 
        startThread(widget, list[index])
        index=index+1
    
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.startButton.clicked.connect(start)
    arrival=[widget.number_0, widget.number_1, widget.number_2]
    names=[widget.name_0, widget.name_1, widget.name_2]
    widget.thread={}
    sys.exit(app.exec())