# 함수 호출1
def exchangeUSDtoKRW(dollar):
    won = dollar * 1065
    return won

usd = 2000
krw = exchangeUSDtoKRW(usd)
print('환전한 금액은 %d 원 입니다.'%(krw))

# krw = exchangeUSDtoKRW()
# print('환전한 금액은 %d 원 입니다.'%(krw))

