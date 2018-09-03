import turtle as t

num_circle = 30
radius = 180

t.bgcolor("blue")
t.color("yellow")
t.speed(0)

for _ in range(num_circle):
    t.circle(radius)
    t.left(360/num_circle)

t.done()
