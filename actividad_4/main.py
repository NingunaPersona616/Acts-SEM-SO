import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from taskManager import *
from PyQt5 import QtCore

#funciones que setean el valor del proceso, puede ser corriendo o denetnido


def setFinished(status, index):
    if(index==-1):
        for i in status:
            i.setText("Detenido")
    status[index].setText("Detenido")

def setRunning(status, index):
    status[index].setText("Corriendo")


#funciones para iniciar o detener los hilos de manera individual

def pauseOne():
    index=int(playButtons.index(widget.sender()))

    startButtons[index].setEnabled(True)

    currentStatus = bars[index].value()

    if(playButtons[index].text()=="⏸"):
        playButtons[index].setText("▶")
        setFinished(status, index)
        stopThread(widget, index)

        bars[index].setValue(currentStatus)

    elif(playButtons[index].text()=="▶"):
        playButtons[index].setText("⏸")
        setRunning(status, index)
        startThread(widget, index)



def stopOne():
    index=int(endButtons.index(widget.sender()))
    endButtons[index].setEnabled(False)
    startButtons[index].setEnabled(True)
    playButtons[index].setText("▶")
    playButtons[index].setEnabled(False)
    setFinished(status, index)
    bars[index].setValue(0)
    stopThread(widget, index)

    
def startOne():
    index=int(startButtons.index(widget.sender()))
    endButtons[index].setEnabled(True)
    startButtons[index].setEnabled(False)
    playButtons[index].setEnabled(True)
    playButtons[index].setText("⏸")
    print(index)
    setRunning(status, index)
    startThread(widget, index)

#funciones para enlazar los botones con la funcion
def disableEndButtons(endButtons, playButtons):
    for i in endButtons:
        i.setEnabled(False)
    for i in playButtons:
        i.setEnabled(False)
   

def linkStartButtons(startButtons):
    for i in startButtons:
        i.clicked.connect(startOne)
    print("botones de start linkeados")

def linkEndButtons(endButtons):
    for i in endButtons:
        i.clicked.connect(stopOne)#aqui va la funcion para terminarde manera individual   
    print("botones de terminar linkeados")

def linkPlayButtons(playButtons):
    for i in playButtons:
        i.clicked.connect(pauseOne)
    print("botones de play/pause linkeados")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    status=[widget.status_1, widget.status_2, widget.status_3, widget.status_4]
    endButtons=[widget.kill_1, widget.kill_2, widget.kill_3, widget.kill_4]
    playButtons=[widget.play_0,widget.play_1,widget.play_2,widget.play_3]
    startButtons=[widget.start_button_1,
                  widget.start_button_2, 
                  widget.start_button_3, 
                  widget.start_button_4,]
    bars = [widget.bar_0,
            widget.bar_1,
            widget.bar_2,
            widget.bar_3]
    #funcion que detenga un hilo indivual
    #1.-funcion para inicio individual, para terminar individual, pausa y resume
    disableEndButtons(endButtons, playButtons)
    setFinished(status, -1)
    linkEndButtons(endButtons)
    linkStartButtons(startButtons)
    linkPlayButtons(playButtons)
    widget.thread={}
    sys.exit(app.exec())