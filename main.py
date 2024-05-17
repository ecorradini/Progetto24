import sys
from PyQt6.QtWidgets import QApplication
from Viste.vista_home import VistaHome

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec())
