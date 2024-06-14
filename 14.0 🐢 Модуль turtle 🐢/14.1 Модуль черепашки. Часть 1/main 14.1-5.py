import turtle

def hexagon(side):
    turtle.showturtle()
    count = 0
    for _ in range(6):
        turtle.forward(side)
        count += 60
        turtle.setheading(count)


side = int(input())
hexagon(side)