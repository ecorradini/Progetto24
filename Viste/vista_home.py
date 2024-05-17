from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from Viste.vista_dipendenti import VistaDipendenti


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        uic.loadUi('Viste/vista_home.ui', self)

        self.bottone_dipendenti.clicked.connect(self.apri_dipendenti)

    def apri_dipendenti(self):
        self.vista_dipendenti = VistaDipendenti()
        self.vista_dipendenti.show()