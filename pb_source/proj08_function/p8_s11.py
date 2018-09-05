# 함수 생성1
def add_txt(arg1, arg2):
    print(arg1, arg2)

param1 = '대~한민국~'
param2 = '짝짝~짝~ 짝.짝!!'
add_txt(param1, param2)

# 함수 생성2
def add_num(num1, num2):
    result = num1 + num2
    return result

param1 = 40
param2 = 50
sum = add_num(param1, param2)
print('%d와 %d의 합은 %d입니다.' % (param1, param2, sum))