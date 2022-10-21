import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
#widget.label_1.setStyleSheet("background-color: gray")

def setDefault():
    cont = 0
    for i in vslot:
        i.setStyleSheet("background-color: gray")
        i.setText("             x")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    vslot=[widget.slot_0, widget.slot_1, widget.slot_2, widget.slot_3, widget.slot_4, widget.slot_5, widget.slot_6, widget.slot_7, widget.slot_8, widget.slot_9, widget.slot_10, widget.slot_11]
    setDefault()
    sys.exit(app.exec())