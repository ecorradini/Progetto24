import os
import pickle
from datetime import datetime

class Abbonamento():

    def __init__(self, codice=None, data_inizio=None, data_rilascio=None,
                 data_scadenza=None, stagionale=None):
        self.codice = codice
        self.data_inizio = data_inizio
        self.data_rilascio = data_rilascio
        self.data_scadenza = data_scadenza
        self.stagionale = stagionale

    def _load(self):
        lista_abbonamenti_salvata = []
        if os.path.isfile('Dati/abbonamenti.pickle'):
            with open('Dati/abbonamenti.pickle', 'rb') as f:
                lista_abbonamenti_salvata = pickle.load(f)
        return lista_abbonamenti_salvata

    def _save(self, lista):
        with open('Dati/abbonamenti.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def aggiungi_abbonamento(self, codice, data_inizio, data_rilascio,
                 data_scadenza, stagionale):
        self.codice = codice
        self.data_inizio = data_inizio
        self.data_rilascio = data_rilascio
        self.data_scadenza = data_scadenza
        self.stagionale = stagionale

        lista_abbonamenti_salvata = self._load()
        lista_abbonamenti_salvata.append(self.get_info_abbonamento())
        self._save(lista_abbonamenti_salvata)

    def get_info_abbonamento(self):
        return {
            "codice": self.codice,
            "data_inizio": self.data_inizio,
            "data_rilascio": self.data_rilascio,
            "data_scadenza": self.data_scadenza,
            "stagionale": self.stagionale
        }

    def _from_dict(self, dizionario_abbonamento):
        return Abbonamento(dizionario_abbonamento["codice"],
                           dizionario_abbonamento["data_inizio"],
                           dizionario_abbonamento["data_rilascio"],
                           dizionario_abbonamento["data_scadenza"],
                           dizionario_abbonamento["stagionale"])

    def ricerca_abbonamento(self, codice):
        lista_abbonamenti_salvata = self._load()
        for abbonamento in lista_abbonamenti_salvata:
            if abbonamento["codice"] == codice:
                return self._from_dict(abbonamento)
        return None

    def rimuovi_abbonamento(self):
        lista_abbonamenti_salvata = self._load()
        for abbonamento in lista_abbonamenti_salvata:
            if abbonamento["codice"] == self.codice:
                lista_abbonamenti_salvata.remove(abbonamento)
                break
        self._save(lista_abbonamenti_salvata)
        self.codice = None
        self.data_inizio = None
        self.data_rilascio = None
        self.data_scadenza = None
        self.stagionale = None
        del self

    def verifica_scaduto(self):
        return datetime.now() > self.data_scadenza