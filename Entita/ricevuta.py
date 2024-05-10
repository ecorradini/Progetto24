import os
import pickle


class Ricevuta:

    def __init__(self, ammontare_lordo=None, assegnamento=None,
                 data=None, prezzo_ingresso=None):
        self.ammontare_lordo = ammontare_lordo
        self.assegnamento = assegnamento
        self.data = data
        self.prezzo_ingresso = prezzo_ingresso

    def _load(self):
        lista_ricevute_salvata = []
        if os.path.isfile('Dati/ricevute.pickle'):
            with open('Dati/ricevute.pickle', 'rb') as f:
                lista_ricevute_salvata = pickle.load(f)
        return lista_ricevute_salvata

    def _save(self, lista):
        with open('Dati/ricevute.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def get_info_ricevuta(self):
        return {
            "ammontare_lordo": self.ammontare_lordo,
            "assegnamento": self.assegnamento,
            "data": self.data,
            "prezzo_ingresso": self.prezzo_ingresso
        }

    def aggiungi_ricevuta(self, ammontare_lordo, assegnamento,
                 data, prezzo_ingresso):
        self.ammontare_lordo = ammontare_lordo
        self.assegnamento = assegnamento
        self.data = data
        self.prezzo_ingresso = prezzo_ingresso

        lista_ricevute_salvata = self._load()
        lista_ricevute_salvata.append(self.get_info_ricevuta())
        self._save(lista_ricevute_salvata)

    def rimuovi_ricevuta(self):
        lista_ricevute_salvata = self._load()
        for ricevuta in lista_ricevute_salvata:
            if ricevuta["assegnamento"].codice == self.assegnamento.codice:
                lista_ricevute_salvata.remove(ricevuta)
                break
        self.ammontare_lordo = None
        self.assegnamento = None
        self.data = None
        self.prezzo_ingresso = None

        del self