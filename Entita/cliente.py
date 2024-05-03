import os
import pickle

from Entita.utilizzatore import Utilizzatore


class Cliente(Utilizzatore):

    def __init__(self, id=None, nome=None, cognome=None, cf=None,
                 indirizzo=None, email=None, telefono=None,
                 abbonamenti=None, note=None):
        super(Cliente, self).__init__(id, nome, cognome, cf,
                                      indirizzo, email, telefono)
        self.abbonamenti = abbonamenti
        self.note = note

    def _load(self):
        lista_clienti_salvata = []
        if os.path.isfile('Dati/clienti.pickle'):
            with open('Dati/clienti.pickle', 'rb') as f:
                lista_clienti_salvata = pickle.load(f)
        return lista_clienti_salvata

    def _save(self, lista):
        with open('Dati/clienti.pickle', 'wb') as f:
            pickle.dump(lista, f)

    def aggiungi_cliente(self, id, nome, cognome, cf, indirizzo, email,
                         telefono, abbonamenti, note):
        super().aggiungiUtilizzatore(id, nome, cognome, cf, indirizzo, email,
                                     telefono)
        self.abbonamenti = abbonamenti
        self.note = note

        lista_clienti_salvata = self._load()
        lista_clienti_salvata.append(self.get_info_cliente())
        self._save(lista_clienti_salvata)

    def get_info_cliente(self):
        info = super().get_info_utilizzatore()
        info["abbonamenti"] = self.abbonamenti
        info["note"] = self.note
        return info

    def _from_dict(self, cliente_dict):
        return Cliente(
            cliente_dict["id"],
            cliente_dict["nome"],
            cliente_dict["cognome"],
            cliente_dict["cf"],
            cliente_dict["indirizzo"],
            cliente_dict["email"],
            cliente_dict["telefono"],
            cliente_dict["abbonamenti"],
            cliente_dict["note"]
        )

    def ricerca_utilizzatore_cf(self, cf):
        lista_clienti_salvata = self._load()
        for cliente_dict in lista_clienti_salvata:
            if cliente_dict["cf"] == cf:
                return self._from_dict(cliente_dict)
        return None

    def ricerca_utilizzatore_codice(self, codice):
        lista_clienti_salvata = self._load()
        for cliente_dict in lista_clienti_salvata:
            if cliente_dict["id"] == codice:
                return self._from_dict(cliente_dict)
        return None

    def ricerca_utilizzatore_nomecognome(self, nome, cognome):
        lista_clienti_salvata = self._load()
        for cliente_dict in lista_clienti_salvata:
            if cliente_dict["nome"] == nome and cliente_dict["cognome"] == cognome:
                return self._from_dict(cliente_dict)
        return None

    def rimuovi_cliente(self):
        lista_clienti_salvata = self._load()
        for cliente in lista_clienti_salvata:
            if cliente["id"] == self.id:
                lista_clienti_salvata.remove(cliente)
                break
        self._save(lista_clienti_salvata)

        super().rimuovi_utilizzatore()
        self.abbonamenti = None
        self.note = None
        del self
