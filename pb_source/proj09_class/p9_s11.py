# 클래스 정의 : X
class MyClass:
    name = '찬영'

    def sayHello():
        hello = "Hello, " + name + "\t It's Good day !"
        return hello


myClass = MyClass()
obj_name = myClass.name
obj_method = myClass.sayHello()

print('Object name   :', obj_name)
print('Object method :', obj_method)

