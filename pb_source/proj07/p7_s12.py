# 팩토리얼 표: 0~100 까지의 Factorial Table
idx, gop, sum  = 0, 0, 0
factorial = [ ]
total_sum = [ ]

# 입력값 확인
# num_check = list(range(10))
num_chk_list = list('0123456789')
# print(num_chk_list)

while True:
    key_in = input('숫자를 입력해 주세요.[1~100] => ')
    chk_num = True
    for char in key_in:
        is_num = char in num_chk_list
        chk_num *= is_num
        if not is_num:
            break
        # print(char, is_num, chk_num)

    if chk_num:
        last_num = int(key_in)
        print('입력한 숫자 :', last_num)
        break
    else:
        print('입력한 값이 숫자가 아닙니다.')

# print('숫자확인 완료!')
# last_num = 10

# 입력값이 숫자인 경우, 미션 수행
title =  str(last_num) + ' 까지의 합계 및 팩토리얼 테이블 구하기!!'
print('-'*50)
print(title)
print('-'*50)

numbers = list(range(last_num+1))
# print('numbers :', numbers)

while idx < len(numbers):
    num = numbers[idx]
    sum += num
    gop *= num

    gop = 1 if gop<1 else gop
    # if gop < 1:
    #     gop = 1

    total_sum.append(sum)
    factorial.append(gop)
    idx += 1

print(last_num, '까지의 합계는', total_sum[-1], '입니다.')
print('아래는 팩토리얼 테이블입니다.')
for fact_num in range(len(factorial)):
    print(str(fact_num)+'!\t= ', factorial[fact_num])
