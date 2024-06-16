import turtle

def rhomb(side):
	for _ in range(2):
		turtle.forward(side)
		turtle.left(60)
		turtle.forward(side)
		turtle.left(120)


for __ in range(10):
	rhomb(75)
	turtle.left(36)
