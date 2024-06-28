from turtle import  Turtle
import random

class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        valor_x = random.randint(-280, 280)
        valor_y = random.randint(-280, 280)
        self.goto(valor_x, valor_y)

    def gerando_comida(self):
        valor_x = random.randint(-280, 280)
        valor_y = random.randint(-280, 280)
        self.goto(valor_x, valor_y)




