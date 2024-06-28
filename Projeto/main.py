from turtle import Screen
from cobra import Cobra
from comida import Comida
from placar import Placar

import time

cobra = Cobra()
tela = Screen()
comida = Comida()
pontos = Placar()

tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Meu jogo da cobra")
tela.tracer(0)

tela.listen() #TODO para fazer os botões funcionarem
tela.onkey(cobra.up, "Up") #Todo são as setinhas para cima
tela.onkey(cobra.down,"Down") #Todo são as setinhas para baixo
tela.onkey(cobra.left,"Left") #Todo são as setinhas para esquerda
tela.onkey(cobra.right,"Right") #Todo são as setinhas para direita


cobra.criacao_cobra()


tela.update()

jogo_on = True
while jogo_on == True:
    tela.update()
    time.sleep(0.1)

    cobra.mover()

    #detectando colisão com a comida

    if cobra.cobra[0].distance(comida) < 15:
        comida.gerando_comida()
        pontos.gerando_placar()
        cobra.extensao()

    # detectando colisão com a parede

    if cobra.cobra[0].xcor() > 290 or cobra.cobra[0].xcor() < -290 or cobra.cobra[0].ycor() > 290 or cobra.cobra[0].ycor() < -290:
        jogo_on = False
        pontos.fim_jogo()

    # detectando colisão com a cobra
    for segmento in cobra.cobra[1:]: # TODO desta forma pegamos apenas uma pequena parte da lista
        if cobra.cobra[0].distance(segmento) < 10: #se a cabeça colide com qualquer segmentode seu corpo:
            jogo_on = False #O JOGO TERMINA
            pontos.fim_jogo()


tela.listen()
tela.exitonclick()