# 인자값, 반환값 없는 함수
def my_func1():
    print('  Func1 :: 함수1 시작')
    pass
    print('  Func1 :: 함수1 실행')
    pass
    print('  Func1 :: 함수1 끝')

def my_func2():
    print('  Func2 :: 함수2 시작')
    my_func1()
    print('  Func2 :: 함수2 끝')

print('Main___ :: 함수호출 전')
my_func2()
print('Main___ :: 함수실행 후')
