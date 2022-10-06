from ipaddress import collapse_addresses
import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5 import QtTest
from threadClass import *

CANT_PROCESOS = 6

def initColaProcesos(ColaProcesos):
    names=["photoshop", "edge", "ableton", "vs-code", "krita", "qemu"]
    ramUsage=[2, 1, 2, 1, 1, 1]
    colors=["purple", "gree", "pink", "blue", "yellow", "cyan"]

    for i in range(CANT_PROCESOS):
        Proceso = {'name': names[i], 'status': "init", 'index':i ,'ramUse':ramUsage[i], 'memoryLocation':0, 'color':colors[i]}
        ColaProcesos.append(Proceso)

def producers ():
    cont=0
    index=0
    for process in processes:
        QtTest.QTest.qWait(1000)
        process.setText(ColaProcesos[cont]['name'])
        use=ColaProcesos[cont]['ramUse']
        
        ColaProcesos[cont]['memoryLocation'] = index

        while(use>0):
            ram[index].setStyleSheet(f"background-color: {ColaProcesos[cont]['color']}")
            
            index=index+1
            use=use-1
        colorProcess[cont].setStyleSheet(f"background-color: {ColaProcesos[cont]['color']}")
        cont=cont+1
        

def setColor():
    for i in ram:
        i.setStyleSheet("background-color: gray")

def cleanMemory(index, usage):
    inicio=index
    fin=index+usage
    for i in range(inicio, fin):
        ram[i].setStyleSheet("background-color: gray")

def FCFS():
    #restartBars()   #Reinicia las barras por si se vuelve a llamar

    #widget.startButton.setEnabled(False)    #Desactiva boton

    while (len(ColaProcesos) > 0):  #Mientras no se carguen todas las barras
        QtTest.QTest.qWait(465) #Espera lo que espera la barra de carga o se bugea pq trabajan en contextos diferentes y se desincronizan
        app.processEvents() #funcion pa que no se freezie la GUI con el while

        index = ColaProcesos[0]['index']   #Toma el primer elemento de la cola ordenada por prioridades

        if(widget.semStatus == VERDE):
            x = 'VERDEEEEE'
        else:
            x = 'ROJOOOOOO'

        print(x, 'Thread: ', index, "Status: ", ColaProcesos[0]['status'], 'value: ', widget.bar_0.value())
        
        if(ColaProcesos[0]['status'] == "finished" and widget.semStatus == VERDE):   #Si el proceso esta al 100% y el semaforo esta en verde se kickea de la cola y se detiene
            cleanMemory(ColaProcesos[0]['memoryLocation'], ColaProcesos[0]['ramUse'])
            ColaProcesos.pop(0)
            widget.bar_0.setValue(0)
        
        elif(widget.bar_0.value() == 100):   #Si el proceso esta al 100% y el semaforo esta en verde se kickea de la cola y se detiene
            stopThread(widget, index)
            ColaProcesos[0]['status'] = "finished"

        elif(ColaProcesos[0]['status'] == "init" and widget.semStatus == VERDE):   #Si el proceso no esta iniciada y el semaforo esta en verde ps lo inicia (?)
            widget.actual_process.setStyleSheet(f"background-color: {ColaProcesos[0]['color']}")
            startThread(widget, index)
            ColaProcesos[0]['status'] = "running"
        
        elif(ColaProcesos[0]['status'] == "running"):   #Si el proceso se esta corriendo, pues sigue corriendo y el semaforo se mantiene en rojo
            #print("jalando")
            pass
        
    #widget.startButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    #arreglos para poder manejar mejor los slots de memoria y el display del nombre de los procesos
    processes=[widget.process_0, widget.process_1, widget.process_2, widget.process_3, widget.process_4, widget.process_5]
    colorProcess=[widget.color_0, widget.color_1, widget.color_2, widget.color_3, widget.color_4, widget.color_5]
    ram=[widget.slot_0, widget.slot_1, widget.slot_2, widget.slot_3, widget.slot_4, widget.slot_5, widget.slot_6, widget.slot_7]

    ColaProcesos = []
    initColaProcesos(ColaProcesos)

    setColor()  #inicializa los colores de la ram para que se ponga en gris para dar a entender que no está en uso
    widget.light_status.setStyleSheet("background-color: red")
    widget.show()
    producers()
    widget.thread={}
    FCFS()
    sys.exit(app.exec())
