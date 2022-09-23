import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5 import QtTest
from fcfs import *
import numpy as np

def setBars():
    for i in bars:
        i.setValue(0)

def start():
    setBars()
    list=np.random.permutation(3)[:3].tolist()
    index=0
    f=open("task.txt", "r")
    widget.startButton.setEnabled(False)
    j=0
    for j in range(3):
        names[list[j]].setText(f.readline())
        arrival[j].setText(str(j))
    for i in arrival:
        startThread(widget, index)
        QtTest.QTest.qWait(5000)
        index=index+1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.startButton.clicked.connect(start)
    arrival=[widget.number_0, widget.number_1, widget.number_2]
    names=[widget.name_0, widget.name_1, widget.name_2]
    bars=[widget.bar_0, widget.bar_1, widget.bar_2]
    widget.thread={}
    sys.exit(app.exec())