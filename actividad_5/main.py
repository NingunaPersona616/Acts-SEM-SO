import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from threadClass import *
from PyQt5 import QtCore

CantProcesos = 3

def restartBars():
    for Bar in bars:
        Bar.setValue(0)

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

def RR():
    restartBars()
    widget.startButton_2.setEnabled(False)

    colaProcesos=[{"index": 0, "status": "init"}, {"index": 1, "status": "init"}, {"index": 2, "status": "init"},]
    quantum = 0

    while(len(colaProcesos)>0):
        QtTest.QTest.qWait(400) #Espera lo que espera la barra de carga o se bugea pq trabajan en contextos diferentes y se desincronizan
        #print('Thread: ', index, 'value: ', bars[index].value())
        app.processEvents() #funcion pa que no se freezie la GUI con el while
        Proceso = colaProcesos[0] #Toma el tope de la cola
        index = Proceso['index']
        status = Proceso['status']
        print(index, status)

        print('Thread: ', index, 'value: ', bars[index].value())

        if(bars[index].value() == 100):
            stopThread(widget, index)
            colaProcesos[0]['status'] = "finished"
            colaProcesos.pop(0)            

        elif(status == "init"):
            startThread(widget, index)
            colaProcesos[0]['status'] = "running"
            status = "running"

        elif(status == "stopped"):
            startThread(widget, index)
            colaProcesos[0]['status'] = "running"
            status == "running"

        elif((bars[index].value() % 10) == 0):
            stopThread(widget, index)
            colaProcesos[0]['status'] = "stopped"
            status = "stopped"
            Aux = colaProcesos.pop(0)
            colaProcesos.append(Aux)
            quantum = 0

        elif(status == "running"):
            print("jalando")


    widget.startButton_2.setEnabled(True)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    bars = [widget.bar_0,
            widget.bar_1,
            widget.bar_2]


    widget.thread={}
    widget.startButton.clicked.connect(FCFS)
    widget.startButton_2.clicked.connect(RR)
    sys.exit(app.exec())