"""
from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow
"""
from gui_engine_base_classes import IGUIDrawer
from common_classes import *
from time import sleep

import turtle

"""
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("ТАНКИ ОНЛАЙН БЕЗ СМС И РЕГИСТРАЦИИ БЕСПЛАТНО")
        self.setGeometry(100, 60, 900, 540)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("ВЫ ЗАПУСТИЛИ ТАНКИ ОНЛАЙН")
        self.main_text.adjustSize()
"""
class GUIActions(IGUIDrawer):
    def __init__(self, x, squarex, squarey):
        self.x = x
        self.squarex = squarex
        self.squarey = squarey
        self.len_square = self.x / self.squarex
        self.y = int(self.squarey * self.len_square)
        print(self.x, self.y, self.squarex, self.squarey)

    def initialize(self):

        """
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())
        """
        turtle.tracer(1, 0)
        turtle.reset()
        turtle.screensize(self.x, self.y)

        turtle.up()
        turtle.goto(0-(self.x/2), 0-(self.y/2))
        turtle.setheading(0)

        for i in range(self.squarex + 1):
            turtle.down()
            turtle.left(90)
            turtle.forward(self.y)
            turtle.back(self.y)
            turtle.right(90)
            turtle.forward(self.len_square)

        turtle.up()
        turtle.goto(0 - (self.x / 2), 0 + (self.y / 2))
        turtle.setheading(0)

        for i in range(self.squarey + 1):
            turtle.down()
            turtle.forward(self.x)
            turtle.back(self.x)
            turtle.right(90)
            turtle.forward(self.len_square)
            turtle.left(90)

        sleep(3)

    def draw_an_obstacle(self, obstacle_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_an_obstacle(...) from interface IGUIDrawer")

    def draw_a_projectile(self, projectile_data: ProjectileData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_projectile(...) from interface IGUIDrawer")

    def draw_a_bot(self, bot_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_bot(...) from interface IGUIDrawer")

    def draw_a_player(self, player_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_player(...) from interface IGUIDrawer")

    def clear_screen(self):
        raise RuntimeError("Can't find override for function"
                           " clear_screen(...) from interface IGUIDrawer")

    def stop(self):
        raise RuntimeError("Can't find override for function"
                           " stop(...) from interface IGUIDrawer")

actions = GUIActions(600, 10, 6)
actions.initialize()

