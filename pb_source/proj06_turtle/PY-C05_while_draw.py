import turtle as t

# 좌,우,상,하 = A,D,W,S
print('거북이를 키보드로 움직여 보아요')
print('\tA : 왼쪽으로 이동')
print('\tD : 오른쪽으로 이동')
print('\tW : 위쪽으로 이동')
print('\tS : 아래쪽으로 이동')
print('\tX : 프로그램 종료')

input('엔터키를 누르면 시작합니다!')
t.shape("turtle")
t.pensize(5)
t.color('green')
t.speed(1500)

while True:
    direction = input('[A,S,D,F] :')
    if 'X' == direction.upper():
        break
    elif 'D' == direction.upper():
        t.setheading(0)
    elif 'W' == direction.upper():
        t.setheading(90)
    elif 'A' == direction.upper():
        t.setheading(180)
    elif 'S' == direction.upper():
        t.setheading(270)
    else:
        continue

    t.forward(50)

print('\n프로그램을 종료하였습니다!')
t.done()
