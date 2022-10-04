import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5 import QtTest
from threadClass import *

def producers ():
    cont=0
    index=0
    for i in process:
        QtTest.QTest.qWait(1000)
        i.setText(names[cont])
        use=ramUsage[cont]
        
        while(use>0):
            ram[index].setStyleSheet(f"background-color: {colors[cont]}")
            
            index=index+1
            use=use-1
        colorProcess[cont].setStyleSheet(f"background-color: {colors[cont]}")
        cont=cont+1
        

def setColor():
    for i in ram:
        i.setStyleSheet("background-color: gray")

def FCFS():
    #restartBars()   #Reinicia las barras por si se vuelve a llamar
    
    priorityQueue=sorted(ColaProcesos, key=lambda d:d['priority'])  #Una vez creada la cola en desorden, se ordena segun la prioridad de los procesos

    for i in range(CantProcesos):   #Se imprime el orden en el que se ejecutaran
        print(priorityQueue[i])

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
        
    #widget.startButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    #arreglos para poder manejar mejor los slots de memoria y el display del nombre de los procesos
    process=[widget.process_0, widget.process_1, widget.process_2, widget.process_3, widget.process_4, widget.process_5]
    colorProcess=[widget.color_0, widget.color_1, widget.color_2, widget.color_3, widget.color_4, widget.color_5]
    ram=[widget.slot_0, widget.slot_1, widget.slot_2, widget.slot_3, widget.slot_4, widget.slot_5, widget.slot_6, widget.slot_7]
    #inicializa los colores de la ram para que se ponga en gris para dar a entender que no está en uso
    names=["photoshop", "edge", "ableton", "vs-code", "krita", "qemu"]
    ramUsage=[2, 1, 2, 1, 1, 1]
    colors=["purple", "gree", "pink", "blue", "yellow", "cyan"]
    setColor()
    widget.light_status.setStyleSheet("background-color: red")
    widget.show()
    producers()
    widget.thread={}
    sys.exit(app.exec())
