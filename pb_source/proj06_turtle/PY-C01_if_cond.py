import turtle

in_color = input('원의 색깔을 입력하세요. (R/G/B/etc)  ')
is_filled = input('원의 색깔로 채우겠습니까? (Yes/No)  ')

if in_color == 'R' or in_color == 'r':
    color = 'red'
elif in_color == 'G' or in_color == 'g':
    color = 'green'
elif in_color == 'B' or in_color == 'b':
    color = 'blue'
else:
    color = 'black'

turtle.begin_fill()

turtle.color(color)
turtle.pensize(10)
turtle.circle(100)

if is_filled == 'Y' or is_filled == 'y':
    turtle.end_fill()
else:
    pass

turtle.done()