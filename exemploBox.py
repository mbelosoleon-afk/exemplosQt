import sys
import CaixaCor
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget

class exemploBox (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con Box")

        caixaH = QHBoxLayout()

        #Bloque 1
        caixaV1 = QVBoxLayout()
        caixaV1.addWidget(CaixaCor.CaixaCor("blue"))
        caixaV1.addWidget(CaixaCor.CaixaCor("green"))
        caixaV1.addWidget(CaixaCor.CaixaCor("red"))
        caixaH.addLayout(caixaV1)

        caixaH.addWidget(CaixaCor.CaixaCor("yellow"))

        #Bloque 2
        caixaV2 = QVBoxLayout()
        caixaV2.addWidget(CaixaCor.CaixaCor("pink"))
        caixaV2.addWidget(CaixaCor.CaixaCor("grey"))
        caixaH.addLayout(caixaV2)

        #Creamos una referencia a un widget y le damos como layout a "CaixaH"
        #De esa manera podremos observar los bloques coloreados
        container = QWidget()
        container.setLayout(caixaH)
        self.setCentralWidget(container)
        #Muestra la ventana
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = exemploBox()
    aplicacion.exec()