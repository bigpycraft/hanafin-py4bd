# 클래스 정의
class MyClass:
    name = str()

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        print(hello)

# 객체 생성, 인스턴스화
myClass = MyClass()
myClass.name = '준영'
myClass.sayHello()
