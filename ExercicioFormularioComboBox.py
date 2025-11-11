import sys
from modeloTaboa import ModeloTaboa
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLabel, QListView, QPushButton, QLineEdit, \
    QVBoxLayout, QComboBox, QTextEdit, QRadioButton, QButtonGroup, QTableView, QTabWidget


class ExemploInterfaceComboBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con ComboBox")

        datos = [['Nome', 'DNI', 'Xénero', 'Falecido'],
                 ["Ana", "3456J", "Muller", False],
                 ["Pepe", "9876T", "Home", True]]

        maia = QGridLayout()

        self.nome_dni = [['Ana', 'Pepe', 'Juan'],['3333R', '4444J', '5555E']]


        caixaV1 =QVBoxLayout()
        maia.addLayout(caixaV1, 0,0,1,1)
        grupo1 = QButtonGroup(self)
        grupo1.setExclusive(True)
        grupo2 = QButtonGroup(self)
        grupo2.setExclusive(True)
        rbtBoton1 = QRadioButton("Boton1", self)
        rbtBoton2 = QRadioButton("Boton2", self)
        rbtBoton3 = QRadioButton("Boton3", self)
        rbtBoton4 = QRadioButton("Boton4", self)
        grupo1.addButton(rbtBoton1)
        grupo1.addButton(rbtBoton2)
        grupo2.addButton(rbtBoton3)
        grupo2.addButton(rbtBoton4)

        caixaV1.addWidget(rbtBoton1)
        caixaV1.addWidget(rbtBoton2)
        caixaV1.addWidget(rbtBoton3)
        caixaV1.addWidget(rbtBoton4)

        clasificador = QTabWidget()
        clasificador.setTabPosition(QTabWidget.TabPosition.North)

        maia.addWidget(clasificador, 0, 1, 1, 1)
        self.tvwTaboa = QTableView()
        self.tvwTaboa.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.modelo = ModeloTaboa(datos)
        self.tvwTaboa.setModel(self.modelo)
        self.seleccion = self.tvwTaboa.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_tvwTaboa_selectionChanged)
        clasificador.addTab(self.tvwTaboa, "Taboa")
        txeOutroCadroTexto = QTextEdit()
        clasificador.addTab(txeOutroCadroTexto, "Cadro texto")

        caixaV2 = QVBoxLayout()
        txtCadro1 = QLineEdit()
        txtCadro2 = QLineEdit()
        self.cmbComboBox = QComboBox()
        self.cmbComboBox.addItems(self.nome_dni[0])
        self.cmbComboBox.currentIndexChanged.connect (self.on_cmbComboBox_currentIndexChanged)
        self.cmbComboBox.currentTextChanged.connect(self.on_cmbComboBox_currentTextChanged)
        caixaV2.addWidget(txtCadro1)
        caixaV2.addWidget(txtCadro2)
        caixaV2.addWidget(self.cmbComboBox)
        maia.addLayout(caixaV2,1,0,1,1)
        self.txeAreaTexto = QTextEdit()
        maia.addWidget(self.txeAreaTexto,1,1,1,1)

        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)
        self.show()

    def on_cmbComboBox_currentIndexChanged(self, indice):
        print(self.cmbComboBox.currentText())
        self.txeAreaTexto.setPlainText("Seleccionaches o usuario " + self.cmbComboBox.itemText(indice) + " con DNI: " + self.nome_dni[1][indice])

    def on_cmbComboBox_currentTextChanged(self, texto):
        print("O combo ten seleccionado o texto: " + texto)

    def on_tvwTaboa_selectionChanged(self):
        indice = self.tvwTaboa.selectedIndexes()
        if indice is not None:
            print(self.modelo.taboa[indice[0].row()][indice[0].column()])
            self.txeAreaTexto.setPlainText(self.modelo.taboa[indice[0].row()][indice[0].column()])
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ExemploInterfaceComboBox()
    aplicacion.exec()