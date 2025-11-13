import sys
from mimetypes import inited

import modeloLista
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QGridLayout, QListWidget)

class ListaIntercambiable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primera ventana con QT")
        maia = QGridLayout()

        listaFollas = [["Follas 1","F"],["Documento 1","D"], ["Follas3","F"]] # Crea las entradas a escribir, utilizadas por el model
        self.modeloListaVisibles = modeloLista.ModeloFollas(listaFollas) # Aplica el model en base a los datos del array
        self.modeloListaOcultos = modeloLista.ModeloFollas()

        lblFollasVisibles = QLabel("Follas Visibles")
        lblFollasOcultas = QLabel("Follas Ocultas")

        btnMOstrar = QPushButton("<<Mostrar")
        btnMOstrar.clicked.connect(self.on_btnMostrar_clicked)
        btnOcultar = QPushButton("Ocultar>>")
        btnOcultar.clicked.connect(self.on_btnOcultar_clicked)
        btnCerrar = QPushButton("Cerrar")
        btnCerrar.clicked.connect(self.on_btnCerrar_clicked)
        btnCerrar.setFixedSize(60,30)

        self.lstOculta = QListView()
        self.lstVisible = QListView()

        self.lstVisible.setModel(self.modeloListaVisibles) # Permite añadir los objetos de oculto a visible
        self.lstOculta.setModel(self.modeloListaOcultos) # igual que el anterior pero al reves

        maia.addWidget(lblFollasVisibles)
        maia.addWidget(lblFollasOcultas,0,2,1,1)
        maia.addWidget(self.lstVisible,1,0,5,1)
        maia.addWidget(self.lstOculta,1,2,5,1)
        maia.addWidget(btnOcultar,1,1,1,1)
        maia.addWidget(btnMOstrar,3,1,1,1)
        maia.addWidget(btnCerrar,7,2,1,1, alignment=Qt.AlignmentFlag.AlignRight)

        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()

    def on_btnMostrar_clicked(self):
        indices = self.lstOculta.selectedIndexes() # array de datos de la lista oculta
        if indices: # Como la selección es unica el valor seleccionado siempre devuelve indice 0
            self.modeloListaVisibles.follas.append(self.modeloListaOcultos.follas[indices[0].row()]) # Entonces añadimos el valor de indice[0] a una lista de los visibles, para mostarlo  Visibles
            del  self.modeloListaOcultos.follas[indices[0].row()] # Borramos la selección de oculto
            # para actualizar los cambios realizados
            self.modeloListaVisibles.layoutChanged.emit()
            self.modeloListaOcultos.layoutChanged.emit()

            self.lstOculta.clearSelection() # Elimina la selección (Importante)

    def on_btnOcultar_clicked(self):
        indices = self.lstVisible.selectedIndexes()  # array de datos de la lista oculta
        if indices:  # Como la selección es unica el valor seleccionado siempre devuelve indice 0
            self.modeloListaOcultos.follas.append(self.modeloListaVisibles.follas[indices[0].row()])  # Entonces añadimos el valor de i
            # ndice[0] a una lista de los visibles, para mostarlo  Visibles
            del self.modeloListaVisibles.follas[indices[0].row()]  # Borramos la selección de oculto
            # para actualizar los cambios realizados
            self.modeloListaVisibles.layoutChanged.emit()
            self.modeloListaOcultos.layoutChanged.emit()

            self.lstVisible.clearSelection()  # Elimina la selección (Importante)

    def on_btnCerrar_clicked(self):
        self.close()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = ListaIntercambiable()
    aplicacion.exec()