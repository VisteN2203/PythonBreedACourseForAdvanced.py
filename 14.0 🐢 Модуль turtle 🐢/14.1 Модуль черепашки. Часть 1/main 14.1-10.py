import turtle


def star(side):
    turtle.forward(side / 2)
    for _ in range(5):
        turtle.right(144)
        turtle.forward(side)


star(80)