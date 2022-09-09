import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from taskManager import *

def beginAll():
    startAll(widget)
    setRunning(status)

def endAll ():
    stopAll(widget)
    setFinished(status)


def setFinished(status):
    for i in status:
        i.setText("Detenido")

def setRunning(status):
    for i in status:
        i.setText("Corriendo")

def linkEndButtons(endButtons):
    for i in endButtons:
        i.clicked.connect()#aqui va la funcion para terminarde manera individual
    print("botones de terminar linkeados")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    status={widget.status_1, widget.status_2, widget.status_3, widget.status_4}
    endButtons={widget.kill_1, widget.kill_2, widget.kill_3, widget.kill_4}
    #funcion que detenga un hilo indivual
    #1.-funcion para inicio individual, para terminar individual, pausa y resume
    setFinished(status)
    linkEndButtons(endButtons)
    widget.thread={}
    widget.start_all.clicked.connect(beginAll)
    widget.stop_all.clicked.connect(endAll)
    sys.exit(app.exec())