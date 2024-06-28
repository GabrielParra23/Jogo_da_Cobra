from turtle import Screen, Turtle
posicao_inicial = [(0, 0), (-20, 0), (-40, 0)]

class Cobra:

    def __init__(self):
        self.cobra = []




    def criacao_cobra(self):
        for posicao in posicao_inicial:
            self.add_segmento(posicao)


    def add_segmento(self, position):
        parte = Turtle(shape="square")
        parte.penup()
        parte.color("green")
        parte.goto(position)
        self.cobra.append(parte)

    def extensao(self):
        self.add_segmento(self.cobra[-1].position())

    def mover(self):
        for segmento in range(len(self.cobra) - 1, 0, -1):  # range(start= len(cobra), stop=0, step = -1)
            novo_x = self.cobra[segmento - 1].xcor()
            novo_y = self.cobra[segmento - 1].ycor()
            self.cobra[segmento].goto(novo_x, novo_y)
        self.cobra[0].forward(20)




     #adiciona um novo segmento a cobra




    def up(self):
        if self.cobra[0].heading() != 270:
            self.cobra[0].seth(90)

    def down(self):
        if self.cobra[0].heading() != 90:
            self.cobra[0].seth(270)

    def left(self):
        if self.cobra[0].heading() != 0:
            self.cobra[0].seth(180)

    def right(self):
        if self.cobra[0].heading() != 180:
            self.cobra[0].seth(360)




