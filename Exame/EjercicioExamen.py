import sys
from mimetypes import inited
from time import sleep

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QPushButton, QComboBox, QLineEdit, QGroupBox, QTextEdit, QWidget, QGridLayout,
                             QHBoxLayout)




class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame grupo A")

        maia = QGridLayout() #Creamos el GridLayout
        self.albaras = [
                    ["1111nm","02/11/2024","1111","Ana","Ruiz"],
                   ["2222io","08/03/2024","2222","Pedro","Diz"],
                   ["3333qw","23/10/2025","3333","Rosa","Sanz"]
        ] #Creamos los datos que vamos a introducir


        gpbCliente = QGroupBox("Albará") #Widget contenedor que se usa para agrupar otros widget
        maia.addWidget(gpbCliente,0,0,3,3) #Añades ese contenedot al Layout principal
        maiaGroup = QGridLayout() #Creas nu layout interno
        gpbCliente.setLayout(maiaGroup) #Establece el maiaGroup como administrador del Layout

        #Creamos los elementos tipo QLabel
        lblNumeroAlbara = QLabel("Número Albará")
        lblDataAlbara = QLabel("Data")
        lblNumeroCliente = QLabel("Número cliente")
        lblNomeCliente = QLabel("Nome Cliente")
        lblApelidosCliente = QLabel("Apelidos")

        #Los metemos en el Grid maiaGroup a través de .addWidget(Widget,fila,columna,row_spawn(cuantas filas ocupa),column_spawn(cuantas columnas ocupa))
        maiaGroup.addWidget(lblNumeroAlbara,0,0,1,1)
        maiaGroup.addWidget(lblNumeroCliente,1,0,1,1)
        maiaGroup.addWidget(lblApelidosCliente,2,0,1,1)
        maiaGroup.addWidget(lblDataAlbara,0,2,1,1)
        maiaGroup.addWidget(lblNomeCliente,1,2,1,1)

        #Creamos los elementos QLineEdit() y el QComboBox. Tenemos q crearlos con el self.
        self.txtDataAlbara = QLineEdit()
        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.cmbNumeroAlbara = QComboBox()
        #En esta línea, hacemos que el comboBox, tenga una acción que definiremos más tarde
        self.cmbNumeroAlbara.currentIndexChanged.connect(self.on_cmbNumeroAlbara_currentIndexChanged)
        #El QComboBox(), debe enseñar solo el primer parámetro de los datos del principio.
        numAlba = []
        for num in self.albaras:
            numAlba.append(num[0])
        self.cmbNumeroAlbara.addItems(numAlba)

        #Ahora metemos estos objetos en el Grid maiaGroup
        maiaGroup.addWidget(self.cmbNumeroAlbara,0,1,1,1)
        maiaGroup.addWidget(self.txtNumeroCliente,1,1,1,1)
        maiaGroup.addWidget(self.txtApelidosCliente,2,1,1,3)
        maiaGroup.addWidget(self.txtDataAlbara,0,3,1,1)
        maiaGroup.addWidget(self.txtNomeCliente,1,3,1,1)

        #Creamos los primeros botones
        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnEditar.clicked.connect(self.on_clicked_editar)
        btnBorrar = QPushButton("Borrar")

        #Los metemos en el Grid maia
        maia.addWidget(btnEngadir,4,0,1,1)
        maia.addWidget(btnEditar,4,1,1,1)
        maia.addWidget(btnBorrar,4,2,1,1)

        #Creamos el cuadro de texto QTextEdit() y lo metemos en el Grid maia
        self.txeCadroTexto = QTextEdit()
        maia.addWidget(self.txeCadroTexto,5,0,3,3)

        #Creamos los siguientes botones y Aceptar lo desabilitamos
        btnAceptar = QPushButton("Aceptar")
        btnAceptar.setEnabled(False)
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.clicked.connect(self.on_btnCancelar_clicked)

        #Metemos esos dos botones en el Grid maia
        maia.addWidget(btnCancelar,8,1,1,1)
        maia.addWidget(btnAceptar,8,2,1,1)

        #Obligatorio para mostrar la interfaz
        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)
        self.show()


    def on_clicked_editar(self):
        print(self.cmbNumeroAlbara.currentText())
        self.txeCadroTexto.append("Numero Albará: " + self.cmbNumeroAlbara.currentText() + ", Numero Cliente: " + self.txtNumeroCliente.text() + ", Apelidos: " + self.txtApelidosCliente.text() + ", Data: " + self.txtDataAlbara.text() + ", Nome Cliente: " + self.txtNomeCliente.text())

    def on_cmbNumeroAlbara_currentIndexChanged(self):
        indice = self.cmbNumeroAlbara.currentIndex()
        if indice is not None:
            contido = self.albaras[indice]
            print(contido)
            self.txtDataAlbara.setText(contido[1])
            self.txtNumeroCliente.setText(contido[2])
            self.txtNomeCliente.setText(contido[3])
            self.txtApelidosCliente.setText(contido[4])

    def on_btnCancelar_clicked(self):
        self.close()

if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()