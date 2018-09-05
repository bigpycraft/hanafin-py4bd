# dir() : 클래스 내부에 들어있는 객체들을 확인하는 명령문
class MyCountry:
    country = 'Korea'

result = dir(MyCountry)
print(result)

num = 0
for internal_element in result:
    num += 1
    print(num, internal_element)