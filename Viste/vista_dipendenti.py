from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
import os
import pickle

from Viste.vista_nuovo_dipendente import VistaNuovoDipendente


class VistaDipendenti(QWidget):

    def __init__(self, parent=None):
        super(VistaDipendenti, self).__init__(parent)
        uic.loadUi('Viste/vista_dipendenti.ui', self)
        self.dipendenti = []
        if os.path.isfile('Dati/bagnini.pickle'):
            with open('Dati/bagnini.pickle', 'rb') as f:
                self.dipendenti = pickle.load(f)

        self.aggiorna_ui()

        self.bottone_nuovo.clicked.connect(self.nuovo)

    def nuovo(self):
        self.vista_nuovo_dipendente = VistaNuovoDipendente()
        self.vista_nuovo_dipendente.show()

    def aggiorna_ui(self):
        self.listview_model = QStandardItemModel(self.lista_dipendenti)
        for dipendente in self.dipendenti:
            item = QStandardItem()
            item.setText(f"{dipendente.id} - {dipendente.nome} {dipendente.cognome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.lista_dipendenti.setModel(self.listview_model)