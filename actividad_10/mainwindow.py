from pager import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import numpy as np

class MainWindow(QMainWindow):
    split=np.random.permutation(6)[:6].tolist()#proceso dividido
    slots=np.random.permutation(12)[:6].tolist()#posiciones random en la memoria virtual
    cont=0
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"form.ui", self)
    

    def bar(self, counter):#processFunction recibira como parametro un contador que sera el que se cargará en la barra de progreso
        cnt=counter#lo igualamos a una variable local
        index=self.sender().index#cachamos el index del thread para saber que barra llenar haciendo match entre barra e hilo
            #esta funcion será llamada varias veces mediante señales y es la que generará la carga visual de las barras segun el hilo que emita la señal
        if index==0:
                self.bar_0.setValue(cnt)
        if index==1:
                self.bar_1.setValue(cnt)
        if index==2:
                self.bar_2.setValue(cnt)
        if index==3:
                self.bar_3.setValue(cnt)
    
    def nextPage(self, flag):
        index=self.sender().index
        if(self.cont<6):
            if index==0:
                self.fslot_0.setText(f"{self.split[self.cont]}")
                self.page.setText(f"{self.split[self.cont]}")
                self.frame.setText(f"0")
                
            if index==1:
                self.fslot_1.setText(f"{self.split[self.cont]}")
                self.page.setText(f"{self.split[self.cont]}")
                self.frame.setText(f"1")
                
            if index==2:
                self.fslot_2.setText(f"{self.split[self.cont]}")
                self.page.setText(f"{self.split[self.cont]}")
                self.frame.setText(f"2")
                
            if index==3:
                self.fslot_3.setText(f"{self.split[self.cont]}")
                self.page.setText(f"{self.split[self.cont]}")
                self.frame.setText(f"3")
                
            self.cont=self.cont+1
            startThread(self, index)
        else:
            print("ya no hay mas paginas que necesiten entrar a memoria")



# widget.page.setText(f"{vslots[slots[i]].text()}")
#         widget.frame.setText(f"{i}")






