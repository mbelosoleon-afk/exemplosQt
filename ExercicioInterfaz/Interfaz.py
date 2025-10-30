import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget, QLabel, QListWidgetItem, \
    QListView, QPushButton


class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()

        #Título de la ventana
        self.setWindowTitle("Exemplo con QListWidget")

        #Ventana actual
        caixaH = QHBoxLayout()

        #Bloque 1
        caixaV1 = QVBoxLayout()
        self.textoBloque1 = QLabel("Hojas visibles")
        self.bloque1 = QListView() #Crea la forma de cada cuadrado
        caixaV1.addWidget(self.textoBloque1)
        caixaV1.addWidget(self.bloque1)
        caixaH.addLayout(caixaV1)

        #Bloque central
        caixaVCentral = QVBoxLayout()
        self.botonOcultar = QPushButton("Ocultar >>")
        self.botonMostrar = QPushButton("<<Mostrar>>")
        caixaVCentral.addWidget(self.botonOcultar)
        caixaVCentral.addWidget(self.botonMostrar)
        caixaH.addLayout(caixaVCentral)

        #Bloque 2
        caixaV2 = QVBoxLayout()
        self.textoBloque2 = QLabel("Hojas ocultas")
        self.bloque2 = QListView()
        self.botonCerrar = QPushButton("Cerrar")
        self.botonCerrar.setFixedSize(200,30)
        caixaV2.addWidget(self.textoBloque2)
        caixaV2.addWidget(self.botonCerrar, alignment= Qt.AlignmentFlag.AlignRight)
        caixaH.addLayout(caixaV2)

        #Creamos una referencia a un widget y le damos como layout a "CaixaH"
        #De esa manera podremos observar los bloques coloreados
        wid = QWidget()
        wid.setLayout(caixaH)
        self.setCentralWidget(wid)

        self.show()



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Interfaz()
    aplicacion.exec()