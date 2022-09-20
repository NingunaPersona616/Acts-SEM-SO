import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from threadClass import *
from PyQt5 import QtCore

def restartBars():
    for i in bars:
        i.setValue(0)

#FCFS ta hecho con una cola de indices(supestamente) y con barras (pero igual se puede usar los hilos directamente)
def FCFS():
    restartBars()   #Reinicia las barras por si se vuelve a llamar
    widget.startButton.setEnabled(False)    #Desactiva boton
    index=0
    while (index < len(bars)):  #Mientras no se carguen todas las barras
        QtTest.QTest.qWait(500) #Espera lo que espera la barra de carga o se bugea pq trabajan en contextos diferentes y se desincronizan
        print('Thread: ', index, 'value: ', bars[index].value())
        app.processEvents() #funcion pa que no se freezie la GUI con el while
        
        if(bars[index].value()==100):   #Si la barra actual esta al 100 se para y se pasa a la siguiente barra
            stopThread(widget, index)
            index+=1
            print(index, 'Barra que se cargara')

        elif(bars[index].value()==0):   #Si la barra no esta iniciada ps la inicia (?)
            startThread(widget, index)
        
        
    widget.startButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    bars = [widget.bar_0,
            widget.bar_1,
            widget.bar_2]


    widget.thread={}
    widget.startButton.clicked.connect(FCFS)
    sys.exit(app.exec())