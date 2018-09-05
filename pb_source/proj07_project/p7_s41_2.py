import turtle
import math

width = 200
diagonal = math.sqrt(width**2 + width**2)

turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(5)

for i in range(4):
    turtle.left(90)
    turtle.forward(width)

turtle.left(90+45)
turtle.forward(diagonal)
turtle.right(90)
turtle.forward(diagonal/2)
turtle.right(90)
turtle.forward(diagonal/2)
turtle.right(90)
turtle.forward(diagonal)

turtle.done()