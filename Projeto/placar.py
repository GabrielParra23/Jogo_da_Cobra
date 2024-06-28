from turtle import Turtle
alinhamento = "center"
fonte = ("courier", 20, "normal")

class Placar(Turtle):
    def __init__(self):
        self.pontos = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.color("white")


        self.write(f"Pontuação = {self.pontos}",align=alinhamento, font=fonte)

    def gerando_placar(self):
        self.clear()
        self.pontos += 1
        self.write(f"Pontuação = {self.pontos}",align=alinhamento, font=fonte)

    def fim_jogo(self):
        self.goto(0, 0)
        self.write("Fim de jogo", align=alinhamento, font=fonte)