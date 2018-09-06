
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

# NumPy Basics 

## NumPy 는 Numerical Python 의 줄임말 
> NumPy 제공 기능
- 빠르고 메모리를 효율적으로 사용하며 벡터 산술연산과 세련된 브로드캐스팅 기능을 제공하는 다차원 배열인 ndarray
- 반복문을 작성할 필요 없이 전체 데이터 배열에 대해 빠른 연산을 제공하는 표준 수학 함수
- 배열 데이터를 디스크에 쓰거나 읽을 수 있는 도구와 메모리에 올려진 파일을 사용하는 도구
- 선형대수, 난수발생기, 푸리에 변환 기능
- C, C++, FORTRAN으로 쓰여진 코드를 통합하는 도구


```python
from numpy.random import randn
import numpy as np
```

## 1. The NumPy ndarray: a multidimensional array object
> 다차원 배열 객체


```python
data = randn(2, 3)
data
```




    array([[-0.0453,  0.3064,  1.4114],
           [ 1.1325,  0.7301, -0.3046]])




```python
data * 10
```




    array([[ -0.4534,   3.0639,  14.1139],
           [ 11.3249,   7.3005,  -3.0462]])




```python
data + data
```




    array([[-0.0907,  0.6128,  2.8228],
           [ 2.265 ,  1.4601, -0.6092]])




```python
data
```




    array([[-0.0453,  0.3064,  1.4114],
           [ 1.1325,  0.7301, -0.3046]])




```python
data.shape
```




    (2, 3)




```python
data.dtype
```




    dtype('float64')



### <font color='brown'> Creating ndarrays </font>


```python
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr1
```




    array([ 6. ,  7.5,  8. ,  0. ,  1. ])




```python
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2
```




    array([[1, 2, 3, 4],
           [5, 6, 7, 8]])




```python
arr2.ndim
```




    2




```python
arr2.shape
```




    (2, 4)




```python
arr1.dtype
```




    dtype('float64')




```python
arr2.dtype
```




    dtype('int32')




```python
np.zeros(10)
```




    array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])




```python
np.zeros((3, 6))
```




    array([[ 0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.]])




```python
np.empty((2, 3, 2))
```




    array([[[  7.2632e-312,   3.1620e-322],
            [  0.0000e+000,   0.0000e+000],
            [  0.0000e+000,   5.7567e-066]],
    
           [[  2.1462e+184,   1.3497e+161],
            [  5.0434e+174,   3.7982e+175],
            [  5.6963e-038,   2.4923e+180]]])



<font color='blue'>
[Tip] np.empty
<br> np.empty는 0으로 초기화된 배열을 반환하지 않는다. 
<br> 대부분 empty는 초기화되지 않은 값으로 채워진 배열을 반환한다.


```python
np.arange(15)
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])



### <font color='brown'> Data Types for ndarrays </font>


```python
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr1.dtype
```




    dtype('float64')




```python
arr2 = np.array([1, 2, 3], dtype=np.int32)
arr2.dtype
```




    dtype('int32')




```python
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
```




    dtype('int32')




```python
float_arr = arr.astype(np.float64)
float_arr.dtype
```




    dtype('float64')




```python
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr
```




    array([  3.7,  -1.2,  -2.6,   0.5,  12.9,  10.1])



<font color='blue'>
[Tip] astype
<br> astype을 호출하면 새로운 dtype이 이전 dtype과 같아도 항상 새로운 배열을 생성(데이터를 복사)한다.
<br> float64나 float32 같은 부동소수점은 근사값이라는 사실을 염두에 두는게 중요하다.


```python
# astype 을 사용하여 숫자로 변환
arr.astype(np.int32)
```




    array([ 3, -1, -2,  0, 12, 10])




```python
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)
```




    array([  1.25,  -9.6 ,  42.  ])




```python
int_array = np.arange(10)
int_array
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
calibers
```




    array([ 0.22 ,  0.27 ,  0.357,  0.38 ,  0.44 ,  0.5  ])




```python
int_array.astype(calibers.dtype)
```




    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])




```python
# u4는 uint32와 동일
empty_uint32 = np.empty(8, dtype='u4')
empty_uint32
```




    array([0, 0, 0, 0, 0, 0, 0, 0], dtype=uint32)



### <font color='brown'> Operations between arrays and scalars </font>
> 배열과 스칼라간의 연산


```python
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr
```




    array([[ 1.,  2.,  3.],
           [ 4.,  5.,  6.]])




```python
arr * arr
```




    array([[  1.,   4.,   9.],
           [ 16.,  25.,  36.]])




```python
arr - arr
```




    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])




```python
1 / arr
```




    array([[ 1.    ,  0.5   ,  0.3333],
           [ 0.25  ,  0.2   ,  0.1667]])




```python
arr ** 0.5
```




    array([[ 1.    ,  1.4142,  1.7321],
           [ 2.    ,  2.2361,  2.4495]])



### <font color='brown'> Basic indexing and slicing </font>
> 색인과 슬라이싱 기초


```python
arr = np.arange(10)
arr
# arr[5]
# arr[5:8]
# arr[5:8] = 12
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
arr[5]
```




    5




```python
arr[5:8]
```




    array([5, 6, 7])




```python
arr[5:8] = 12
```


```python
arr
```




    array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])




```python
arr_slice = arr[5:8]
arr_slice
```




    array([12, 12, 12])




```python
arr_slice[1] = 12345
arr
```




    array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,     9])




```python
arr_slice[:] = 64
arr
```




    array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])



<font color='blue'>
[Tip] 슬라이스 복사본
<br> 만약에 뷰 대신 ndarray 슬라이스의 복사본을 얻고 싶다면 arr[5:8].copy()를 사용해서 명시적으로 배열을 복사하면 된다.

### 2차원 배열

#### NumPy 배열에서 요소 색인하기
<img src="./images/Figure4-1.png">

<font color='brown'>


```python
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
```




    array([7, 8, 9])




```python
arr2d[0][2]
```




    3




```python
arr2d[0, 2]
```




    3



### 3차원 배열


```python
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr3d[0]
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
old_values = arr3d[0].copy()
old_values
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
arr3d[0] = 42
arr3d

```




    array([[[42, 42, 42],
            [42, 42, 42]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr3d[0] = old_values
arr3d
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr3d[1, 0]
```




    array([7, 8, 9])



### <font color='brown'> Indexing with slices </font>
> 슬라이스 색인


```python
arr
```




    array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])




```python
arr[1:6]
```




    array([ 1,  2,  3,  4, 64])



#### 2차원 배열 슬라이싱
<img src="./images/Figure4-2.png">


```python
arr2d
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])




```python
arr2d[:2]
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
arr2d[:2, 1:]
```




    array([[2, 3],
           [5, 6]])




```python
arr2d[1, :2]
```




    array([4, 5])




```python
arr2d[2, :1]
```




    array([7])




```python
arr2d[:, :1]
```




    array([[1],
           [4],
           [7]])




```python
arr2d[:2, 1:] = 0
```


```python
arr2d
```




    array([[1, 0, 0],
           [4, 0, 0],
           [7, 8, 9]])



### <font color='brown'> Boolean indexing </font>
> 불리언 색인


```python
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names
```




    array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], 
          dtype='<U4')




```python
data = randn(7, 4)
data
```




    array([[ 0.8584,  1.6698,  0.4934, -0.2145],
           [ 0.9081,  0.0017, -0.8361,  1.8122],
           [-1.6222, -0.6698, -1.4189, -1.0957],
           [-0.6082, -1.4673,  1.7697,  0.0724],
           [ 0.8184, -0.2183, -0.5236, -1.072 ],
           [-0.4936, -0.0068,  0.2073, -1.7294],
           [ 0.8147,  1.5524, -0.0186,  0.8183]])




```python
names == 'Bob'
```




    array([ True, False, False,  True, False, False, False], dtype=bool)




```python
data[names == 'Bob']
```




    array([[ 0.8584,  1.6698,  0.4934, -0.2145],
           [-0.6082, -1.4673,  1.7697,  0.0724]])




```python
data[names == 'Bob', 2:]
```




    array([[ 0.4934, -0.2145],
           [ 1.7697,  0.0724]])




```python
data[names == 'Bob', 3]
```




    array([-0.2145,  0.0724])




```python
names != 'Bob'
```




    array([False,  True,  True, False,  True,  True,  True], dtype=bool)




```python
data[-(names == 'Bob')]
```

    C:\Python\Anaconda3-44\lib\site-packages\ipykernel_launcher.py:1: DeprecationWarning: numpy boolean negative, the `-` operator, is deprecated, use the `~` operator or the logical_not function instead.
      """Entry point for launching an IPython kernel.
    




    array([[ 0.9081,  0.0017, -0.8361,  1.8122],
           [-1.6222, -0.6698, -1.4189, -1.0957],
           [ 0.8184, -0.2183, -0.5236, -1.072 ],
           [-0.4936, -0.0068,  0.2073, -1.7294],
           [ 0.8147,  1.5524, -0.0186,  0.8183]])



<font color='blue'>
[Tip] NumPy Boolean Negative
<br> '-' 연산자는 사용하지 않으며, ~  혹은 Logical Not 함수를 대신 사용한다.


```python
data[~(names == 'Bob')]
```




    array([[ 0.9081,  0.0017, -0.8361,  1.8122],
           [-1.6222, -0.6698, -1.4189, -1.0957],
           [ 0.8184, -0.2183, -0.5236, -1.072 ],
           [-0.4936, -0.0068,  0.2073, -1.7294],
           [ 0.8147,  1.5524, -0.0186,  0.8183]])




```python
data[ (names != 'Bob')]
```




    array([[ 0.9081,  0.0017, -0.8361,  1.8122],
           [-1.6222, -0.6698, -1.4189, -1.0957],
           [ 0.8184, -0.2183, -0.5236, -1.072 ],
           [-0.4936, -0.0068,  0.2073, -1.7294],
           [ 0.8147,  1.5524, -0.0186,  0.8183]])




```python
data
```




    array([[ 0.8584,  1.6698,  0.4934, -0.2145],
           [ 0.9081,  0.0017, -0.8361,  1.8122],
           [-1.6222, -0.6698, -1.4189, -1.0957],
           [-0.6082, -1.4673,  1.7697,  0.0724],
           [ 0.8184, -0.2183, -0.5236, -1.072 ],
           [-0.4936, -0.0068,  0.2073, -1.7294],
           [ 0.8147,  1.5524, -0.0186,  0.8183]])




```python
mask = (names == 'Bob') | (names == 'Will')
mask
```




    array([ True, False,  True,  True,  True, False, False], dtype=bool)




```python
data[mask]
```




    array([[ 0.8584,  1.6698,  0.4934, -0.2145],
           [-1.6222, -0.6698, -1.4189, -1.0957],
           [-0.6082, -1.4673,  1.7697,  0.0724],
           [ 0.8184, -0.2183, -0.5236, -1.072 ]])




```python
data[data < 0] = 0
data
```




    array([[ 0.8584,  1.6698,  0.4934,  0.    ],
           [ 0.9081,  0.0017,  0.    ,  1.8122],
           [ 0.    ,  0.    ,  0.    ,  0.    ],
           [ 0.    ,  0.    ,  1.7697,  0.0724],
           [ 0.8184,  0.    ,  0.    ,  0.    ],
           [ 0.    ,  0.    ,  0.2073,  0.    ],
           [ 0.8147,  1.5524,  0.    ,  0.8183]])




```python
data[names != 'Joe'] = 7
data
```




    array([[ 7.    ,  7.    ,  7.    ,  7.    ],
           [ 0.9081,  0.0017,  0.    ,  1.8122],
           [ 7.    ,  7.    ,  7.    ,  7.    ],
           [ 7.    ,  7.    ,  7.    ,  7.    ],
           [ 7.    ,  7.    ,  7.    ,  7.    ],
           [ 0.    ,  0.    ,  0.2073,  0.    ],
           [ 0.8147,  1.5524,  0.    ,  0.8183]])



### <font color='brown'> Fancy indexing </font>
> 팬시 색인
- 팬시 색인은 정수 배열을 사용한 색인을 설명하기 위해 NumPy에서 차용한 단어다.


```python
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
arr
```




    array([[ 0.,  0.,  0.,  0.],
           [ 1.,  1.,  1.,  1.],
           [ 2.,  2.,  2.,  2.],
           [ 3.,  3.,  3.,  3.],
           [ 4.,  4.,  4.,  4.],
           [ 5.,  5.,  5.,  5.],
           [ 6.,  6.,  6.,  6.],
           [ 7.,  7.,  7.,  7.]])



> 
- 특정한 순서로  로우를 선택하고 싶다면, 그냥 원하는 순서가 명시된 정수가 담긴 ndarray나 리스트를 넘기면 된다.


```python
arr[[4, 3, 0, 6]]
```




    array([[ 4.,  4.,  4.,  4.],
           [ 3.,  3.,  3.,  3.],
           [ 0.,  0.,  0.,  0.],
           [ 6.,  6.,  6.,  6.]])




```python
arr[[-3, -5, -7]]
```




    array([[ 5.,  5.,  5.,  5.],
           [ 3.,  3.,  3.,  3.],
           [ 1.,  1.,  1.,  1.]])



> 
- 다차원 색인 배열을 넘기는 것은 조금 다르게 동작
- 각각의 색인 튜를에 대응하는 1차원 배열을 선택한 후, reshape 시킨다.


```python
# more on reshape in Chapter 12
arr = np.arange(32).reshape((8, 4))
arr
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15],
           [16, 17, 18, 19],
           [20, 21, 22, 23],
           [24, 25, 26, 27],
           [28, 29, 30, 31]])



> 
- (1, 0), (5, 3), (7, 1), (2, 2) 에 대응하는 요소 선택


```python
arr[[1, 5, 7, 2], [0, 3, 1, 2]]
```




    array([ 4, 23, 29, 10])




```python
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
```




    array([[ 4,  7,  5,  6],
           [20, 23, 21, 22],
           [28, 31, 29, 30],
           [ 8, 11,  9, 10]])




```python
arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]
```




    array([[ 4,  7,  5,  6],
           [20, 23, 21, 22],
           [28, 31, 29, 30],
           [ 8, 11,  9, 10]])



### <font color='brown'> Transposing arrays and swapping axes </font>
> 배열 전치와 축 바꾸기
- 배열 전치는 데이터를 복사하지 않고 데이터 모양이 바뀐 뷰를 반환하는 특별한 기능
- ndarray는 transpose 메소드와 T라는 이름의 특수한 속성을 가진다.
- 다차원 배열의 경우 transpose 메소드는 튜플로 축 번호를 받아서 치환한다.


```python
arr = np.arange(15).reshape((3, 5))
arr
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])




```python
arr.T
```




    array([[ 0,  5, 10],
           [ 1,  6, 11],
           [ 2,  7, 12],
           [ 3,  8, 13],
           [ 4,  9, 14]])




```python
arr = np.random.randn(6, 3)
arr
```




    array([[-1.797 ,  1.6269,  1.03  ],
           [-0.2503, -1.3112, -1.2814],
           [ 1.0662, -1.2736, -0.1101],
           [-0.7869,  2.1681,  0.7224],
           [-1.6   ,  1.3376,  1.0532],
           [ 1.2421, -0.0666, -2.3197]])




```python
np.dot(arr.T, arr)
```




    array([[  9.1509,  -7.8824,  -6.7825],
           [ -7.8824,  12.4827,   6.6257],
           [ -6.7825,   6.6257,   9.7273]])




```python
arr = np.arange(16).reshape((2, 2, 4))
arr
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7]],
    
           [[ 8,  9, 10, 11],
            [12, 13, 14, 15]]])




```python
arr.transpose((1, 0, 2))
```




    array([[[ 0,  1,  2,  3],
            [ 8,  9, 10, 11]],
    
           [[ 4,  5,  6,  7],
            [12, 13, 14, 15]]])




```python
arr
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7]],
    
           [[ 8,  9, 10, 11],
            [12, 13, 14, 15]]])




```python
arr.swapaxes(1, 2)
```




    array([[[ 0,  4],
            [ 1,  5],
            [ 2,  6],
            [ 3,  7]],
    
           [[ 8, 12],
            [ 9, 13],
            [10, 14],
            [11, 15]]])



<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
