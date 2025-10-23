import sys

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QLabel, QPushButton, QWidget


class SegundaFiestra (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi segunda ventana")
        self.setMinimumSize(400, 300)

        caixa = QVBoxLayout()

        self.lblEtiqueta = QLabel("Ola")
        self.lblEtiqueta.setText("Esta es la segunda ventana")

        btnSaudo = QPushButton("Abrir la primera ventana")
        btnSaudo.clicked.connect(self.abrirventanapadre)

        caixa.addWidget(self.lblEtiqueta)
        caixa.addWidget(btnSaudo)

        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()

    def abrirventanapadre(self):
        self.hide()
        from saudoQT import NosaPrimeiraFiestra
        self.vp = NosaPrimeiraFiestra()
        self.vp.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SegundaFiestra()
    sys.exit(app.exec())