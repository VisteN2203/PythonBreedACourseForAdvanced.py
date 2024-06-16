import turtle

def rays_of_star(side):
    turtle.forward(side)
    turtle.backward(side)
    turtle.left(36)

for _ in range(10):
    rays_of_star(75)