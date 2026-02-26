import sys
from time import sleep

import saudo2
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout)

"""
Ventana 1 del programa
"""


class Ventana1(QMainWindow):
    """
    Modifica el texto principal y vacía el valor de la barra donde se introducen datos
    """

    def on_btnSaudo_clicked(self):
        nome = self.txtSaudo.text()
        if self.chkOculto.isChecked():
            nome = self.nomeOculto  # crea una variable nome con formato de texto
        if self.txtSaudo.text() != "":  # si es nulo el valor introducido
            if self.txtSaudo.text().isdigit():  # o es un número
                self.txtSaudo.clear()  # muestra un error
                self.lblEtiqueta.setText("Nome non permitido")
            else:
                self.txtSaudo.clear()  # Si no muestra un texto con el nombre añadido
                # self.lblEtiqueta.setText("Ola "+ nome + " encantado/a de coñecerte")
                self.lblEtiqueta.setText(nome)
                self.nomeOculto = ''
                self.txtSaudo.setText('')

    """
    Permite cambiar de ventana
    """

    def cambio_ventana(self):
        if self.ventana_secundaria is None:  # si la referencia a la otra ventana  es nula
            self.ventana_secundaria = saudo2.Ventana2(self)  # crea una referencia a la otra ventana
        self.hide()  # se oculta la ventana 1
        self.ventana_secundaria.show()  # muestra la ventana 2

    """
    MUDADO A on_chk_mayusculas_toogled
    Se ejecuta cuando se presiona el botón mayúsculas
    Transforma la etiqueta a mayúsculas

    def boton_mayusculas_presionado(self):
        if self.btnMayusculas.isChecked(): # Si está seleccionado el botón de mayúsculas
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper()) # Transforma el texto en mayúscula
            self.mayusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower()) # Transforma el texto en minúscula
            self.mayusculas = False
    """

    """
    De pendiendo si es o no mayúscula permite escribir SOLO en mayúscula o SOLO en minúscula
    """

    def on_btnSaudo_text_change(self):
        if self.mayusculas:
            self.txtSaudo.setText(self.txtSaudo.text().upper())
        else:
            self.txtSaudo.setText(self.txtSaudo.text().lower())

        nome = self.txtSaudo.text()  # Instancia del texto
        if self.chkOculto.isChecked():
            for i, caracteres in enumerate(nome):  # Recorre cada char de la palabra
                if caracteres != "*":  # Cuando uno de los chars es diferente a "*"
                    if len(self.nomeOculto) == i:  # Si coincide lon el tamaño del nombre oculto
                        self.nomeOculto = self.nomeOculto + caracteres  # Le da al nombre oculto el character del texto
                        break
                    else:
                        self.nomeOculto = self.nomeOculto[:i] + caracteres + self.nomeOculto[i + 1:]
            self.txtSaudo.setText('*' * len(self.nomeOculto))

    """
    Es lo mismo que el método mudado pero ahora en vez de un botón normal es un check
    """

    def on_chk_mayusculas_toogled(self):
        if self.chkMaiusculas.isChecked():  # Si está seleccionado el botón de mayúsculas
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper())  # Transforma el texto en mayúscula
            self.txtSaudo.setText(self.txtSaudo.text().upper())
            self.mayusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower())  # Transforma el texto en minúscula
            self.txtSaudo.setText(self.txtSaudo.text().lower())
            self.mayusculas = False

    """
    Para modificar el texto cuando se selecciones el checked ocultar
    """

    def on_ocultar_toggled(self):
        if self.chkOculto.isChecked():
            self.nomeOculto = self.txtSaudo.text()
            self.txtSaudo.setText('*' * len(self.nomeOculto))
        else:
            self.txtSaudo.setText(self.nomeOculto)
            self.nomeOculto = ''

    """
    Define la estructura de la ventana
    """

    def __init__(self):
        super().__init__()

        # Referencias
        self.nomeOculto = ""
        self.mensaje_guardado = None
        self.ventana_secundaria = None  # Referencia para usar en "cambio_ventana"

        # Configuración de tamaño y título de esta ventana
        self.setWindowTitle("Ventana 1")  # Título de la ventana
        self.setMinimumSize(500, 300)  # Tamaño de la ventana

        # Configuración del label inicial
        self.lblEtiqueta = QLabel("OLA A TODOS!")  # Primer label, cambia cuando este se modifica
        fonte = self.lblEtiqueta.font()  # Administrar la fuente de letra
        fonte.setPointSize(30)  # Tamaño de la letra
        self.lblEtiqueta.setFont(fonte)  # Proporciona a self ese tamaño de letra
        self.lblEtiqueta.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignHCenter)  # Ajustar el texto, centrarlo
        self.lblEtiqueta.setText("OLA A TODOS E TODAS!")  # Muestra un texto

        # Metodo para la introducción de texto por una barra
        self.txtSaudo = QLineEdit()

        # Configuración de la barra de introducción de datos
        self.txtSaudo.setPlaceholderText("Introduce un texto")  # Texto que muestra la barra de introducción de texto
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)
        self.txtSaudo.textChanged.connect(self.on_btnSaudo_text_change)

        # Configuración del botón de saudo
        btnSaudo = QPushButton("Saudo")  # Crea un botón con ese nombre
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)  # Crea una conexión con la función "on_btnSaudo_clicked"

        # Configuración del botón de cambiar ventana
        btnCambio = QPushButton("Cambiar")  # Botón para cambiar de escena
        btnCambio.clicked.connect(self.cambio_ventana)  # Crea una conexión con la función "cambio_ventana"

        """
        MUDAMOS ESTE BOTON POR chkMaiusculas
        # Configuración del botón de mayúsculas
        self.btnMayusculas = QPushButton("Mayúsculas")
        self.btnMayusculas.setCheckable(True) # le añadimos un self para verificar su estado en otros métodos
        self.btnMayusculas.setChecked(True)
        self.btnMayusculas.toggled.connect(self.boton_mayusculas_presionado)
        self.mayusculas = True
        """

        # Para ordenar los bloques de manera horizontal
        caixaH = QHBoxLayout()

        # Configuración del check de mayúsculas
        # En vez de ser un botón como el anterior ( el mudado ) es un recuadro de check
        self.chkMaiusculas = QCheckBox("MAYÚSCULAS")
        self.chkMaiusculas.setChecked(True)  # Aparece de principio seleccionado
        self.chkMaiusculas.toggled.connect(self.on_chk_mayusculas_toogled)
        self.mayusculas = True

        self.chkOculto = QCheckBox("Ocultar")
        self.chkOculto.setChecked(False)
        self.chkOculto.toggled.connect(self.on_ocultar_toggled)

        # Añade al contenedor horizontal
        caixaH.addWidget(self.chkMaiusculas)
        caixaH.addWidget(self.chkOculto)

        # Almacenar el contenido de botones, labels , etc
        caixaV = QVBoxLayout()

        # Añade a la ventana los elementos anteriores
        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)
        caixaV.addWidget(btnCambio)
        # caixaV.addWidget(self.btnMayusculas) # Metodo mudado
        caixaV.addLayout(caixaH)

        # Almacena todos los caixaV
        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        # Muestra la ventana
        self.show()


"""
Ejecuta la ventana
"""
if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    fiestra = Ventana1()
    aplication.exec()