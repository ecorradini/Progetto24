class Utilizzatore():

    def __init__(self, id=None, nome=None, cognome=None, cf=None,
                 indirizzo=None, email=None, telefono=None):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.indirizzo = indirizzo
        self.email = email
        self.telefono = telefono

    def aggiungiUtilizzatore(self, id, nome, cognome, cf, indirizzo, email, telefono):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.indirizzo = indirizzo
        self.email = email
        self.telefono = telefono

    def get_info_utilizzatore(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "cf": self.cf,
            "indirizzo": self.indirizzo,
            "email": self.email,
            "telefono": self.telefono
        }

    def ricerca_utilizzatore_cf(self, cf):
        raise NotImplementedError()

    def ricerca_utilizzatore_codice(self, codice):
        raise NotImplementedError()

    def ricerca_utilizzatore_nomecognome(self, nome, cognome):
        raise NotImplementedError()

    def rimuovi_utilizzatore(self):
        self.id = None
        self.nome = None
        self.cognome = None
        self.cf = None
        self.indirizzo = None
        self.email = None
        self.telefono = None