# Keyword Arguments, 키워드 인자 활용하기
def introduceMyCar(brand, seats=4, type='세단'):
    print('나의 차는 {b} {s}인승 {t}이다'.format(
        b = brand,
        s = seats,
        t = type
    ))
    # print('나의 차는', brand, '의', seats, '인승', type, '이다')

# 위치 인자 값 1개
introduceMyCar('아우디')

# 키워드 인자 값 1개
introduceMyCar(brand='렉서스')

# 위치 인자 값 1개, 키워드 인자 값 1개, 혼용으로 사용 가능
introduceMyCar('제규어', seats=2)

# 키워드 인자 값 2개
introduceMyCar(brand='머큐리', type='머슬카')

# 순서 바뀐 키워드 인자 값2개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용
introduceMyCar(type='미니벤', brand='카니발')

# 순서를 지킨 위치 인자 값 3개, 순서가 같다면 모두 위치 인지 값 사용 가능
introduceMyCar('카니발', 9, '미니벤')

# 순서 바뀐 키워드 인자 값3개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용
introduceMyCar('쉐보레', type='SUV ', seats=7)



