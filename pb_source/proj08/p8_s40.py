# add ( 더한다 )

# add2(10, 20) => 30
# add2(10, 20, 30) => 60

# add3([10, 20, 30]) => 60

def add(a, b):
    return a + b

def add2(a, b, c):
    return a + b + c

def add3(numbers):  # 숫자 리스트를 받아서, 합을 리턴하는 함수
    sum = 0
    for num in numbers:
        sum += num
    return sum


print(add(10, 20))
print(add2(10, 20, 30))
print(add3([10, 20, 30, 40]))

