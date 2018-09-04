# 클래스 변수와 인스턴스 변수
# 변수의 선언위체 따라 달라지는 유효범위
class MyChildren:
    school = '대학교'       # 클래스변수 country 선언

    def __init__(self, name):     # 초기화 함수 재정의
        self.name   = name        # 인스턴스 변수 name 선언

    def go_to_school(self):
        print(self.name + '이는 ' + self.school + '에 다닙니다.')

# 객체 인스턴스화
myChild  = MyChildren('희영')
myChild1 = MyChildren('찬영')
myChild2 = MyChildren('준영')
myChild3 = MyChildren('채영')

myChild1.school = '고등학교'
myChild2.school = '중학교'
myChild3.school = '초등학교'

# 클래스변수 country 확인
print('myChild0.school : ', myChild.school)
print('myChild1.school : ', myChild1.school)
print('myChild2.school : ', myChild2.school)
print('myChild3.school : ', myChild3.school)

# 클래스함수 호출 (인스턴스 변수 name 출력)
myChild.go_to_school()
myChild1.go_to_school()
myChild2.go_to_school()
myChild3.go_to_school()
