from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget

class CaixaCor (QWidget):
    def __init__(self, cor):
        super().__init__()
        self.setAutoFillBackground(True) #Autorrellena el background
        paleta = self.palette() #Creamos un objeto paleta para rellenar con un color
        paleta.setColor(QPalette.ColorRole.Window, QColor(cor)) #Le proporcionamos a paleta un color específico
        self.setPalette(paleta) #Y se lo asignamos
