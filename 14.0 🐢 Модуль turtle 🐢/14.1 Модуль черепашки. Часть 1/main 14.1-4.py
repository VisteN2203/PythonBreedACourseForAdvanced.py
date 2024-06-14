import turtle

def square(side):
    turtle.showturtle()
    for __ in range(4):
        for _ in range(3):
            turtle.forward(side)
            turtle.left(90)
        turtle.forward(side)
    turtle.left(45)
    for __ in range(4):
        for _ in range(3):
            turtle.forward(side)
            turtle.left(90)
        turtle.forward(side)

side = int(input())
square(side)