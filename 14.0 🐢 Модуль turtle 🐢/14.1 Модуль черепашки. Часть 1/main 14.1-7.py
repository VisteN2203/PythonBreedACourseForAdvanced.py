import turtle

def rhomb(side):
	turtle.showturtle()
	for _ in range(2):
		turtle.forward(side)
		turtle.left(120)
		turtle.forward(side)
		turtle.left(60)

side = int(input())

rhomb(side)