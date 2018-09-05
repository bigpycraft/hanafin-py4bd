
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>에러와 예외처리, Errors & Exceptions</font>
>  
- 구문 에러, Syntax Errors
- 예외, Exceptions
- try-except 구문으로 예외상황 제어, Handling Exceptions
- else와 finally 활용하기
- 사용자 정의 예외, User-defined Exceptions!

### 구문 에러, Syntax Errors


```python
# print() 함수의 괄호 누락
print 'I can do coding with python. Wow~~~'
```


      File "<ipython-input-1-c0abefaa7ede>", line 2
        print 'I can do coding with python. Wow~~~'
                                                  ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print('I can do coding with python. Wow~~~')?
    



```python
# 콜론(:) 누락
if 1>0
    print("1은 0보다 크다.")
```


      File "<ipython-input-2-0c27e6b29d97>", line 2
        if 1>0
              ^
    SyntaxError: invalid syntax
    



```python
# 들여쓰기 실수
if 1>0:
    print('1은 0보다 크다.')
  print('당연하쥐!')
```


      File "<tokenize>", line 4
        print('당연하쥐!')
        ^
    IndentationError: unindent does not match any outer indentation level
    


### 예외, Exceptions


```python
# 정의하지 않은 변수 stragne 호출
print(strange)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-20527d0147e7> in <module>()
          1 # 정의하지 않은 변수 stragne 호출
    ----> 2 print(strange)
    

    NameError: name 'strange' is not defined



```python
# 숫자와 문자열의 덧셈, 불가하다.
2 + '2'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-abdd20d17bfa> in <module>()
          1 # 숫자와 문자열의 덧셈, 불가하다.
    ----> 2 2 + '2'
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'


### try-except 구문으로 예외상황 제어, Exceptions Handling


```python
# 예외상황 테스트를 위한 함수
def exception_test():
    print("[1] Can you add 2 and '2' in python? ")
    print("[2] Try it~! ", 2+'2')     # 예외 발생
    print("[3] It's not possible to add integer and string together. ")
    
exception_test()
```

    [1] Can you add 2 and '2' in python? 
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-c971d69df651> in <module>()
          5     print("[3] It's not possible to add integer and string together. ")
          6 
    ----> 7 exception_test()
    

    <ipython-input-6-c971d69df651> in exception_test()
          2 def exception_test():
          3     print("[1] Can you add 2 and '2' in python? ")
    ----> 4     print("[2] Try it~! ", 2+'2')     # 예외 발생
          5     print("[3] It's not possible to add integer and string together. ")
          6 
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
# 예외상황에 대한 처리를 구현한 함수
def exception_test2():
    print("[1] Can you add 2 and '2' in python? ")
    
    try:
        print("[2] Try it~! ", 2+'2')     # TypeError 발생
    except TypeError:
        print("[2] I got TypeError! ")    # 에러 메시지 출력
    
    
    print("[3] It's not possible to add integer and string together. ")
    
exception_test2()
```

    [1] Can you add 2 and '2' in python? 
    [2] I got TypeError! 
    [3] It's not possible to add integer and string together. 
    


```python
# 예외상황에 대한 에러메시지를 상세히 나타낸 함수
def exception_test3():
    print("[1] Can you add 2 and '2' in python? ")
    
    try:
        print("[2] Try it~! ", 2+'2')     # TypeError 발생
    except TypeError as err:
        print("[2] TypeError: {}".format(err))    # 에러 메시지 출력
    
    
    print("[3] It's not possible to add integer and string together. ")
    
exception_test3()
```

    [1] Can you add 2 and '2' in python? 
    [2] TypeError: unsupported operand type(s) for +: 'int' and 'str'
    [3] It's not possible to add integer and string together. 
    


```python
import traceback 

# 처음에 보았던 트레이스백 메시지와 함께 나타낸 함수
def exception_test4():
    print("[1] Can you add 2 and '2' in python? ")
    
    try:
        print("[2] Try it~! ", 2+'2')     # TypeError 발생
    except TypeError:
        print("[2] I got TypeError! Check below! ")    # 에러 메시지 출력
        traceback.print_exc()                          # 트레이스백 메시지 출력
    
    print("[3] It's not possible to add integer and string together. ")
    
exception_test4()
```

    [1] Can you add 2 and '2' in python? 
    [2] I got TypeError! Check below! 
    [3] It's not possible to add integer and string together. 
    

    Traceback (most recent call last):
      File "<ipython-input-9-c6979eb4973d>", line 8, in exception_test4
        print("[2] Try it~! ", 2+'2')     # TypeError 발생
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
