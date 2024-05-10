import os
import pickle

from Servizi.servizio import Servizio


class Cabina(Servizio):

    tipo = "cabina"

    def __init__(self, codice, prezzo_giornata):
        super(Cabina, self).__init__(codice)
        self.prezzo_giornata = prezzo_giornata

    def _load(self):
        lista_servizi_salvata = []
        if os.path.isfile('Dati/servizi.pickle'):
            with open('Dati/servizi.pickle', 'rb') as f:
                lista_servizi_salvata = pickle.load(f)
        return lista_servizi_salvata

    def _save(self, lista):
        with open('Dati/servizi.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def get_info_servizio(self):
        info = super().get_info_servizio()
        info["prezzo_giornata"] = self.prezzo_giornata
        info["tipo"] = Cabina.tipo

    def aggiungi_cabina(self, codice, prezzo_giornata):
        super().aggiungi_servizio(codice)
        self.prezzo_giornata = prezzo_giornata
        lista_servizi_salvata = self._load()
        lista_servizi_salvata.append(self.get_info_servizio())
        self._save(lista_servizi_salvata)

    def rimuovi_servizio(self):
        lista_servizi_salvata = self._load()
        for servizio in lista_servizi_salvata:
            if servizio["tipo"] == Cabina.tipo and servizio["codice"] == self.codice:
                lista_servizi_salvata.remove(servizio)
                break
        super().rimuovi_servizio()
        self.prezzo_giornata = None
        del self

    def _from_dict(self, dizionario_cabina):
        return Cabina(dizionario_cabina["codice"],
                      dizionario_cabina["prezzo_giornata"])

    def ricerca_servizio(self, codice):
        lista_servizi_salvata = self._load()
        for servizio in lista_servizi_salvata:
            if servizio["tipo"] == Cabina.tipo and servizio["codice"] == codice:
                return self._from_dict(servizio)
        return None
