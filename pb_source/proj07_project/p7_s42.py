import turtle

turtle.color('red')
turtle.pensize(10)

for i in range (6):
    # 육각형 그리기
    for j in range(6):
        turtle.forward(100)
        turtle.left(360/6)

    # 패턴찾기
    turtle.forward(100)
    turtle.right(60)

turtle.done()

# def hexagon():
#   for _ in range(6):
#       turtle.forward(100)
#       turtle.left(60)
#
# for _ in range (6):
#     hexagon()
#     turtle.forward(100)
#     turtle.right(60)
#
# turtle.done()

