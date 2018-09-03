import turtle as t

t.pensize(3)
t.color('red')

for i in range(10):
    t.forward(15)
    t.penup()
    t.forward(15)
    t.pendown()

t.done()