# This Python file uses the following encoding: utf-8
#import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Users\aleja\Desktop\qt weas\actividad_3\form.ui", self)
        #self.ui = MainWindow()
        #self.ui.setupUi(self)
