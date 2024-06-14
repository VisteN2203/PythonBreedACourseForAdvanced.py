import turtle


def rectangle(width, height):
	turtle.showturtle()
	turtle.forward(width)
	turtle.right(90)
	turtle.forward(height)
	turtle.right(90)
	turtle.forward(width)
	turtle.right(90)
	turtle.forward(height)


width = int(input())
height = int(input())
rectangle(width, height)
