import turtle
import math

width = 200
diagonal = math.sqrt(width**2 + width**2)

turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(5)

turtle.left(45)
turtle.forward(diagonal)
turtle.left(90)
turtle.forward(diagonal/2)
turtle.left(90)
turtle.forward(diagonal/2)
turtle.left(90)
turtle.forward(diagonal)

turtle.left(45)

for i in range(4):
    turtle.left(90)
    turtle.forward(width)

turtle.done()