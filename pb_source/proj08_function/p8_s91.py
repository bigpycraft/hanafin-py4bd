def calculator(type, num1=0, num2=0):
    result = 0
    if type == '+':
        result = sum(num1, num2)
    else:
        print('잘못된 기호입니다!!!')
        result = 'Error!!!'
    return result

result = sum('+', 9, 8)
print('계산값:', result)
