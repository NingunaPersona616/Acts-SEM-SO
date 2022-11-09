from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"form.ui", self)



    def iod(self, counter):
        cnt=counter#lo igualamos a una variable local
        index=self.sender().index#cachamos el index del thread para saber que barra llenar haciendo match entre barra e hilo
            #esta funcion será llamada varias veces mediante señales y es la que generará la carga visual de las barras segun el hilo que emita la señal
        if index==0:
            self.printBar.setValue(cnt)
            if self.printBar.value()==100:
                self.printStatus.setText("se terminó de imprimir")
                self.printButton.setEnabled(True)
                self.slot1.setStyleSheet("background-color: gray")



