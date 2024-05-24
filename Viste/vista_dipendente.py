from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class VistaDipendente(QWidget):
    def __init__(self, dipendente, parent=None):
        super().__init__(parent)
        uic.loadUi('Viste/vista_dipendente.ui', self)

        self.label_nomecognome.setText(dipendente.nome + " " + dipendente.cognome)
        self.label_id.setText(f"id: {dipendente.id}")
        self.label_cf.setText(f"Codice Fiscale: {dipendente.cf}")
        self.label_indirizzo.setText(f"Indirizzo: {dipendente.indirizzo}")
        self.label_email.setText(f"E-mail: {dipendente.email}")
        self.label_telefono.setText(f"Telefono: {dipendente.telefono}")
        self.label_datanascita.setText(f"Data di nascita: {dipendente.datanascita.strftime('%d/%m/%Y')}")
        self.label_luogonascita.setText(f"Luogo di nascita: {dipendente.luogonascita}")
        self.label_licenza.setText(f"Licenza: {dipendente.licenza}")
