import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from threadClass import *


CantProcesos = 5

def restartBars():
    for Bar in bars:
        Bar.setValue(0)

#FCFS ta hecho con una cola de indices(supestamente) y con barras (pero igual se puede usar los hilos directamente)
def Prioridades():
    restartBars()   #Reinicia las barras por si se vuelve a llamar
    widget.startButton.setEnabled(False)    #Desactiva boton

    while (len(priorityQueue) > 0):  #Mientras no se carguen todas las barras
        QtTest.QTest.qWait(500) #Espera lo que espera la barra de carga o se bugea pq trabajan en contextos diferentes y se desincronizan
        app.processEvents() #funcion pa que no se freezie la GUI con el while

        index = priorityQueue[0]['index']   #Toma el primer elemento de la cola ordenada por prioridades
        print('Thread: ', index, "Status: ", priorityQueue[0]['status'], 'value: ', bars[index].value())
        
        if(bars[index].value()==100):   #Si el proceso esta al 100% se kickea de la cola y se detiene
            stopThread(widget, index)
            priorityQueue[0]['status'] = "finished"
            priorityQueue.pop(0)

        elif(priorityQueue[0]['status'] == "init"):   #Si el proceso no esta iniciada ps lo inicia (?)
            startThread(widget, index)
            priorityQueue[0]['status'] = "running"
        
        elif(priorityQueue[0]['status'] == "running"):   #Si el proceso se esta corriendo, pues sigue corriendo
            #print("jalando")
            pass
        
    widget.startButton.setEnabled(True)


def initView(): #Inicializa una lista con los procesos en desorden e inicia la vista
    for i in range(CantProcesos):
        priority = randint(0,2)
        proceso={"index": i, "status": "init", "priority": priority}
        ColaProcesos.append(proceso)

        priorLabels[i].setText(str(priority))


def closeEvent():   #Detiene todos los hilos y subprocesos al dar click en CERRAR
    for i in widget.thread:
        widget.thread[i].stop()

    app.quit()
    widget.close()
    app.exit()
    sys.exit()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    widget.show()
    bars = [widget.bar_0,
            widget.bar_1,
            widget.bar_2, 
            widget.bar_3,
            widget.bar_4]

    priorLabels = [
        widget.prior_0,
        widget.prior_1,
        widget.prior_2,
        widget.prior_3,
        widget.prior_4]

    ColaProcesos=[]
    widget.thread={}

    initView()
    priorityQueue=sorted(ColaProcesos, key=lambda d:d['priority'])  #Una vez creada la cola en desorden, se ordena segun la prioridad de los procesos

    for i in range(CantProcesos):   #Se imprime el orden en el que se ejecutaran
        print(priorityQueue[i])

    widget.startButton.clicked.connect(Prioridades)
    widget.closeButton.clicked.connect(closeEvent)
    app.quit()
    sys.exit(app.exec())