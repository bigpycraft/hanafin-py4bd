# 이름장식 Name Mangling  : __가 있는 것에 한하여 이름을 변경해 버리는 이름 장식 기법
# 변형된 규칙 : _[클래스명]__[변수명]
class MyCountry:
    __country = 'Korea'

result = dir(MyCountry)
print(result)

# 클래스 내부 변형변수는 정의시 사용했던 변수명으로는 접근이 불가능
# MyCountry.__country

num = 0
for internal_element in result:
    num += 1
    print(num, internal_element)


# myCountry = MyCountry()
# my_country = myCountry._MyCountry__country
# print('My country is ', my_country)
