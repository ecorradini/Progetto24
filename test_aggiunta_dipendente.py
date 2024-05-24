import os
import pickle
from unittest import TestCase
from datetime import datetime

from Entita.bagnino import Bagnino


class TestAggiuntaDipendente(TestCase):

    def _ottieni_ultimo_id(self):
        lista_bagnini_salvata = []
        if os.path.isfile('Dati/bagnini.pickle'):
            with open('Dati/bagnini.pickle', 'rb') as f:
                lista_bagnini_salvata = pickle.load(f)
        if len(lista_bagnini_salvata) > 0:
            return max([b['id'] for b in lista_bagnini_salvata])
        else:
            return 0

    def test_aggiunta_dipendente(self):
        id = self._ottieni_ultimo_id() + 1
        lista_bagnini_salvata = []
        if os.path.isfile('Dati/bagnini.pickle'):
            with open('Dati/bagnini.pickle', 'rb') as f:
                lista_bagnini_salvata = pickle.load(f)
        lista_id = [bagnino['id'] for bagnino in lista_bagnini_salvata]
        self.assertNotIn(id, lista_id)
        bagnino = Bagnino()
        bagnino.aggiungi_bagnino(id, "Test1", "Test1",
                                 "test1", "via test, 1",
                                 "test1@test.com", 123456,
                                 datetime.strptime("01/01/1990", "%d/%m/%Y"),
                                 "Test 1", 123)
        info = bagnino.get_info_bagnino()
        self.assertNotIn(info, lista_bagnini_salvata)
        if os.path.isfile('Dati/bagnini.pickle'):
            with open('Dati/bagnini.pickle', 'rb') as f:
                lista_bagnini_salvata = pickle.load(f)
        self.assertIn(info, lista_bagnini_salvata)

