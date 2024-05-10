class Servizio:

    tipo = "servizio"

    def __init__(self, codice=None):
        self.codice = codice

    def aggiungi_servizio(self, codice):
        self.codice = codice

    def get_info_servizio(self):
        return {
            "codice": self.codice
        }

    def rimuovi_servizio(self):
        self.codice = None

    def ricerca_servizio(self, codice):
        raise NotImplementedError()