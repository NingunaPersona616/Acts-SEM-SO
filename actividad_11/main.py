import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

def init():
    for i in ram:
        i.setStyleSheet("background-color: gray")
    widget.slot1.setStyleSheet("background-color: purple")
    widget.ramStatus.setText("archivo cargado en RAM")
    widget.diskStatus.setText("Nada por escribir en disco")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    ram=[widget.slot1, widget.slot2, widget.slot3]
    widget.show()
    init()
    widget.thread={}
    sys.exit(app.exec())