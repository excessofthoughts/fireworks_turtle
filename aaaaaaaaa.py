import turtle
import random

screen = turtle.Screen()
screen.bgcolor('#191970')

pashka = turtle.Turtle()
pashka.speed(20)
pashka.hideturtle()
screen.setup(600, 600)
def one_firework(color1, color2, length): #функция, которая рисует один фейерверк
    pashka.color(color1, color2)
    pashka.begin_fill()
    for _ in range(36):
        pashka.fd(length)
        pashka.left(170)
    pashka.end_fill()


def work_firework(fw_amount): # крутое название для функции?!
    while True:
        for _ in range(fw_amount):
            pashka.penup()
            pashka.right(random.randint(0, 360))
            pashka.goto(0, 0) #перемещаем в центр
            pashka.forward(random.randint(0, 100)) #черепашка движется вперед под заданным ранее углом
            pashka.pendown()
            color1 = '#{:06x}'.format(random.randint(0, 0xffffff)) #выбор рандомных цветов
            color2 = '#{:06x}'.format(random.randint(0, 0xffffff))
            length = random.randint(30, 100)
            one_firework(color1, color2, length)
        screen.clear() #очистка окна, чтобы салютов не стало слишком много
        screen.bgcolor('#191970')


work_firework(10)

screen.exitonclick()