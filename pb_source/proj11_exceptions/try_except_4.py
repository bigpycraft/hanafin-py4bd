import  traceback
# 예외상황 테스트를 위한 함수
def exception_test4():

    try:
        print("[1] Can you add 2 and '2' in python? ")
        print("[2] Try it~! ", 2 + '2')  # 예외 발생
        print("[3] It's not possible to add integer and string together. ")
    except Exception as err:
        print('TypeError 발생 : {}'.format(err))
        # traceback.print_exc()

    finally:
        print('마지막 정리!!')



exception_test4()