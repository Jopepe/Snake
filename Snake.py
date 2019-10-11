import turtle
import time
import random
import keyboard

posponer = 0.1


#Ventana
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 550)
wn.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direccion = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.direccion = "stop"

#Cuerpo
segmentos = []


#Funciones
def arriba():
    cabeza.direccion = "up"
def abajo():
    cabeza.direccion = "down"
def derecha():
    cabeza.direccion =  "right"
def izquierda():
    cabeza.direccion = "left"
    
def mov():
    if cabeza.direccion == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direccion == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direccion == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        
    if cabeza.direccion == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

#Bucle principal
while True:
    wn.update()

    #Bordes
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() < -250 or cabeza.ycor() > 250:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Limpiar segmentos
        for segmento in segmentos:
            segmento.goto(2000,2000)
        segmentos.clear()
        

    #Colision cuerpo
#    totalSeg = len(segmentos)
#    if  cabeza.xcor() == :
#        time.sleep(1)
#        cabeza.goto(0,0)
#        cabeza.direction = "stop"

        #Limpiar segmentos
#        for segmento in segmentos:
#            segmento.goto(2000,2000)
#        segmentos.clear()
        
        
    #Colision comida
    if cabeza.distance(comida) < 20:
        tx = random.randint(-280,280)
        ty = random.randint(-205,205)
        comida.goto(tx,ty)
        
        n_segmento = turtle.Turtle()
        n_segmento.speed(0)
        n_segmento.shape("square")
        n_segmento.color("grey")
        n_segmento.penup()
        segmentos.append(n_segmento)

    #Mover segmentos
    totalSeg = len(segmentos)
    for index in range(totalSeg -1,0,-1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()
    time.sleep(posponer)
