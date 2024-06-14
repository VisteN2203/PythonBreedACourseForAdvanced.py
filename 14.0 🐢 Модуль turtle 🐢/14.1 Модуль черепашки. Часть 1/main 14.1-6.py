import turtle

def hexagon(side):
    turtle.showturtle()
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)
    turtle.forward(side)
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

side = int(input())
hexagon(side)