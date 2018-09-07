
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## 정규표현식, RegEx ( Regular Expression )


### <font color='brown'> Regular Expression 관련 사이트
- <a href="http://regexr.com/"> Text 정보를 re로 테스트 </a>
- <a href="https://regexper.com/"> 작성된 re를 다이어그램으로 표현 </a>


```python
import re 
```

### <font color='brown'>정규표현식, 문자열에서 패턴찾기</font>


```python
# 테스트용 문자열 저장
text = 'My id number is [G203_5A]'
text
```




    'My id number is [G203_5A]'




```python
# 소문자 a 찾기
result = re.findall('a', text)
result
```




    []




```python
# 대문자 A 찾기
result = re.findall('A', text)
result
```




    ['A']




```python
# 소문자 i 찾기
result = re.findall('i', text)
result
```




    ['i', 'i']




```python
# 소문자 찾기
result = re.findall('[a-z]', text)
result
```




    ['y', 'i', 'd', 'n', 'u', 'm', 'b', 'e', 'r', 'i', 's']




```python
# 소문자 연속해서 찾기
result = re.findall('[a-z]+', text)
result

```




    ['y', 'id', 'number', 'is']




```python
# 대문자 찾기
result = re.findall('[A-Z]', text)
result
```




    ['M', 'G', 'A']




```python
# 숫자 찾기
result = re.findall('[0-9]', text)
result
```




    ['2', '0', '3', '5']




```python
# 숫자 연속해서 찾기
result = re.findall('[0-9]+', text)
result
```




    ['203', '5']




```python
# 영문자 및 숫자 찾기
result = re.findall('[a-zA-Z0-9]', text)
result
```




    ['M',
     'y',
     'i',
     'd',
     'n',
     'u',
     'm',
     'b',
     'e',
     'r',
     'i',
     's',
     'G',
     '2',
     '0',
     '3',
     '5',
     'A']




```python
# 영문자 및 숫자 연속해서 찾기
result = re.findall('[a-zA-Z0-9]+', text)
result
```




    ['My', 'id', 'number', 'is', 'G203', '5A']




```python
# 영문자/숫자 아닌 문자 찾기
result = re.findall('[^a-zA-Z0-9]', text)
result
```




    [' ', ' ', ' ', ' ', '[', '_', ']']




```python
# 영문자 및 '_'특수기호 찾기
result = re.findall('[\w]', text)
result
```




    ['M',
     'y',
     'i',
     'd',
     'n',
     'u',
     'm',
     'b',
     'e',
     'r',
     'i',
     's',
     'G',
     '2',
     '0',
     '3',
     '_',
     '5',
     'A']




```python
# 영문자 및 '_'특수기호 연속해서 찾기
result = re.findall('[\w]+', text)
result
```




    ['My', 'id', 'number', 'is', 'G203_5A']




```python
# 영문자 및 '_'특수기호 아닌 문자 찾기
result = re.findall('[\W]', text)
result
```




    [' ', ' ', ' ', ' ', '[', ']']



### <font color='brown'>문자열에서 특정이름 찾아내기</font>


```python
# \w ( 1 char )
# \d ( 1 decimal )
# \s ( 1 space )

# + ( 1, ..., N )
# ? ( 0, 1 )
# * ( 0, 1, .. N )

# \d{N} ( 숫자가 N개 나온다. )
# \d{N,M} ( 숫자가 N~M개 나온다 )
```


```python
text = """
옛날 옛적에 김진수라는 사람이 살았습니다.
그에게는 5형제가 있었는데, 김진수, 김진구, 김진용, 김진태, 김진욱 이렇게 5명 있었습니다.
그리고 그는 결혼을 해서 김찬영, 김준영, 김채영 3남매를 낳고 행복하게 잘 살았습니다.
"""
# 형제 : 김진O
# 자녀 : 김O영
```


```python
pattern = re.compile("김진\w")
```


```python
brother = pattern.findall(text)
brother
```




    ['김진수', '김진수', '김진구', '김진용', '김진태', '김진욱']




```python
pattern = re.compile("김.영")
pattern = re.compile("김\w영")
```


```python
children = pattern.findall(text)
children
```




    ['김찬영', '김준영', '김채영']




```python
brother = set(brother)
brother
```




    {'김진구', '김진수', '김진용', '김진욱', '김진태'}



### <font color='brown'> 핸드폰 번호에 대한 파싱 </font>
> 
- 010-5670-3847
- 010-오륙칠공-3847
- 공일빵 5670 3팔4칠      
cf. 0.5% 정도는 저런사람 있쥐요~


```python
# ...fly => dragonfly, butterfly
```


```python
text = "A sky, a dragonfly and a butterfly!!!!!"
```


```python
pattern = re.compile("\w+fly")
pattern.findall(text)
```




    ['dragonfly', 'butterfly']




```python
text = """
    010-5670-3847   # space, -, . => []
    010 5670 3847
    010.5670 3847
"""
```


```python
pattern = re.compile("\d{3}[ -.]?\d{4}[ -.]?\d{4}")
```


```python
pattern.findall(text)
```




    ['010-5670-3847', '010 5670 3847', '010.5670 3847']




```python
text = """
    010-5670-3847   # space, -, . => []
    옛날에는 011-1052-3847 이랬는데..
    010 5670 3847
    010.-5670 3847
    사는동네가 자이아파트 516동512호
    그리구, 사무실번호는 02-360-4047이고
    우편번호는 100-791, 청파로 463번지
    
"""
```


```python
pattern = re.compile("\d{3}[ -\.]{1,2}\d{3,4}[ -\.]?\d{4}")
```


```python
pattern.findall(text)
```




    ['010-5670-3847', '011-1052-3847', '010 5670 3847', '010.-5670 3847']




```python
pattern = re.compile("\d{2,3}[ -\.]?\d{3,4}[ -\.]?\d{4}")
```


```python
pattern.findall(text)
```




    ['010-5670-3847', '011-1052-3847', '010 5670 3847', '02-360-4047']




```python
# \w ( 1 char )
# \d ( 1 decimal )
# \s ( 1 space )

# + ( 1, ..., N )
# ? ( 0, 1 )
# * ( 0, 1, .. N )

# \d{N} ( 숫자가 N개 나온다. )
# \d{N,M} ( 숫자가 N~M개 나온다 )
```

### <font color='brown'> 주민등록번호에 대한 파싱 </font>
> 
- 주민등록번호 : 숫자 6자리 - 숫자 7자리 
- 데이터에서 주민등록번호만 찾아서, 뒷자리를 암호화(*******)


```python
text = """
    김찬영 020822-3069110
    김준영 040825-3069115
    김채영 110715-4063111
"""
```


```python
pattern = re.compile("\d{6}-?\d{7}")
```


```python
pattern.findall(text)
```




    ['020822-3069110', '040825-3069115', '110715-4063111']




```python
pattern = re.compile("\d{6}-\d{7}")
# 정규표현식 GROUP
# 1. 생년월일 그룹 <birth>
# 2. 주민등록번호 뒷자리 그룹 <secret>
```


```python
pattern = re.compile("(?P<birth>\d{6})-(?P<secret>\d{7})")

# 김채영 110715-******* => 김채영(110715-*******)
```


```python
pattern.findall(text)
```




    [('020822', '3069110'), ('040825', '3069115'), ('110715', '4063111')]




```python
result = pattern.sub("\g<birth>-*******", text)
print(result)
```

    
        김찬영 020822-*******
        김준영 040825-*******
        김채영 110715-*******
    
    


```python
result = pattern.sub("\g<birth>-*******", text)
print(result)
```

    
        김찬영 020822-*******
        김준영 040825-*******
        김채영 110715-*******
    
    


```python
pattern = re.compile("(?P<name>\w{3}) (?P<birth>\d{6})-(?P<secret>\d{7})")
```


```python
pattern.findall(text)
```




    [('김찬영', '020822', '3069110'),
     ('김준영', '040825', '3069115'),
     ('김채영', '110715', '4063111')]




```python
print(text)
```

    
        김찬영 020822-3069110
        김준영 040825-3069115
        김채영 110715-4063111
    
    


```python
pattern = re.compile("(?P<name>\w{3}) (?P<birth>\d{6})-(?P<secret>\d{7})")
```


```python
pattern.findall(text)
```




    [('김찬영', '020822', '3069110'),
     ('김준영', '040825', '3069115'),
     ('김채영', '110715', '4063111')]




```python
result = pattern.sub("\g<name>(\g<birth>-*******)", text)
print(result)
```

    
        김찬영(020822-*******)
        김준영(040825-*******)
        김채영(110715-*******)
    
    


```python
result = pattern.sub("\g<name>(\g<birth>-*******)", text)
print(result)
```

    
        김찬영(020822-*******)
        김준영(040825-*******)
        김채영(110715-*******)
    
    


```python
result = result.split('\n')
result
```




    ['',
     '    김찬영(020822-*******)',
     '    김준영(040825-*******)',
     '    김채영(110715-*******)',
     '']




```python
result.pop(0)
result
```




    ['    김찬영(020822-*******)',
     '    김준영(040825-*******)',
     '    김채영(110715-*******)',
     '']




```python
result.pop(-1)
result
```




    ['    김찬영(020822-*******)',
     '    김준영(040825-*******)',
     '    김채영(110715-*******)']




```python
for idx, val in enumerate(result):
    val = val.replace(" ", "")
    # val[2] = "O"
    # val.pop(2)
    # val.insert(2, "O")
    print(idx, val)
```

    0 김찬영(020822-*******)
    1 김준영(040825-*******)
    2 김채영(110715-*******)
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
