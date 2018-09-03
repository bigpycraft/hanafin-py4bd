# import turtle as t
#
# polygon = t.Turtle()
#
#
# var1 = input('면의 수는?')
# var2 = input('면의 길이?')
#
# num_sides = int(var1)
# side_length = int(var2)
# angle = 360.0 / num_sides
#
# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)
#
# t.done()

import turtle as t

print('다각형을 그리는 예제입니다.')
var1 = input('변의 수를 입력해주세요? [3-8] ')
var2 = input('한변의 길이를 입력해주세요? [100-200] ')
# var2 = str(150)

num_of_side = int(var1)
len_of_side = int(var2)

angle = 360.0 / num_of_side
c_mod = num_of_side % 3
color = 'red' if c_mod==0 else 'green' if c_mod==1 else 'blue'

t.begin_fill()
t.color(color)
t.pensize(5)

for i in range(num_of_side):
    t.forward(len_of_side)
    t.left(angle)

t.end_fill()

t.done()
