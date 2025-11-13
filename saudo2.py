import sys
from  PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget)

"""
Muestra una segunda ventana
"""
class Ventana2(QMainWindow):

    """
    Permite el cambio de escena
    """
    def on_cambio(self):
        if self.ventana_padre is not None:
            #self.hide() # Oculta la ventana actual
            self.primera_ventana = self.ventana_padre # Crea una referencia a la otra ventana
            self.primera_ventana.show() # Muestra la nueva ventana
            self.destroy() # elimina esta ventana para ahorrar espacio en memoria al tener dos ventanas abiertas
            print("Ventana destruida")

    """
    Define la estructura de la ventana
    """
    def __init__(self , ventana_padre):
        super().__init__() # Llama al super

        self.primera_ventana = None # Crea una referencia para usarla en "on_cambio"
        self.ventana_padre = ventana_padre # Referencia a la ventana padre

        self.setWindowTitle("A miña segunda fiestra con QT") # Titulo
        self.setMinimumSize(500,300) # Tamaño de la ventana

        self.label = QLabel("Hola") # Lo primero que se muestra si no se modifica
        self.label.setText("Pepsi cola") # Se modifica lo anterior y se cambia
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignHCenter) # Centrar el texto

        # Botón para regresar a la ventana anterior
        boton_cambio_ventana  = QPushButton("Anterior")
        boton_cambio_ventana.clicked.connect(self.on_cambio) # Conectarse a la función que permitirá el cambio de escena

        cajaV = QVBoxLayout() # Almacenar

        cajaV.addWidget(self.label) # Añade el el label a la ventana
        cajaV.addWidget(boton_cambio_ventana)

        container = QWidget() # Almacenar

        container.setLayout(cajaV)
        self.setCentralWidget(container)

        self.show() # Muestra la ventana actual

"""
Ejecuta todo el código
"""
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = Ventana2(None) # Es none porque no tiene ventana padre, se anida ella
    aplicacion.exec()