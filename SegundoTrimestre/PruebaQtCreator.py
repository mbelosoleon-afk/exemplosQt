import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUi

class MinhaAplicacion:
    def __init__(self):
        self.aplicacion = QApplication(sys.argv)

        self.fiestra = loadUi("UnhaFiestra/form.ui")
        self.txtApelido = self.fiestra.txtApelido
        self.cmbNumeroCliente = self.fiestra.cmbNumeroCliente
        self.cmbNumeroCliente.insertItems(0,"1","2","3","4","5")
        self.btnEngadir = self.fiestra.btnEngadir
        self.btnEngadir.pressed.connect(self.on_btnEngadir_presed)

        self.fiestra.show()

    def run(self):
        sys.exit(self.aplicacion.exec())

    def on_btnEngadir_presed(self):
        numCliente = self.cmbNumeroCliente.currentText()
        self.txtApelido.set_text("O número do cliente é: " + numCliente)

if __name__ == "__main__":
    apli = MinhaAplicacion()
    apli.aplicacion