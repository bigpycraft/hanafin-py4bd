# 구구단 출력
dan = input('출력할 단을 입력해주세요.[2~9] ')
# dan = 5
dan = int(dan)
gop = 0

print(dan, '단 출 력 \n' + '-'*20)
# print(dan, '단 출 력 - Case1\n' + '-'*20)
for i in range(9):
    num = i + 1
    gop = dan * num
    print(dan, '*', num, '=', gop)

#
# print(dan, '단 출 력 - Case2\n' + '-'*20)
# for i in range(9):
#     num = i + 1
#     gop = dan * num
#     print('%d * %d = %d' % (dan, num, gop))
#
# print(dan, '단 출 력 - Case3\n' + '-'*20)
# for i in range(9):
#     num = i + 1
#     gop = dan * num
#     print('{} * {} = {}'.format(dan, num, gop))
#
# print(dan, '단 출 력 - Case4\n' + '-'*20)
# for i in range(9):
#     num = i + 1
#     gop = dan * num
#     print('{d} * {n} = {g}'.format(d=dan, n=num, g=gop))
