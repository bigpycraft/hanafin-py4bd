# 클래스 정의 : OK
class MyClass:
    name = '찬영'

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        return hello


myClass = MyClass()
obj_name = myClass.name
obj_method = myClass.sayHello()

print('Object name   :', obj_name)
print('Object method :', obj_method)

