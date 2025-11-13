import sys
from mimetypes import inited

from modeloTaboa import ModeloTaboa
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QListWidget, QComboBox, QTextEdit, QGridLayout, QRadioButton,
                             QButtonGroup, QTableView, QTableWidget, QTabWidget)

"""
Aprendiendo a usar el ComboBox en Python Qt
"""
class Combo(QMainWindow):
    """
    Metodo principal del programa
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo combobox QT")
        maia = QGridLayout() # Grid para colocar ordenadamente los layout

        # Valores para crear una tabla
        datos = [['Nome','DNI', 'Xenero','Falecido'],
                 ['Ana','234574Y', 'Muller', False],
                 ['Paco','131313R', 'Home', True  ]]

        self.nome_dni = [['Ana','Pepe','Juan'],['33333R','222222W','111111J']]

        caixaV = QVBoxLayout() # Sirve para crear cada una de las cajas que tienen sus diferentes funcionalidades


        caixaV2 = QVBoxLayout()
        # Crea 4 Radio Buttons
        # Tenemos que añadirle self a cada uno para que funcionen los grupos de los botones
        rbtBoton1 = QRadioButton("Botón1",self)
        rbtBoton2 = QRadioButton("Botón2",self)
        rbtBoton3 = QRadioButton("Botón3",self)
        rbtBoton4 = QRadioButton("Botón4",self)

        # Crea 2 grupos para administrar el orden de los botones
        grupo1 = QButtonGroup(self)
        grupo2 = QButtonGroup(self)
        # Para permitir que se conecten
        grupo1.setExclusive(True)
        grupo2.setExclusive(True)

        # Añade los botones a los grupos
        grupo1.addButton(rbtBoton1)
        grupo1.addButton(rbtBoton2)
        grupo2.addButton(rbtBoton3)
        grupo2.addButton(rbtBoton4)



        txtCadro1 = QLineEdit() # Bloque donde podemos escribir texto
        txtCadro2 = QLineEdit() # Bloque donde podemos escribir texto

        self.cmbComboBox = QComboBox() # Lista desplegable
        #self.cmbComboBox.addItems(("hola","que","tal","estas")) # Añade estos texto al comboBox, OJO ponerlos entre paréntesis porque .addItems pide tuples no strings
        self.cmbComboBox.addItems(self.nome_dni[0]) # Otra forma de hacerlo con una lista de tuples
        self.cmbComboBox.currentIndexChanged.connect(self.on_cmbComboBox_currentIndexChanged) # Que ocurre cuando seleccionamos un objeto del comboBox
        self.cmbComboBox.currentTextChanged.connect(self.on_cmbComboBox_currentTextChanged)

        # Añade los 4 Radio Buttons
        caixaV2.addWidget(rbtBoton1)
        caixaV2.addWidget(rbtBoton2)
        caixaV2.addWidget(rbtBoton3)
        caixaV2.addWidget(rbtBoton4)
        maia.addLayout(caixaV2,0,0,1,1)

        # Crea una tabla aplicando el modelo de la clase ModeloTaboa, y le pasamos los datos creados
        clasificador = QTabWidget()
        clasificador.setTabPosition(QTabWidget.TabPosition.North)

        self.tvwTaboa = QTableView()
        self.modelo = ModeloTaboa(datos)
        self.tvwTaboa.setModel(self.modelo)
        maia.addWidget(clasificador,0,1,1,1)

        clasificador.addTab(self.tvwTaboa, "Taboa")
        txeOutroCadroTexto = QTextEdit()
        clasificador.addTab(txeOutroCadroTexto, "Cadro de texto")

        caixaV.addWidget(txtCadro1)  # Añade en el primer cuadro, tanto el texto 1 el 2 y el desplegable
        caixaV.addWidget(txtCadro2) # Añade el segundo cuadro de texto
        caixaV.addWidget(self.cmbComboBox) # Añade la comboBox

        maia.addLayout(caixaV,1,0,1,1) # Como caixaV es layout tiene que ser addLayout

        self.txeAreaTexto = QTextEdit() # Area donde podremos introducir texto
        maia.addWidget(self.txeAreaTexto,1,1,1,1) # Aquí como txtArea no es un layout, se le añade con widget

        # MOSTRAR LO DISEÑADO ANTERIORMENTE(OBLIGATORIO)
        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()


    """
    Lo que ocurre cuando seleccionamos una opción del ComboBox
    Al seleccionar una opción mostrará tanto el nombre del usuario como su DNI
    indice: indice de cada una de las opciones del comboBox
    """
    def on_cmbComboBox_currentIndexChanged(self, indice):
        print(self.cmbComboBox.itemText(indice)) # Muestra por consola la opción escogida del comboBox
        self.txeAreaTexto.setPlainText("Has seleccionado el usuario: "+ self.cmbComboBox.itemText(indice)+ " con el dni: "+ self.nome_dni[1][indice] ) # Muestra en el bloque de texto el texto seleccionado del comboBox

    """
    Muestra el usuario seleccionado
    texto: recoge el valor del string del indice seleccionado del comboBox
    """
    def on_cmbComboBox_currentTextChanged(self, texto):
        print("El combo tiene seleccionado el elemento: "+ texto)

# EJECUTA LA VENTANA(OBLIGATORIO)
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Combo()
    aplicacion.exec()