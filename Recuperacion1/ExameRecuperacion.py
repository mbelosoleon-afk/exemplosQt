import sys
from datetime import datetime
from xmlrpc.client import DateTime

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTabWidget, QCheckBox, QSlider,
                             QTextEdit)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 24-11-2025")
        maia = QGridLayout()

        clasificador = QTabWidget()
        clasificador.setTabPosition(QTabWidget.TabPosition.North)
        maia.addWidget(clasificador,0,1,1,1)

        self.Conf1 = QGroupBox()
        clasificador.addTab(self.Conf1, "Configuración Zoa 1")
        self.Conf2 = QTableView()
        clasificador.addTab(self.Conf2, "Configuración Zoa 2")
        self.txeOutroCadroTexto = QTextEdit()
        clasificador.addTab(self.txeOutroCadroTexto, "Consola")

        self.maia1 = QGridLayout()
        self.Conf1.setLayout(self.maia1)


        self.group = QGroupBox()
        self.maia1.addWidget(self.group,0,0)
        self.maiaGroup = QGridLayout()
        self.group.setLayout(self.maiaGroup)

        lblZoaActivada = QLabel("Zoa activada")
        self.maiaGroup.addWidget(lblZoaActivada,0,0,1,1)

        self.chkZoaActivada = QCheckBox()
        self.maiaGroup.addWidget(self.chkZoaActivada,0,1,1,1)
        self.chkZoaActivada.stateChanged.connect(self.chkZoActivada_escribir)

        lblHoraComezoRego = QLabel("Hora de comezo de rego")
        self.maiaGroup.addWidget(lblHoraComezoRego,1,0,1,1)

        self.txtHoraComezoRego = QLineEdit()
        self.maiaGroup.addWidget(self.txtHoraComezoRego,1,1,1,1)
        self.txtHoraComezoRego.returnPressed.connect(self.on_txtHoraComezoRego_clicked)

        lblDuracionRego = QLabel("Duración rego")
        self.maiaGroup.addWidget(lblDuracionRego,2,0,1,1)

        self.sldDuracionRego = QSlider(Qt.Orientation.Horizontal)
        self.maiaGroup.addWidget(self.sldDuracionRego,2,1,1,1)
        self.sldDuracionRego.setRange(0,600)
        self.sldDuracionRego.sliderReleased.connect(self.sldDuracionRego_rango)

        self.group1 = QGroupBox("Opcións")
        self.maia1.addWidget(self.group1)
        self.maiaGroup = QGridLayout()
        self.group1.setLayout(self.maiaGroup)

        self.cmbDiario = QComboBox()
        self.datos = ["Semanal","Diario"]
        self.cmbDiario.addItems(self.datos)
        self.maiaGroup.addWidget(self.cmbDiario,0,0,1,1)
        self.cmbDiario.currentIndexChanged.connect(self.on_cmbDiario_currentIndexChanged)

        chkAntixiada = QCheckBox("Antixiada")
        self.maiaGroup.addWidget(chkAntixiada,0,1,1,1)
        chkChuvia = QCheckBox("Chuvia")
        self.maiaGroup.addWidget(chkChuvia,0,2,1,1)

        self.group2 = QGroupBox("Días")
        self.maia1.addWidget(self.group2,0,2)
        self.maiaGroup2 = QGridLayout()
        self.group2.setLayout(self.maiaGroup2)

        chkLuns = QCheckBox("Luns")
        self.maiaGroup2.addWidget(chkLuns,0,0,1,1)
        chkMartes = QCheckBox("Martes")
        self.maiaGroup2.addWidget(chkMartes, 0, 1, 1, 1)
        chkMercores = QCheckBox("Mércores")
        self.maiaGroup2.addWidget(chkMercores, 1, 0, 1, 1)
        chkXoves = QCheckBox("Xoves")
        self.maiaGroup2.addWidget(chkXoves, 1, 1, 1, 1)
        chkVenres = QCheckBox("Venres")
        self.maiaGroup2.addWidget(chkVenres, 2, 0, 1, 1)
        chkSabado = QCheckBox("Sábado")
        self.maiaGroup2.addWidget(chkSabado, 2, 1, 1, 1)
        chkDomingo = QCheckBox("Domingo")
        self.maiaGroup2.addWidget(chkDomingo, 3, 0, 1, 1)


        btnAceptar = QPushButton("Aceptar")
        self.maia1.addWidget(btnAceptar,3,2,1,1)

        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()


    def chkZoActivada_escribir(self):
        if self.chkZoaActivada.isChecked():
            self.txeOutroCadroTexto.append("Zoa Activada")
        else:
            self.txeOutroCadroTexto.append("Zoa Desactivada")

    def on_cmbDiario_currentIndexChanged(self):
        self.txeOutroCadroTexto.append("El combo Box marca: " + self.cmbDiario.currentText())

    def sldDuracionRego_rango(self):
        self.txeOutroCadroTexto.append("El rango del slide es: " + str(self.sldDuracionRego.value()))


    def on_txtHoraComezoRego_clicked(self):
        self.txeOutroCadroTexto.append("Hora: " + self.txtHoraComezoRego.text())


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()