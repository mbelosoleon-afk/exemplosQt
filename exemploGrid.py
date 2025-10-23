import sys
import CaixaCor
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget, QGridLayout


class ExemploBox (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con QGridLayout")

        maia = QGridLayout()
        maia.addWidget(CaixaCor.CaixaCor("red"))
        maia.addWidget(CaixaCor.CaixaCor("blue"), 0,1,1,2)
        maia.addWidget(CaixaCor.CaixaCor("green"),1,0,2,1)
        maia.addWidget(CaixaCor.CaixaCor("pink"),1,1,1,2)
        maia.addWidget(CaixaCor.CaixaCor("orange"),2,1,1,1)
        maia.addWidget(CaixaCor.CaixaCor("yellow"),2,2,1,1)


        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)

        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ExemploBox()
    aplicacion.exec()