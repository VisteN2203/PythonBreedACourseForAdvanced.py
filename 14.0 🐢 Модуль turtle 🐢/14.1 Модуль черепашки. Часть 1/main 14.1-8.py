import turtle

def rhomb(side):
	for _ in range(4):
		turtle.forward(side)
		turtle.left(60)

turtle.showturtle()
side = int(input())
for __ in range(10):
	rhomb(side)




