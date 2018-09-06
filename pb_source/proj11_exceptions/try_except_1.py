# 예외상황 테스트를 위한 함수
def exception_test():
    print("[1] Can you add 2 and '2' in python? ")
    print("[2] Try it~! ", 2 + '2')  # 예외 발생
    print("[3] It's not possible to add integer and string together. ")


exception_test()