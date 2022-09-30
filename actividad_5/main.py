import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from threadClass import *


CantProcesos = 3

def restartBars():
    for Bar in bars:
        Bar.setValue(0)

#FCFS ta hecho con una cola de indices(supestamente) y con barras (pero igual se puede usar los hilos directamente)
def FCFS():
    restartBars()   #Reinicia las barras por si se vuelve a llamar
    widget.startButton.setEnabled(False)    #Desactiva boton
    widget.startButton_2.setEnabled(False)

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
    widget.startButton_2.setEnabled(True)

def RR():
    restartBars()
    widget.startButton.setEnabled(False)    #Desactiva boton
    widget.startButton_2.setEnabled(False)


    colaProcesos=[{"index": 0, "status": "init"}, {"index": 1, "status": "init"}, {"index": 2, "status": "init"}]
    quantum = 0

    while(len(colaProcesos)>0): #Mientras haya un proceso en la cola
        QtTest.QTest.qWait(400) #Espera lo que espera la barra de carga o se bugea pq trabajan en contextos diferentes y se desincronizan

        app.processEvents() #funcion pa que no se freezie la GUI con el while

        #Toma el tope de la cola
        index = colaProcesos[0]['index']
        print(index, colaProcesos[0]['status'])

        print('Thread: ', index, 'value: ', bars[index].value())

        if(bars[index].value() == 100): #Si el proceso ya esta al 100% lo detiene y lo borra de la cola
            stopThread(widget, index)
            colaProcesos[0]['status'] = "finished"
            colaProcesos.pop(0)            

        elif(colaProcesos[0]['status'] == "init"):  #Si es un proceso nuevo pues lo inicia
            startThread(widget, index)
            colaProcesos[0]['status'] = "running"

        elif(colaProcesos[0]['status'] == "stopped"):   #Si el proceso esta en pausa lo inicia
            startThread(widget, index)
            colaProcesos[0]['status'] = "running"

        elif((bars[index].value() % 10) == 0):  #Si el proceso alcanzo el quantum de ejecucion
            stopThread(widget, index)
            colaProcesos[0]['status'] = "stopped"   #Detiene el proceso
            Aux = colaProcesos.pop(0)   #Lo kickea de la cola
            colaProcesos.append(Aux)    #Y lo vuelve a encolar al final

        elif(colaProcesos[0]['status'] == "running"):   #Si esta el proceso se esta corriendo, pues sigue corriendo
            print("jalando")


    widget.startButton.setEnabled(True)
    widget.startButton_2.setEnabled(True)


def closeEvent():
    for i in range(len(widget.thread)):
        widget.thread[i].stop()

    app.quit()
    widget.close()
    app.exit()
    sys.exit()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    #app.aboutToQuit.connect(closeEvent)
    widget.show()
    bars = [widget.bar_0,
            widget.bar_1,
            widget.bar_2]


    widget.thread={}
    widget.startButton.clicked.connect(FCFS)
    widget.startButton_2.clicked.connect(RR)
    widget.closeButton.clicked.connect(closeEvent)
    app.quit()
    sys.exit(app.exec())