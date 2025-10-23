import sys
from distutils.core import setup_keywords
from os import setegid

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QBoxLayout, QVBoxLayout,
                             QWidget, QCheckBox, QHBoxLayout)



class NosaPrimeiraFiestra (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A miña primeira fiestra con QT")
        self.setMinimumSize(500,300)
        caixaV = QVBoxLayout()

        self.nomeOculto = ""

        self.lblEtiqueta = QLabel("OLA A TODOS!")
        self.lblEtiqueta.setText("Ola a todos e todas")

        self.txtSaudo = QLineEdit()
        self.txtSaudo.setPlaceholderText("Introduce tu nombre")
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)
        self.txtSaudo.textChanged.connect(self.on_btnSaudo_textChanged)

        btnSaudo = QPushButton ("Saúdo")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)

        """Mudamos btnMaiusculas por chkMaiusculas
        self.btnMaiusculas = QPushButton("Maiusculas")
        self.btnMaiusculas.setCheckable(True)
        self.btnMaiusculas.setChecked(True)
        self.btnMaiusculas.toggled.connect(self.on_btnMaiusculas_toggled)
        self.maiusculas = True
        """
        caixaH = QHBoxLayout()

        self.chkMaiusculas = QCheckBox("Maiusculas")
        self.chkMaiusculas.setChecked(True)
        self.chkMaiusculas.toggled.connect(self.on_chkMaiusculas_toggled)
        self.maiusculas = True

        self.chkOculto = QCheckBox("Oculto")
        caixaH.addWidget(self.chkMaiusculas)
        caixaH.addWidget(self.chkOculto)
        self.chkOculto.toggled.connect(self.on_chkOculto_toggled)

        btn2 = QPushButton ("Abrir la segunda ventana")
        btn2.clicked.connect(self.abrirVentana2)
        caixaV.addWidget(btn2)

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)
        #caixaV.addWidget(self.btnMaiusculas)
        #caixaV.addWidget(self.chkMaiusculas)
        caixaV.addLayout(caixaH)

        container = QWidget()
        container.setLayout(caixaV)

        self.setCentralWidget(container)
        self.show()

    def on_btnSaudo_clicked (self):
        if self.chkOculto.isChecked():
            nome = self.nomeOculto
            nome.strip()
        if len(nome)!=0 :
            self.txtSaudo.clear()
            #self.txtSaudo.setText("")
            self.lblEtiqueta.setText("Hola " + nome + " encantando de conocerte")
        else:
            self.lblEtiqueta.setText("Introduce tu nombre para recibir un saludo personalizado")
        self.on_chkMaiusculas_toggled()
    def abrirVentana2(self):
        self.hide()
        from saudo2 import SegundaFiestra
        self.a =  SegundaFiestra()
        self.a.show

    def on_chkMaiusculas_toggled (self):
        if self.chkMaiusculas.isChecked():
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper())
            self.maiusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower())
            self.maiusculas = False

    def on_chkOculto_toggled(self):
        if self.chkOculto.isChecked():
            self.nomeOculto = self.txtSaudo.text()
            self.txtSaudo.setText('*' * len(self.nomeOculto))
        else:
            self.txtSaudo.setText(self.nomeOculto)
            self.nomeOculto = ''

    def on_btnSaudo_textChanged(self):
        if self.maiusculas:
            self.txtSaudo.setText(self.txtSaudo.text().upper())
        else:
            self.txtSaudo.setText(self.txtSaudo.text().lower())
        nome = self.txtSaudo.text()
        if self.chkOculto.isChecked():
            for i, caracter in enumerate(nome):
                if caracter != '*':
                    if len(self.nomeOculto) == i:
                        self.nomeOculto = self.nomeOculto + caracter
                        break
                    else:
                        self.nomeOculto = self.nomeOculto [:i] + caracter + self.nomeOculto[i:]
            self.txtSaudo.setText('*' * len(self.nomeOculto))
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = NosaPrimeiraFiestra()
    aplicacion.exec()
