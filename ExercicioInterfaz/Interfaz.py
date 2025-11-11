import sys
import modeloLista
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLabel, QListView, QPushButton


class ExemploListasIntercambiables(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con QGridLayout")

        maia = QGridLayout()
        listaFollas = [["Folla 1", "F"], ["Documento 1", "D"], ["Folla 3", "F"], ["Folla 4","F"], ["Documento 2", "D"]]
        self.modeloListaVisibles = modeloLista.ModeloFollas(listaFollas)
        self.modeloListaOcultos = modeloLista.ModeloFollas()

        lblFollasVisibles = QLabel("Follas visibles")
        lblFollasOcultas = QLabel("Follas ocultas")
        btnMostrar = QPushButton("<< Mostrar")
        btnMostrar.clicked.connect(self.on_btnMostrar_clicked)
        btnOcultar = QPushButton("Ocultar >>")
        btnOcultar.clicked.connect(self.on_btnOcultar_clicked)
        btnPechar = QPushButton("Pechar")
        btnPechar.clicked.connect(self.close)

        self.lstOcultos = QListView()
        self.lstOcultos.setModel(self.modeloListaOcultos)
        self.lstVisibles = QListView()
        self.lstVisibles.setModel(self.modeloListaVisibles)

        controlInerte = QWidget()
        controlInerte.setMinimumSize(1, 20)

        maia.addWidget(lblFollasVisibles)
        maia.addWidget(lblFollasOcultas, 0, 2, 1, 1)
        maia.addWidget(self.lstVisibles, 1, 0, 5, 1)
        maia.addWidget(self.lstOcultos, 1, 2, 5, 1)
        maia.addWidget(btnOcultar, 1, 1, 1, 1)
        maia.addWidget(btnMostrar, 3, 1, 1, 1)
        maia.addWidget(controlInerte, 7, 2, 1, 1)
        maia.addWidget(btnPechar, 7, 2, 1, 1)

        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)
        self.show()

    def on_btnMostrar_clicked(self):
        indices = self.lstOcultos.selectedIndexes()
        if indices:
            self.modeloListaVisibles.follas.append(self.modeloListaOcultos.follas[indices[0].row()])
            del self.modeloListaOcultos.follas[indices[0].row()]
            self.modeloListaVisibles.layoutChanged.emit()
            self.modeloListaOcultos.layoutChanged.emit()
            self.lstOcultos.clearSelection()

    def on_btnOcultar_clicked(self):
        indices = self.lstVisibles.selectedIndexes()
        if indices:
            self.modeloListaOcultos.follas.append(self.modeloListaVisibles.follas[indices[0].row()])
            del self.modeloListaVisibles.follas[indices[0].row()]
            self.modeloListaVisibles.layoutChanged.emit()
            self.modeloListaOcultos.layoutChanged.emit()
            self.lstVisibles.clearSelection()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ExemploListasIntercambiables()
    aplicacion.exec()