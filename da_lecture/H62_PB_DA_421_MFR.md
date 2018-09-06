
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## Lambda Operator

### <font color='blue'>일반 함수</font>


```python
def hello():
    return "Hey guys, Let's get it !"
```


```python
hello()
```




    "Hey guys, Let's get it !"




```python
def double(x):
    return x * 2
```


```python
double(100)
```




    200



### <font color='blue'>람다 함수</font>


```python
(lambda x: x * 2)
```




    <function __main__.<lambda>>




```python
(lambda x: x * 2)(200)
```




    400




```python
# 익명 함수를 만들어서, 그 위치를 double2 이라는 변수에 저장
double2 = lambda x: x * 2
```


```python
double2(300)
```




    600




```python
double2    
```




    <function __main__.<lambda>>



### <font color='brown'>Missions</font>
> 
#### 미션1 : 리스트를 받아서, 제곱수의 리스트  
- Input: 1부터 10까지의 자연수 ⇒ Output : [ 1, 4, 9, ..., 100 ] 
> 
#### 미션2 : 리스트를 받아서, 양수인 element 만 새로운 리스트 
- Input: [1, -2, 3, -4, 5] ⇒ Output : [1, 3, 5]

### <font color='blue'>미션1</font>


```python
def get_square(number):
    return number ** 2

def get_square_list(numbers):
    elements = []
    for number in numbers:
        elements.append(get_square(number))
    return elements

```


```python
numbers = list(range(1, 11))
get_square_list(numbers)
```




    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



### <font color='blue'>미션2</font>


```python
def get_positive_list(numbers):
    elements = []
    for number in numbers:
        if number > 0:
            elements.append(number)
    return elements    
```


```python
numbers = [1, -2, 3, -4, 5]
get_positive_list(numbers)
```




    [1, 3, 5]



# Map, Filter, Reduce

### <font color='blue'>map</font>
> 
- 입력값과 출력값이 1:1로 맵핑된다.
- 즉, 한번만에 즉시 연산
- cf. generator => 한번에 연산 X


```python
list(map(  
    get_square,         
    [1, 2, 3, 4, 5],
))
```




    [1, 4, 9, 16, 25]




```python
list(map(
    lambda x: x ** 2,
    [1, 2, 3, 4, 5]
))
```




    [1, 4, 9, 16, 25]




```python
def get_square_list(numbers):
    return list(map(lambda x: x ** 2, numbers))

get_square_list([1, 2, 3, 4, 5])
```




    [1, 4, 9, 16, 25]



### <font color='blue'>filter</font>
> 
- 함수: 리스트를 받아서, 양수인 element 만 새로운 리스트 
- input: [1, -2,  3, -4,  5] => [1, 3, 5]


```python
numbers = [1, -2,  3, -4,  5]

list(map(
    lambda x: x > 0,
    numbers,
))   # Boolean List / Boolean Mask, Filtering Mask

list(filter(
    lambda x: x > 0,
    numbers,
))

# map - element func apply
# filter - element func apply, filtering when True ( Filtering Mask )
```




    [1, 3, 5]




```python
def get_positive_list(numbers):
    elements = []
    for number in numbers:
        if number > 0:               # False, False, True, True
            elements.append(number)
    return elements

get_positive_list(numbers)
```




    [1, 3, 5]



 


```python
list(filter(
    lambda x: x > 0,
    numbers,
))

def get_positive_list(numbers):
    return list(filter(lambda x: x > 0, numbers))

get_positive_list([1, -2,  3, -4,  5])


get_positive_list = lambda numbers: list(filter(lambda x: x > 0, numbers))
```


```python
get_positive_list([1, -2,  3, -4,  5])
```




    [1, 3, 5]



### <font color='blue'>reduce</font>
> 
- 입력값을 순차적으로 한개씩 받아서 최종결과값을 갱신한다.


```python
# 1. 리스트를 받아서, 리스트의 숫자들 의 곱 | [1, 2, 3, 4] => 24
# 2. 리스트를 받아서, 리스트 중에서 제일 큰 수 | [-1, 0, 2, 4, 3] => 4
```


```python
# 1. 곱 

def get_multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

get_multiply([1, 2, 3, 4])

# 1, 1, 2, 3, 4
#    1, 2, 3, 4
#       2, 3, 4
#          6, 4
#            24
```




    24




```python
def get_max(numbers):
    result = numbers[0]  # 만약에, 0이라고 했을 때 => 음수의 리스트 
    for number in numbers:
        if result < number:
            result = number
    return result

get_max([3, -1, 5, -6])

# 3, -1, 5, -6
#     3, 5, -6
#        5, -6
#            5
```




    5




```python
# 최종적인 output 
# [init, a, b, c, d, e] => result
```


```python
# reduce - python 2
from functools import reduce
```


```python
def get_bigger(a, b):
    return a if a > b else b

reduce(
    get_bigger,
    [3, -1, 5, -6],
)                     # get_max
```




    5




```python
get_bigger(1, 2)
```




    2




```python
reduce(
    get_bigger,
    [1, 2, 40, 3, -1, 5, -6],
)      
```




    40




```python
def get_bigger(a, b):
    return a if a > b else b

reduce(
    get_bigger,
    [3, -1, 5, -6],
)                     # get_max

reduce(
    lambda x, y: x if x > y else y,
    [3, -1, 5, -6],
)

def get_max(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

get_max([3, -1, 5, -6])

```




    5




```python
# 리스트를 받아서, 모든 엘리먼트를 곱하는 기능

# 1, 1, 2, 3, 4, 5 => 120
```


```python
def multiply(a, b):
    print((a, b))
    return a * b

reduce(
    multiply,
    [1, 2, 3, 4, 5],
    0,               # 기본값!!! (*)
)

```

    (0, 1)
    (0, 2)
    (0, 3)
    (0, 4)
    (0, 5)
    




    0




```python
# 1. map      - apply
# 2. filter   - apply, True
# 3. reduce   - apply(a,b)
```

### <font color='blue'>실습. Histogram 함수 작성해보기</font>
> 리스트를 받아서, 히스토그램을 그리는 함수
- 입력값 : ["cat", "cat", "cat", "sheep", "sheep", "duck", "duck", "duck", "duck" ]
### 1. 히스토그램을 그리는 함수 
###  input: {'cat': 3, 'duck': 4, 'sheep': 2} => output: 그림 

### 2. 리스트를 받아서, 숫자를 세는 함수
###  input: list => output: histogram dict

```python
data = ["cat", "cat", "cat", "sheep", "sheep", "duck", "duck", "duck", "duck" ]
```


```python
result_dict = {'cat': 3, 'duck': 4, 'sheep': 2}
result_hist = """
  dog   ====
  cat   ==
  bird  ===
"""

print(result_dict)
print('-'*40, result_hist)
```

    {'cat': 3, 'duck': 4, 'sheep': 2}
    ---------------------------------------- 
      dog   ====
      cat   ==
      bird  ===
    
    

### # 각자 reduce를 활용하여  아래와 같은 Histogram이 출력되도록 함수를 구현해보세요 !!!


```python
def draw_histogram(data):
    pass
    pass
    pass
```


```python
draw_histogram(data)
```

    cat    ===
    sheep  ==
    duck   ====
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
