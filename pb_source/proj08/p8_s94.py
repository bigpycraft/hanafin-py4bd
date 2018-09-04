import turtle as t

# 마우스클릭으로 이어그리기
t.speed(1)
t.pensize(5)
t.shape("turtle")

# t.hideturtle()
t.onscreenclick(t.goto)
t.mainloop()
