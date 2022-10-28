import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import numpy as np
from pager import *
#widget.label_1.setStyleSheet("background-color: gray")

def setDefault():
    for i in vslots:
        i.setStyleSheet("background-color: gray")
        i.setText("x")
    for i in fslots:
        i.setStyleSheet("background-color: gray")
    widget.name.setText("Git")
    widget.size.setText("24 KiB")

    ramSetter(widget ,fslots, vslots, widget.split, widget.slots)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    vslots=[widget.slot_0, widget.slot_1, widget.slot_2, widget.slot_3, widget.slot_4, widget.slot_5, widget.slot_6, widget.slot_7, widget.slot_8, widget.slot_9, widget.slot_10, widget.slot_11]

    fslots=[widget.fslot_0, widget.fslot_1, widget.fslot_2, widget.fslot_3]
    widget.thread={}
    setDefault()
    sys.exit(app.exec())