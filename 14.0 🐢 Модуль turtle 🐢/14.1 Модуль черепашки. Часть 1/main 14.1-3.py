import turtle

def square(side):
	turtle.showturtle()
	for __ in range(3):
		turtle.left(20)
		for _ in range(4):
			turtle.forward(side)
			turtle.left(90)



side = int(input())
square(side)