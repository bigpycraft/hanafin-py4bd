
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>파일 입출력, File I/O</font>


```python
fp = open('./data/hello.txt', 'r')
```


```python
fp.read()
```




    'Hello, Jupyter !!'




```python
fp.close()
```


```python
fp.read()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-4-5b707e20d623> in <module>()
    ----> 1 fp.read()
    

    ValueError: I/O operation on closed file.



```python
with open('./data/hello.txt', 'r') as fp:
    data = fp.read()
    print(data)
```

    Hello, Jupyter !!
    


```python
data
```




    'Hello, Jupyter !!'




```python
with open('./data/subject.txt', 'w') as fp:
    data = '파이썬을 이용한 빅데이터 분석!!'
    fp.write(data)
```


```python
with open('./data/subject.txt', 'r') as fp:
    data = fp.read()
    print(data)
```

    파이썬을 이용한 빅데이터 분석!!
    
<!--
# students.csv
김태희,서울대,thkim@gmail.com
신민아,성균관대,sma@gmial.com
전지현,중앙대,jhjeon@gmail.com
이영애,숭실대,janggumi@gamil.com
//-->
> <font color='blue'>FileName : students.csv</font>
- 김태희,서울대,thkim@gmail.com
- 신민아,성균관대,sma@gmial.com
- 전지현,중앙대,jhjeon@gmail.com
- 이영애,숭실대,janggumi@gamil.com


```python
def read_csv(filepath):
    
    fp = open(filepath, 'r', encoding='utf-8')
    data = fp.read()
    fp.close()
    
    # return dataL
    elements = []
    
    rows = data.split("\n")
    # print(rows)
    for row in rows:        
        
        fields = row.split(",")
        # print(fields)
        
        element = {   
            "name"   : fields[0],
            "school" : fields[1],
            "email"  : fields[2],
        }
        elements.append(element)
    return elements
```


```python
filepath = 'data/students.csv'
read_csv(filepath)
```




    [{'email': 'thkim@gmail.com', 'name': '김태희', 'school': '서울대'},
     {'email': 'sma@gmial.com', 'name': '신민아', 'school': '성균관대'},
     {'email': 'jhjeon@gmail.com', 'name': '전지현', 'school': '중앙대'},
     {'email': 'janggumi@gamil.com', 'name': '이영애', 'school': '숭실대'}]


<!--
# company.csv
랭킹, 회사이름, 영문명, 창업자
1, 애플, Apple, 스티브잡스
2, 구글, Google, 세르게이브린 & 레리페이지
3, 마이크로소프트, Microsoft, 빌게이츠 & 폴앨런
4, 페이스북, Facebook, 마크쥬크버그
5, 에어비엔비, Airbnb, 브라이언체크키 & 조게비어
//-->
> <font color='blue'>FileName : company.csv</font>
<br>
<br> 랭킹, 회사이름, 영문명, 창업자
<br> 1, 애플, Apple, 스티브잡스
<br> 2, 구글, Google, 세르게이브린 & 레리페이지
<br> 3, 마이크로소프트, Microsoft, 빌게이츠 & 폴앨런
<br> 4, 페이스북, Facebook, 마크쥬크버그
<br> 5, 에어비엔비, Airbnb, 브라이언체크키 & 조게비어


```python
def read_csv(filepath):         # 어떤 헤더가 있는 CSV 파일이든지 읽을 수 있는 함수
                                # "," 말고 다른 어떤 seperator 가 들어가더라도, 
                                # CSV 읽을 수 있는 함수
                                # "\t", "::", "|" 이 모든 sep 에 대한 함수!
    fp = open(filepath, 'r', encoding='utf-8')
    data = fp.read()
    fp.close()
    
    elements = []
    
    rows = data.split("\n")
    columns = rows[0].split(",")    # ["랭킹", "회사이름", "영문명", "창업자"]
    columns = [key.replace(' ','') for key in columns]
    print(columns)
    for row in rows[1:]:
        fields = row.split(",")
        element = {}
        
        for idx in range(len(columns)):   # index 의 값으로 비교해야 한다.
            column = columns[idx]
            field = fields[idx]
            element[column] = field
        
        elements.append(element)
    return elements
```


```python
filepath = 'data/company.csv'
read_csv(filepath)
```

    ['랭킹', '회사이름', '영문명', '창업자']
    




    [{'랭킹': '1', '영문명': ' Apple', '창업자': ' 스티브잡스 ', '회사이름': ' 애플'},
     {'랭킹': '2', '영문명': ' Google', '창업자': ' 세르게이브린 & 레리페이지 ', '회사이름': ' 구글'},
     {'랭킹': '3', '영문명': ' Microsoft', '창업자': ' 빌게이츠 & 폴앨런 ', '회사이름': ' 마이크로소프트'},
     {'랭킹': '4', '영문명': ' Facebook', '창업자': ' 마크쥬크버그 ', '회사이름': ' 페이스북'},
     {'랭킹': '5', '영문명': ' Airbnb', '창업자': ' 브라이언체크키 & 조게비어', '회사이름': ' 에어비엔비'}]



<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
