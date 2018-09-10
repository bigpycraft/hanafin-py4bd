
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>공공데이터 활용<font>

### Case1. 30년이상 노후화된 공공시설물현황(공동주택제외)
>  
- [공공시설물] 한국시설안전공단 30년이상 노후화된 공공시설물현황
- https://www.data.go.kr/dataset/15017291/fileData.do


```python
import platform

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.rcParams["figure.figsize"] = [12,6]
%matplotlib inline
```


```python
df = pd.read_csv('data/public_old_buildings_20171016.csv', encoding='EUC-KR')
df.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시설물명</th>
      <th>시설물구분</th>
      <th>시설물소재지</th>
      <th>준공일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>부암1동 동부교육청 입구 옹벽</td>
      <td>옹벽</td>
      <td>부산광역시 부산진구 부암동</td>
      <td>19860510</td>
    </tr>
    <tr>
      <th>1</th>
      <td>전포천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>19801231</td>
    </tr>
    <tr>
      <th>2</th>
      <td>부전천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>19791231</td>
    </tr>
    <tr>
      <th>3</th>
      <td>사당천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 방배동</td>
      <td>19801231</td>
    </tr>
    <tr>
      <th>4</th>
      <td>반포천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 서초동</td>
      <td>19820929</td>
    </tr>
    <tr>
      <th>5</th>
      <td>두구교(구)</td>
      <td>교량</td>
      <td>부산광역시 금정구 두구동</td>
      <td>19660725</td>
    </tr>
    <tr>
      <th>6</th>
      <td>진해1부두</td>
      <td>항만</td>
      <td>경상남도 창원시 진해구 행암동</td>
      <td>19700929</td>
    </tr>
    <tr>
      <th>7</th>
      <td>호형정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 고흥읍</td>
      <td>19820101</td>
    </tr>
    <tr>
      <th>8</th>
      <td>금사정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 포두면</td>
      <td>19790101</td>
    </tr>
    <tr>
      <th>9</th>
      <td>신호정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 도화면</td>
      <td>19850101</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3243 entries, 0 to 3242
    Data columns (total 4 columns):
    시설물명      3243 non-null object
    시설물구분     3243 non-null object
    시설물소재지    3243 non-null object
    준공일자      3243 non-null int64
    dtypes: int64(1), object(3)
    memory usage: 101.4+ KB
    

#### <font color='blue'> # 준공일자 기준으로 정렬 </font>


```python
df.sort_values(by='준공일자', ascending=1).tail(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시설물명</th>
      <th>시설물구분</th>
      <th>시설물소재지</th>
      <th>준공일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1978</th>
      <td>송촌정수장</td>
      <td>상하수도</td>
      <td>대전광역시 대덕구 송촌동</td>
      <td>19870930</td>
    </tr>
    <tr>
      <th>1858</th>
      <td>비전2배수지</td>
      <td>상하수도</td>
      <td>경기도 평택시 매봉산4길</td>
      <td>19871001</td>
    </tr>
    <tr>
      <th>2167</th>
      <td>염포배수지</td>
      <td>상하수도</td>
      <td>울산광역시 북구 염포동</td>
      <td>19871001</td>
    </tr>
    <tr>
      <th>2169</th>
      <td>전하배수지</td>
      <td>상하수도</td>
      <td>울산광역시 동구 봉수로</td>
      <td>19871001</td>
    </tr>
    <tr>
      <th>2165</th>
      <td>무거배수지</td>
      <td>상하수도</td>
      <td>울산광역시 남구 무거동</td>
      <td>19871001</td>
    </tr>
    <tr>
      <th>2168</th>
      <td>성남배수지</td>
      <td>상하수도</td>
      <td>울산광역시 중구 북부순환도로</td>
      <td>19871001</td>
    </tr>
    <tr>
      <th>1561</th>
      <td>강진읍 상수도</td>
      <td>상하수도</td>
      <td>전라남도 강진군 강진읍</td>
      <td>19871002</td>
    </tr>
    <tr>
      <th>1838</th>
      <td>팔마주경기장</td>
      <td>건축물</td>
      <td>전라남도 순천시 팔마로</td>
      <td>19871002</td>
    </tr>
    <tr>
      <th>2224</th>
      <td>광주종합체육관</td>
      <td>건축물</td>
      <td>광주광역시 서구 화정동</td>
      <td>19871005</td>
    </tr>
    <tr>
      <th>270</th>
      <td>순지교</td>
      <td>교량</td>
      <td>전라남도 장흥군 장흥읍</td>
      <td>19871015</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['시설물명', '시설물구분', '시설물소재지', '준공일자'], dtype='object')




```python
type(df['준공일자'][0])
```




    numpy.int64




```python
from datetime import datetime
```

#### <font color='blue'> # 문자열인 준공일자를 Date 객체로 변환 </font>


```python
df['준공일자'] = pd.to_datetime(df['준공일자'], format='%Y%m%d') 
df.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시설물명</th>
      <th>시설물구분</th>
      <th>시설물소재지</th>
      <th>준공일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>부암1동 동부교육청 입구 옹벽</td>
      <td>옹벽</td>
      <td>부산광역시 부산진구 부암동</td>
      <td>1986-05-10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>전포천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1980-12-31</td>
    </tr>
    <tr>
      <th>2</th>
      <td>부전천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1979-12-31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>사당천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 방배동</td>
      <td>1980-12-31</td>
    </tr>
    <tr>
      <th>4</th>
      <td>반포천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 서초동</td>
      <td>1982-09-29</td>
    </tr>
    <tr>
      <th>5</th>
      <td>두구교(구)</td>
      <td>교량</td>
      <td>부산광역시 금정구 두구동</td>
      <td>1966-07-25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>진해1부두</td>
      <td>항만</td>
      <td>경상남도 창원시 진해구 행암동</td>
      <td>1970-09-29</td>
    </tr>
    <tr>
      <th>7</th>
      <td>호형정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 고흥읍</td>
      <td>1982-01-01</td>
    </tr>
    <tr>
      <th>8</th>
      <td>금사정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 포두면</td>
      <td>1979-01-01</td>
    </tr>
    <tr>
      <th>9</th>
      <td>신호정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 도화면</td>
      <td>1985-01-01</td>
    </tr>
  </tbody>
</table>
</div>



#### <font color='blue'> # 준공일자 칼럼을 인덱스로 지정 </font>


```python
df.set_index('준공일자', inplace=True)           
df.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시설물명</th>
      <th>시설물구분</th>
      <th>시설물소재지</th>
    </tr>
    <tr>
      <th>준공일자</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1986-05-10</th>
      <td>부암1동 동부교육청 입구 옹벽</td>
      <td>옹벽</td>
      <td>부산광역시 부산진구 부암동</td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>전포천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
    </tr>
    <tr>
      <th>1979-12-31</th>
      <td>부전천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>사당천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 방배동</td>
    </tr>
    <tr>
      <th>1982-09-29</th>
      <td>반포천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 서초동</td>
    </tr>
    <tr>
      <th>1966-07-25</th>
      <td>두구교(구)</td>
      <td>교량</td>
      <td>부산광역시 금정구 두구동</td>
    </tr>
    <tr>
      <th>1970-09-29</th>
      <td>진해1부두</td>
      <td>항만</td>
      <td>경상남도 창원시 진해구 행암동</td>
    </tr>
    <tr>
      <th>1982-01-01</th>
      <td>호형정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 고흥읍</td>
    </tr>
    <tr>
      <th>1979-01-01</th>
      <td>금사정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 포두면</td>
    </tr>
    <tr>
      <th>1985-01-01</th>
      <td>신호정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 도화면</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    DatetimeIndex: 3243 entries, 1986-05-10 to 1979-08-20
    Data columns (total 3 columns):
    시설물명      3243 non-null object
    시설물구분     3243 non-null object
    시설물소재지    3243 non-null object
    dtypes: object(3)
    memory usage: 101.3+ KB
    

#### <font color='blue'> # 준공일자 인덱스로부터 준공년 컬럼 추가 </font>


```python
df.index.year
```




    Int64Index([1986, 1980, 1979, 1980, 1982, 1966, 1970, 1982, 1979, 1985,
                ...
                1985, 1979, 1987, 1984, 1984, 1984, 1984, 1982, 1986, 1979],
               dtype='int64', name='준공일자', length=3243)




```python
df['준공년'] = df.index.year
df.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시설물명</th>
      <th>시설물구분</th>
      <th>시설물소재지</th>
      <th>준공년</th>
    </tr>
    <tr>
      <th>준공일자</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1986-05-10</th>
      <td>부암1동 동부교육청 입구 옹벽</td>
      <td>옹벽</td>
      <td>부산광역시 부산진구 부암동</td>
      <td>1986</td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>전포천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1980</td>
    </tr>
    <tr>
      <th>1979-12-31</th>
      <td>부전천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1979</td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>사당천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 방배동</td>
      <td>1980</td>
    </tr>
    <tr>
      <th>1982-09-29</th>
      <td>반포천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 서초동</td>
      <td>1982</td>
    </tr>
    <tr>
      <th>1966-07-25</th>
      <td>두구교(구)</td>
      <td>교량</td>
      <td>부산광역시 금정구 두구동</td>
      <td>1966</td>
    </tr>
    <tr>
      <th>1970-09-29</th>
      <td>진해1부두</td>
      <td>항만</td>
      <td>경상남도 창원시 진해구 행암동</td>
      <td>1970</td>
    </tr>
    <tr>
      <th>1982-01-01</th>
      <td>호형정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 고흥읍</td>
      <td>1982</td>
    </tr>
    <tr>
      <th>1979-01-01</th>
      <td>금사정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 포두면</td>
      <td>1979</td>
    </tr>
    <tr>
      <th>1985-01-01</th>
      <td>신호정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 도화면</td>
      <td>1985</td>
    </tr>
  </tbody>
</table>
</div>



#### <font color='blue'> # 연도별 준공건수 </font>


```python
df_year = df['준공년'].value_counts()
df_year.head(10)
```




    1985    338
    1984    269
    1986    233
    1983    196
    1980    188
    1987    167
    1982    130
    1981    128
    1979    128
    1977     92
    Name: 준공년, dtype: int64




```python
df_year.index
```




    Int64Index([1985, 1984, 1986, 1983, 1980, 1987, 1982, 1981, 1979, 1977, 1970,
                1978, 1973, 1975, 1974, 1976, 1969, 1971, 1972, 1963, 1965, 1961,
                1964, 1968, 1955, 1962, 1966, 1945, 1967, 1959, 1960, 1958, 1940,
                1939, 1942, 1938, 1930, 1934, 1937, 1954, 1932, 1957, 1936, 1931,
                1935, 1900, 1944, 1926, 1956, 1914, 1922, 1924, 1949, 1953, 1947,
                1906, 1925, 1943, 1950, 1946, 1929, 1921, 1933, 1923, 1928, 1920,
                1912, 1905, 1941, 1952, 1918, 1951, 1911, 1919, 1915, 1948, 1927],
               dtype='int64')




```python
plt.rcParams["figure.figsize"] = [20,12]
```


```python
df_year.plot(kind='bar')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2da633e44a8>




![png](output/PD_DA_621/output_24_1.png)


#### <font color='blue'> # 연도별로 정렬 </font>


```python
df_year = df_year.sort_index()
df_year.head(10)
```




    1900    11
    1905     2
    1906     5
    1911     1
    1912     2
    1914     7
    1915     1
    1918     1
    1919     1
    1920     2
    Name: 준공년, dtype: int64




```python
df_year.plot(kind='bar')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2da63930080>




![png](output/PD_DA_621/output_27_1.png)



```python
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시설물명</th>
      <th>시설물구분</th>
      <th>시설물소재지</th>
      <th>준공년</th>
    </tr>
    <tr>
      <th>준공일자</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1986-05-10</th>
      <td>부암1동 동부교육청 입구 옹벽</td>
      <td>옹벽</td>
      <td>부산광역시 부산진구 부암동</td>
      <td>1986</td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>전포천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1980</td>
    </tr>
    <tr>
      <th>1979-12-31</th>
      <td>부전천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1979</td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>사당천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 방배동</td>
      <td>1980</td>
    </tr>
    <tr>
      <th>1982-09-29</th>
      <td>반포천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 서초동</td>
      <td>1982</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['시설물소재지'].values[100]
```




    '경기도 가평군 외서면'




```python
tmp = '부산광역시 부산진구 부암동'
```


```python
tmp.find(' ')
```




    5




```python
tmp2 = tmp[0:(tmp.find(' '))]
```


```python
tmp2
```




    '부산광역시'




```python
len(df)
```




    3243




```python
df['시설물소재지'].values[1][0:5]
```




    '부산광역시'




```python
tmp3 = df['시설물소재지'].values[1].find(' ')
```


```python
df['시설물소재지'].values[1][0:tmp3]
```




    '부산광역시'




```python
df['state'] = ' '
df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시설물명</th>
      <th>시설물구분</th>
      <th>시설물소재지</th>
      <th>준공년</th>
      <th>state</th>
    </tr>
    <tr>
      <th>준공일자</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1986-05-10</th>
      <td>부암1동 동부교육청 입구 옹벽</td>
      <td>옹벽</td>
      <td>부산광역시 부산진구 부암동</td>
      <td>1986</td>
      <td></td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>전포천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1980</td>
      <td></td>
    </tr>
    <tr>
      <th>1979-12-31</th>
      <td>부전천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1979</td>
      <td></td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>사당천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 방배동</td>
      <td>1980</td>
      <td></td>
    </tr>
    <tr>
      <th>1982-09-29</th>
      <td>반포천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 서초동</td>
      <td>1982</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



#### <font color='blue'> # 시설물소재지를 시/도별로 구분하는 state 컬럼 추가 </font>


```python
for n in np.arange(len(df)):
    endN = df['시설물소재지'].values[n].find(' ')
    df['state'].values[n] = df['시설물소재지'].values[n][0:endN]
```


```python
df.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시설물명</th>
      <th>시설물구분</th>
      <th>시설물소재지</th>
      <th>준공년</th>
      <th>state</th>
    </tr>
    <tr>
      <th>준공일자</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1986-05-10</th>
      <td>부암1동 동부교육청 입구 옹벽</td>
      <td>옹벽</td>
      <td>부산광역시 부산진구 부암동</td>
      <td>1986</td>
      <td>부산광역시</td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>전포천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1980</td>
      <td>부산광역시</td>
    </tr>
    <tr>
      <th>1979-12-31</th>
      <td>부전천본류 복개구조물</td>
      <td>교량</td>
      <td>부산광역시 부산진구 부전2동</td>
      <td>1979</td>
      <td>부산광역시</td>
    </tr>
    <tr>
      <th>1980-12-31</th>
      <td>사당천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 방배동</td>
      <td>1980</td>
      <td>서울특별시</td>
    </tr>
    <tr>
      <th>1982-09-29</th>
      <td>반포천복개구조물</td>
      <td>교량</td>
      <td>서울특별시 서초구 서초동</td>
      <td>1982</td>
      <td>서울특별시</td>
    </tr>
    <tr>
      <th>1966-07-25</th>
      <td>두구교(구)</td>
      <td>교량</td>
      <td>부산광역시 금정구 두구동</td>
      <td>1966</td>
      <td>부산광역시</td>
    </tr>
    <tr>
      <th>1970-09-29</th>
      <td>진해1부두</td>
      <td>항만</td>
      <td>경상남도 창원시 진해구 행암동</td>
      <td>1970</td>
      <td>경상남도</td>
    </tr>
    <tr>
      <th>1982-01-01</th>
      <td>호형정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 고흥읍</td>
      <td>1982</td>
      <td>전라남도</td>
    </tr>
    <tr>
      <th>1979-01-01</th>
      <td>금사정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 포두면</td>
      <td>1979</td>
      <td>전라남도</td>
    </tr>
    <tr>
      <th>1985-01-01</th>
      <td>신호정수장</td>
      <td>상하수도</td>
      <td>전라남도 고흥군 도화면</td>
      <td>1985</td>
      <td>전라남도</td>
    </tr>
  </tbody>
</table>
</div>



#### <font color='blue'> # 제대로 잘 잘렸는지, unique()를 통해서 확인한다. </font>


```python
df['state'].unique()
```




    array(['부산광역시', '서울특별시', '경상남도', '전라남도', '대구광역시', '전라북도', '인천광역시', '충청북도',
           '강원도', '제주특별자치도', '경기도', '충청남도', '광주광역시', '경상북도', '대전광역시',
           '세종특별자치시', '울산광역시'], dtype=object)



#### <font color='blue'> # 시/도별 준공건수 </font>


```python
df_state = df['state'].value_counts()
df_state
```




    서울특별시      609
    경상북도       454
    경상남도       369
    강원도        244
    경기도        213
    전라남도       210
    충청북도       204
    충청남도       203
    전라북도       187
    부산광역시      160
    대구광역시      105
    광주광역시       92
    대전광역시       59
    인천광역시       55
    울산광역시       53
    세종특별자치시     14
    제주특별자치도     12
    Name: state, dtype: int64




```python
plt.rcParams["figure.figsize"] = [15,15]
df_state.plot(kind='pie')
plt.show()
```


![png](output/PD_DA_621/output_46_0.png)



```python
plt.rcParams["figure.figsize"] = [12,6]
df_state.plot(kind='barh')
plt.show()
```


![png](output/PD_DA_621/output_47_0.png)


#### <font color='blue'> # 내림차순 정렬 </font>


```python
df_state.sort_values(ascending=False).head(5)
```




    서울특별시    609
    경상북도     454
    경상남도     369
    강원도      244
    경기도      213
    Name: state, dtype: int64



#### <font color='blue'> # 오름차순 정렬 </font>


```python
df_state.sort_values(ascending=True).head(5)
```




    제주특별자치도    12
    세종특별자치시    14
    울산광역시      53
    인천광역시      55
    대전광역시      59
    Name: state, dtype: int64



#### <font color='blue'> # 30년이상 노후화된 공공시설물 현황 </font>


```python
plt.figure(figsize=(20,20))

plt.subplot(211) 
plt.title('노후공공시설물 설립년도별 현황')
df_year.plot(kind='bar')

plt.subplot(223) 
plt.title("시도별 노후공공시설 현황")
df_state.plot(kind='pie')

plt.subplot(224)
plt.title("시도별 노후공공시설 순위 TOP10")
df_state.sort_values(ascending=False).head(10).plot(kind='barh', color='y')

plt.show()

```


![png](output/PD_DA_621/output_53_0.png)


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
