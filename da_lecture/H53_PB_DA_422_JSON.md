
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## JSON (JavaScript Object Notation)
> 자바스크립트 객체 표기법
- JSON (JavaScript Object Notation)은 경량의 DATA-교환 형식이다. <br><br>
- XML은 태그속에 데이타가 들어 있으므로 데이타를 사용하는게 조금 번거롭다.
<br> JSON은 객체이므로 바로 꺼집어내어 사용이 가능하며, 또한 무겁지도 않다. <br><br>
- JSON은 두개의 구조를 기본으로 두고 있다.
<div>
1) name/value 형태의 쌍으로 collection 타입. <br> &nbsp; - 
다양한 언어들에서, 이는 object, record, struct(구조체), dictionary, hash table, 키가 있는 list, 또는 연상배열로서 실현 되었다. <br>
2) 값들의 순서화된 리스트. <br> &nbsp; - 
대부분의 언어들에서, 이는 array, vector, list, 또는 sequence로서 실현 되었다.
</div><br>
- 참조사이트 : http://www.json.org/ 

### <font color='blue'>JSON 파일 읽어오기</font>


```python
import json
```


```python
json_data = {
    'firstname' : '길동',
    'lastname'  : '홍',
    'age'       : 20, 
    'country'   : '율도국'
}
```


```python
json_code = json.JSONEncoder().encode(json_data)
print(json_code)
```

    {"firstname": "\uae38\ub3d9", "lastname": "\ud64d", "age": 20, "country": "\uc728\ub3c4\uad6d"}
    


```python
check = json.dumps('한글')
print(check)
```

    "\ud55c\uae00"
    


```python
check = json.dumps('한글', ensure_ascii=False)
print(check)
```

    "한글"
    


```python
check = json.dumps(json_data, ensure_ascii=False)
print(check)
```

    {"firstname": "길동", "lastname": "홍", "age": 20, "country": "율도국"}
    


```python
json_code = json.JSONDecoder().decode(check)
json_code
```




    {'age': 20, 'country': '율도국', 'firstname': '길동', 'lastname': '홍'}




```python
json_code['country']
```




    '율도국'




```python
"{}{}은 {}살 이고, {}에 살고 있습니다.".format(
    json_code['lastname'],
    json_code['firstname'],
    json_code['age'],
    json_code['country'],
)
```




    '홍길동은 20살 이고, 율도국에 살고 있습니다.'



### <font color='blue'>Person 객체</font>


```python
class Person:
    name = str()
    age  = int()
    hometown = str()
    
    def __init__(self, name, age, hometown):
        self.name = name
        self.age  = age
        self.hometown = hometown
    
    def to_string(self):
        # str = '나의 살던 고향은 ' + self.hometown + '입니다.'
        str = '%s의 나이는 %d살이고, 고향은 %s입니다.' % (self.name, self.age, self.hometown)
        return str
```


```python
theif1 = Person("홍길동", 20, "율도국");
theif2 = Person("임꺽정", 35, "구월산");
```


```python
theif1.to_string()
```




    '홍길동의 나이는 20살이고, 고향은 율도국입니다.'




```python
theif2.to_string()
```




    '임꺽정의 나이는 35살이고, 고향은 구월산입니다.'




```python
# % ls data
```

### <font color='blue'>JSON 코드 작성하기</font>

### JSON 코드1
<hr>
```python
# girlgroup.json
──────────────────────────────────────────────────
    [ "소녀시대", "앱터스쿨", "에이핑크", "걸스데이", "우주소녀" ]
```

> <font size=2 color='#CC0000'> 출력 :
내가 좋아하는 걸그룹은 에이핑크와 우주소녀입니다.
</font>


```python
with open('data/girlgroup.json', 'w') as fp:
    data = '[ "소녀시대", "앱터스쿨", "에이핑크", "걸스데이", "우주소녀" ]'
    fp.write(data)
```


```python
with open('data/girlgroup.json') as data_file:    
    girlgroup = json.load(data_file)
```


```python
girlgroup
```




    ['소녀시대', '앱터스쿨', '에이핑크', '걸스데이', '우주소녀']




```python
"내가 좋아하는 걸그룹은 {}와 {}입니다.".format(
    girlgroup[2], girlgroup[4]
) 
```




    '내가 좋아하는 걸그룹은 에이핑크와 우주소녀입니다.'



### JSON 코드2
<hr>
```python
# member.json
──────────────────────────────────────────────────
    {
        "name" : "홍길동",
        "age"  : 20,
        "addr" : {
            "city"  : "서울시",
            "dong"  : "염창동"
        }
    }
```

> <font size=2 color='#CC0000'> 출력 :
홍길동은 20살 이고, 서울시 염창동에 살고 있습니다.
</font>


```python
data = '''
    {
        "name" : "홍길동",
        "age"  : 20,
        "addr" : {
            "city"  : "서울시",
            "dong"  : "염창동"
        }
    }
'''
with open('data/member.json', 'w') as fp:
    fp.write(data)
```


```python
with open('data/member.json') as data_file:    
    member = json.load(data_file)

print(member)
```

    {'name': '홍길동', 'age': 20, 'addr': {'city': '서울시', 'dong': '염창동'}}
    


```python
"{}은 {}살 이고, {} {}에 살고 있습니다.".format(
    member["name"],
    member["age"],
    member["addr"]["city"], 
    member["addr"]["dong"], 
)
```




    '홍길동은 20살 이고, 서울시 염창동에 살고 있습니다.'



### JSON 코드3
<hr>
```python
# person.json
──────────────────────────────────────────────────
    {
        "name" : "홍길동",
        "dog"  : {
            "name" : "순둥이",
            "toys" : [
                    { "name" : "뽀로로" },
                    { "name" : "토마스" }
            ]
        }
    }
```

> <font size=2 color='#CC0000'> 출력 :
홍길동의 개 순둥이의 장난감은 뽀로로, 토마스입니다.
</font>


```python
data = '''
    {
        "name" : "홍길동",
        "dog"  : {
            "name" : "순둥이",
            "toys" : [
                    { "name" : "뽀로로" },
                    { "name" : "토마스" }
            ]
        }
    }
'''
```


```python
with open('data/person.json', 'w') as fp:
    fp.write(data)
```


```python
with open('data/person.json') as data_file:    
    person = json.load(data_file)
    
print(person)
```

    {'name': '홍길동', 'dog': {'name': '순둥이', 'toys': [{'name': '뽀로로'}, {'name': '토마스'}]}}
    

#### 아래와 같이 출력하는 JSON 코드로 작성하세요.
> <font size=2 color='#CC0000'> 출력 :
홍길동의 개 순둥이의 장난감은 뽀로로, 토마스입니다.
</font>

### <font size=2 color='blue'>JSON코드로 완성하기 </font>
"{}의 개 {}의 장난감은 {}, {}입니다.".format(
<!--
    person["name"], 
    person["dog"]["name"],
    person["dog"]["toys"][0]["name"],
    person["dog"]["toys"][1]["name"]
//-->
)



```python
"{}의 개 {}의 장난감은 {}, {}입니다.".format(

    
    
    
)

```




    '홍길동의 개 순둥이의 장난감은 뽀로로, 토마스입니다.'



<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
