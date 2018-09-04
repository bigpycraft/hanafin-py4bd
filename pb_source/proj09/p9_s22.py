# 클래스 초기화 함수, __init__() 재정의
class MyClass:
    def __init__(self, name):     # 초기화 함수 재정의
        self.name = name

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        print(hello)

# 객체 생성, 인스턴스화
# myClass = MyClass()
myClass = MyClass('채영')
myClass.sayHello()
