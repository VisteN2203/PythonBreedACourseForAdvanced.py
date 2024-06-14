import turtle

def triangle(side):
	turtle.showturtle()
	for _ in range(3):
		turtle.forward(side)
		turtle.left(60*2)

side = int(input())
triangle(side)