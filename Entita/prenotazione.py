from datetime import datetime
import os
import pickle


class Prenotazione:

    def __init__(self, cliente=None, codice=None,
                 data_ora_inizio=None, data_ora_fine=None,
                 servizio=None):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio

    def _load(self):
        lista_prenotazioni_salvata = []
        if os.path.isfile('Dati/prenotazioni.pickle'):
            with open('Dati/prenotazioni.pickle', 'rb') as f:
                lista_prenotazioni_salvata = pickle.load(f)
        return lista_prenotazioni_salvata

    def _save(self, lista):
        with open('Dati/prenotazioni.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def aggiungi_prenotazione(self, cliente, codice,
                 data_ora_inizio, data_ora_fine,
                 servizio):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio

        lista_prenotazioni_salvata = self._load()
        lista_prenotazioni_salvata.append(self.get_info_prenotazione())
        self._save(lista_prenotazioni_salvata)

    def get_info_prenotazione(self):
        return {
            "cliente": self.cliente,
            "codice": self.codice,
            "data_ora_inizio": self.data_ora_inizio,
            "data_ora_fine": self.data_ora_fine,
            "servizio": self.servizio
        }

    def verifica_fine(self):
        return datetime.now() > self.data_ora_fine

    def disdisci_prenotazione(self):
        lista_prenotazioni_salvata = self._load()
        for prenotazione in lista_prenotazioni_salvata:
            if prenotazione["codice"] == self.codice:
                lista_prenotazioni_salvata.remove(prenotazione)
                break
        self.codice = None
        self.cliente = None
        self.data_ora_fine = None
        self.data_ora_inizio = None
        self.servizio = None
        del self