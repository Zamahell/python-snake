import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

#S == canvas
s = turtle.Screen()
s.setup(650, 650) #Darle un pixeleado a la pantalla
s.bgcolor('gray')
s.title('Serpiente')
s.tracer()

serpiente = turtle.Turtle()
serpiente.speed(4)
serpiente.shape('square')
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color('green')

#Comida Snake, Circulo de color naranja.
comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)
comida.speed(0)


#Crecimineto del cuerpo al comer, Lista vacia de cuerpo.
cuerpo = []

#Instanciar texto para el marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0, -260)
texto.write("Puntaje: 0\tPuntaje Supremo: 0", align="center", font=("verdana", 24, "normal"))



def arriba():
    serpiente.direction = 'up'

def abajo():
    serpiente.direction = 'down'

def derecha():
    serpiente.direction = 'right'

def izquierda():
    serpiente.direction = 'left'

#movimiento de la serpiente con plano cartesiano
def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    elif serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    elif serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    elif serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)

#Movimiento presionando las teclas
s.listen() #la pantalla o lienzo toma valores escritos por el usuario
s.onkeypress(arriba, "Up") #cuando presione la flecha hacia arriba, se activa el movimiento
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")




#Movimiento de Serpiente constante, actualizacion y tiempo
while True:
    s.update()

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = 'stop'
        cuerpo.clear()


        marcador = 0
        texto.clear()
        texto.write("Puntaje:{}\tPuntaje Supremo:{}".format(marcador,marcador_alto),align="center", font=("verdana", 24, "normal"))
        


    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250) #cuando la comida toca con la cabeza, la comida toma un punto entre eje Y y X
        y = random.randint(-250, 250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Puntaje:{}\tPuntaje Supremo:{}".format(marcador,marcador_alto),align="center", font=("verdana", 24, "normal"))

    total = len(cuerpo) #medida del cuerpo
    for index in range(total -1 , 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)
        


    movimiento()

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"

    time.sleep(retraso)

turtle.done()