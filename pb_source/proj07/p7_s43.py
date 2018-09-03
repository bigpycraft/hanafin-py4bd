import turtle as t

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']
# colors = ['red', 'green', 'blue', 'yellow']
for i in range(45):
    t.color(colors[i%len(colors)])
    # t.pendown()
    t.forward(2 + i*5)
    t.left(45)
    t.width(i)
    # t.penup()

t.done()