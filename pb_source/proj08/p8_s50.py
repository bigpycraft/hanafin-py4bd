# 지역변수와 전역변수
param   = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print('func1.strdata = %s, id = %d' % (strdata, id(strdata)))

def func2(param):
    param = 20
    print('func2.param = %d, id = %d' % (param, id(param)))

def func3():
    global param
    param = 30
    print('func3.param = %d, id = %d' % (param, id(param)))

func1()
print('main1.strdata = %s, id = %d' % (strdata, id(strdata)))

print('-'*50)
func2(param)
print('main2.param = %d, id = %d' % (param, id(param)))

print('-'*50)
func3()
print('main3.param = %d, id = %d' % (param, id(param)))