"""
from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow
"""
from gui_engine_base_classes import IGUIDrawer
from common_classes import *
from time import sleep

import turtle
turtle.reset()
turtle.tracer(0, 0)
turtle.hideturtle()
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

        turtle.screensize(self.x, self.y)
        turtle.color("black")

        turtle.penup()
        turtle.goto(0-(self.x/2), 0-(self.y/2))
        turtle.setheading(0)

        for i in range(self.squarex + 1):
            turtle.down()
            turtle.left(90)
            turtle.forward(self.y)
            turtle.back(self.y)
            turtle.right(90)
            turtle.forward(self.len_square)

        turtle.penup()
        turtle.goto(0 - (self.x / 2), 0 + (self.y / 2))
        turtle.setheading(0)

        for i in range(self.squarey + 1):
            turtle.pendown()
            turtle.forward(self.x)
            turtle.back(self.x)
            turtle.right(90)
            turtle.forward(self.len_square)
            turtle.left(90)

        turtle.penup()
        turtle.update()

    def draw_an_obstacle(self, x, y):
        turtle.color("black")

        turtle.goto((x - 1) * self.len_square - self.x / 2, (y - 1) * self.len_square - self.y / 2)
        turtle.setheading(0)
        turtle.pendown()

        turtle.begin_fill()
        for i in range(4):
            turtle.forward(self.len_square)
            turtle.left(90)
        turtle.end_fill()

        turtle.penup()
        turtle.update()

    def draw_a_projectile(self, x, y):
        turtle.color("gray")
        turtle.goto((x - 1) * self.len_square - self.x / 2, (y - 1) * self.len_square - self.y / 2)
        turtle.setheading(0)
        turtle.forward(self.len_square / 2)
        turtle.left(90)
        turtle.forward(self.len_square//4)
        turtle.right(90)
        turtle.pendown()

        turtle.begin_fill()
        turtle.circle(self.len_square // 4)
        turtle.end_fill()

        turtle.penup()
        turtle.update()

    def draw_a_bot(self, x, y):
        turtle.color("red")
        turtle.goto((x - 1) * self.len_square - self.x / 2, (y - 1) * self.len_square - self.y / 2)
        turtle.setheading(0)
        turtle.forward(self.len_square / 2)
        turtle.pendown()

        turtle.begin_fill()
        turtle.circle(self.len_square / 2)
        turtle.end_fill()

        turtle.penup()
        turtle.update()

    def draw_a_player(self, x, y):
        turtle.color("green")
        turtle.goto((x - 1) * self.len_square - self.x / 2, (y - 1) * self.len_square - self.y / 2)
        turtle.setheading(0)
        turtle.forward(self.len_square / 2)
        turtle.pendown()

        turtle.begin_fill()
        turtle.circle(self.len_square / 2)
        turtle.end_fill()

        turtle.penup()
        turtle.update()

    def clear_screen(self):
        turtle.clear()

    def stop(self):
        raise RuntimeError("Can't find override for function"
                           " stop(...) from interface IGUIDrawer")

