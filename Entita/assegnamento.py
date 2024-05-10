import os
import pickle
from datetime import datetime

class Assegnamento:

    def __init__(self, cliente=None, codice=None,
                 data_ora_inizio=None, data_ora_fine=None,
                 servizio=None):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio

    def _load(self):
        lista_assegnamenti_salvata = []
        if os.path.isfile('Dati/assegnamenti.pickle'):
            with open('Dati/assegnamenti.pickle', 'rb') as f:
                lista_assegnamenti_salvata = pickle.load(f)
        return lista_assegnamenti_salvata

    def _save(self, lista):
        with open('Dati/assegnamenti.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def aggiungi_assegnamento(self, cliente, codice,
                 data_ora_inizio, data_ora_fine,
                 servizio):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio

        lista_assegnamenti_salvata = self._load()
        lista_assegnamenti_salvata.append(self.get_info_assegnamento())
        self._save(lista_assegnamenti_salvata)

    def get_info_assegnamento(self):
        return {
            "cliente": self.cliente,
            "codice": self.codice,
            "data_ora_inizio": self.data_ora_inizio,
            "data_ora_fine": self.data_ora_fine,
            "servizio": self.servizio
        }

    def rimuovi_assegnamento(self):
        lista_assegnamenti_salvata = self._load()
        for assegnamento in lista_assegnamenti_salvata:
            if assegnamento["codice"] == self.codice:
                lista_assegnamenti_salvata.remove(assegnamento)
                break
        self.cliente = None
        self.codice = None
        self.data_ora_fine = None
        self.data_ora_inizio = None
        self.servizio = None

        del self

    def verifica_fine(self):
        return datetime.now() > self.data_ora_fine