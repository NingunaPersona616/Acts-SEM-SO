from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"form.ui", self)

    def taskManager(self, counter):#processFunction recibira como parametro un contador que sera el que se cargará en la barra de progreso
            cnt=counter#lo igualamos a una variable local
            self.bar_0.setValue(cnt)
