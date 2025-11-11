import sys
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage

doc = QImage ('documento.png')
fol = QImage ('follaCalculo.png')

class ModeloFollas (QAbstractListModel):
    def __init__(self, follas=None):
        super().__init__()
        self.follas = follas or []

    def data (self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            texto,_ = self.follas [indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            _,tipo = self.follas [indice.row()]
            if tipo =="F":
                return fol
            if tipo == "D":
                return doc

    def rowCount(self, indice):
        return len (self.follas)