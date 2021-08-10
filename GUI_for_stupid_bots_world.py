from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("ТАНКИ ОНЛАЙН БЕЗ СМС И РЕГИСТРАЦИИ")
        self.setGeometry(100, 60, 900, 540)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("ВЫ ЗАПУСТИЛИ ТАНКИ ОНЛАЙН")
        self.main_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


application()
