from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
import pickle
import os
from datetime import datetime

from Entita.bagnino import Bagnino


class VistaNuovoDipendente(QWidget):

    def __init__(self, callback, parent=None):
        super(VistaNuovoDipendente, self).__init__(parent)
        uic.loadUi('Viste/vista_nuovo_dipendente.ui', self)

        self.callback = callback

        self.bottone_annulla.clicked.connect(self.annulla)
        self.bottone_conferma.clicked.connect(self.conferma)

    def _ottieni_ultimo_id(self):
        lista_bagnini_salvata = []
        if os.path.isfile('Dati/bagnini.pickle'):
            with open('Dati/bagnini.pickle', 'rb') as f:
                lista_bagnini_salvata = pickle.load(f)
        if len(lista_bagnini_salvata) > 0:
            return max([b['id'] for b in lista_bagnini_salvata])
        else:
            return 0

    def annulla(self):
        self.close()

    def conferma(self):
        nome = self.text_nome.text()
        cognome = self.text_cognome.text()
        cf = self.text_cf.text()
        indirizzo = self.text_indirizzo.text()
        email = self.text_email.text()
        telefono = self.text_telefono.text()
        datanascita = self.text_datanascita.text()
        luogonascita = self.text_luogonascita.text()
        licenza = self.text_licenza.text()
        if nome == "" or cognome == "" or cf == "" or indirizzo == "" \
            or email == "" or telefono == "" or datanascita == "" \
            or luogonascita == "" or licenza == "":
            QMessageBox.critical(self, 'Attenzione!',
                                 "Per favore, inserisci tutti i dati richiesti.",
                                 QMessageBox.StandardButton.Ok)
        else:
            try:
                datanascita = datetime.strptime(datanascita, "%d/%m/%Y")
                nuovo_bagnino = Bagnino()
                nuovo_bagnino.aggiungi_bagnino(id=self._ottieni_ultimo_id() + 1,
                                               nome=nome, cognome=cognome,
                                               cf=cf, indirizzo=indirizzo,
                                               email=email, telefono=telefono,
                                               datanascita=datanascita,
                                               luogonascita=luogonascita,
                                               licenza=licenza)
                self.callback()
                self.close()
            except:
                QMessageBox.critical(self, 'Attenzione!',
                                     "Per favore, inserisci la data nel formato dd/MM/yyyy",
                                     QMessageBox.StandardButton.Ok)
