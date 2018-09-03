import turtle as t

print('다각형을 그리는 예제입니다.')
var1 = input('변의 수를 입력해주세요? [3-8] ')
var2 = input('한변의 길이를 입력해주세요? [100-200] ')
# var2 = str(150)

num_of_side = int(var1)
len_of_side = int(var2)
angle = 360.0 / num_of_side

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']
c_choice = (num_of_side + len_of_side) % len(colors)

t.begin_fill()
t.color(colors[c_choice])
t.pensize(5)

for i in range(num_of_side):
    t.forward(len_of_side)
    t.left(angle)

t.end_fill()

t.done()
