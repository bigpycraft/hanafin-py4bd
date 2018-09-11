
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## 웹 크롤링 2/2

## 웹 자료를 이용한 데이터 분석 2


```python
from bs4 import BeautifulSoup 
from urllib.request import urlopen

import pandas as pd
import re
```

#### <font color='blue'> # 웹크롤링한 데이터 읽어오기 </font>


```python
# df = pd.read_csv('data/exam-WebParsing.csv')       
df = pd.read_csv('data/chicagomag_info.csv', index_col='Rank') 
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
      <th>Unnamed: 0</th>
      <th>Cafe</th>
      <th>Menu</th>
      <th>URL</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# index_col='Unnamed: 0'') 삭제
del df['Unnamed: 0']
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
      <th>Cafe</th>
      <th>Menu</th>
      <th>URL</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 50 entries, 1 to 50
    Data columns (total 3 columns):
    Cafe    50 non-null object
    Menu    50 non-null object
    URL     50 non-null object
    dtypes: object(3)
    memory usage: 1.6+ KB
    


```python
df['Menu'][1]
```




    'BLT'




```python
df['URL'][1]
```




    'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/'




```python
from images import bigpycraft_bda as bpc
bpc.Figure(bpc.BDA_WC_12, 800)
```




![png](output/PE_DA_712/output_11_0.png)



#### <font color='blue'> # 첫번째 URL 페이지 크롤링하기 </font>


```python
html = urlopen(df['URL'][1])
soup = BeautifulSoup(html, "lxml")
soup.title
# type(soup)
```




    <title>
      1. Old Oak Tap BLT |
      Chicago magazine
          |  November 2012
        </title>




```python
soup.find('p', 'addy')
```




    <p class="addy">
    <em>$10. 2109 W. Chicago Ave., 773-772-0406, <a href="http://www.theoldoaktap.com/">theoldoaktap.com</a></em></p>




```python
taginfo = soup.find('p', 'addy').get_text()
taginfo
```




    '\n$10. 2109 W. Chicago Ave., 773-772-0406, theoldoaktap.com'




```python
taginfo = taginfo[taginfo.find('$'):]
taginfo
```




    '$10. 2109 W. Chicago Ave., 773-772-0406, theoldoaktap.com'



### <font color='brown'> Regular Expression 관련 사이트
- http://regexr.com/   : text 정보를 re로 테스트
- https://regexper.com/ : 작성된 re를 다이어그램으로 표현


```python
price = re.search('\$\d+\.(\d+)?', taginfo).group()
price
```




    '$10.'




```python
address = '일단보류'    # Street, City
```


```python
phone = re.search('\d{3}[-]\d{3}[-]\d{4}', taginfo)
if phone is not None:
    phone = phone.group()
phone
```




    '773-772-0406'




```python
infolist = taginfo.split(', ')
if infolist[-1].endswith('.com') or infolist[-1].endswith('.net'):
    homepage = infolist[-1]
else:
    homepage = 'No Homepage'
homepage
```




    'theoldoaktap.com'




```python
start = len(price)
if phone is None:
    phone = 'No Contact'
    end = taginfo.find(homepage)
else:
    end = taginfo.find(phone)
    
address = taginfo[start:end]
address
```




    ' 2109 W. Chicago Ave., '



#### <font color='blue'> # 상위 TOP3 페이지에서 가격과 주소정보만 읽어오기  </font>


```python
Price    = []
Address  = []
Phone    = []
Homepage = []

for n in [1,2,3,4,5]:   
    html = urlopen(df['URL'][n])
    soup = BeautifulSoup(html, 'lxml')
    
    taginfo = soup.find('p', 'addy').get_text()
    taginfo = taginfo[taginfo.find('$'):]
    
    price = re.search('\$\d+\.(\d+)?', taginfo).group()
    
    address = '일단보류'    # Street, City
    
    phone = re.search('\d{3}[-]\d{3}[-]\d{4}', taginfo)
    if phone is not None:
        phone = phone.group()    
        
    infolist = taginfo.split(', ')
    if infolist[-1].endswith('.com') or infolist[-1].endswith('.net'):
        homepage = infolist[-1]
    else:
        homepage = 'No Homepage'

    start = len(price)
    if phone is None:
        phone = 'No Contact'
        end = taginfo.find(homepage)
    else:
        end = taginfo.find(phone)

    address = taginfo[start:end] 

    Price.append(price)
    Address.append(address)
    Phone.append(phone)
    Homepage.append(homepage)
    
    print(n)
```

    1
    2
    3
    4
    5
    


```python
Price
```




    ['$10.', '$9.', '$9.50', '$9.40', '$10.']




```python
Address
```




    [' 2109 W. Chicago Ave., ',
     ' 800 W. Randolph St., ',
     '. 445 N. Clark St., ',
     '. 914 Noyes St., Evanston, ',
     ' 825 W. Fulton Mkt., ']




```python
Phone
```




    ['773-772-0406',
     '312-929-4580',
     '312-334-3688',
     '847-475-9400',
     '312-445-8977']




```python
Homepage
```




    ['theoldoaktap.com',
     'aucheval.tumblr.com',
     'rickbayless.com',
     'alsdeli.net',
     'publicanqualitymeats.com']




```python
price = Price[0]
if price.endswith('.'):
    price = price[:-1]
price
```




    '$10'




```python
address = Address[2]
address = address[:-2]
if address.startswith('.'):
    address = address[1:]
address = address.strip()
address
```




    '445 N. Clark St.'



#### <font color='blue'> # 가격과 주소정보를 수정보완 </font>


```python
Price    = []
Address  = []
Phone    = []
Homepage = []

for n in [1,2,3,4,5]:   
    html = urlopen(df['URL'][n])
    soup = BeautifulSoup(html, 'lxml')
    
    taginfo = soup.find('p', 'addy').get_text()
    taginfo = taginfo[taginfo.find('$'):]
    
    price = re.search('\$\d+\.(\d+)?', taginfo).group()
    # price update
    if price.endswith('.'):
        price = price[:-1]
        
    address = '일단보류'    # Street, City
    
    phone = re.search('\d{3}[-]\d{3}[-]\d{4}', taginfo)
    if phone is not None:
        phone = phone.group()    
        
    infolist = taginfo.split(', ')
    if infolist[-1].endswith('.com') or infolist[-1].endswith('.net'):
        homepage = infolist[-1]
    else:
        homepage = 'No Homepage'

    start = len(price)
    if phone is None:
        phone = 'No Contact'
        end = taginfo.find(homepage)
    else:
        end = taginfo.find(phone)

    address = taginfo[start:end] 
    # address update
    address = address[:-2]
    if address.startswith('.'):
        address = address[1:]
    address = address.strip()
    
    Price.append(price)
    Address.append(address)
    Phone.append(phone)
    Homepage.append(homepage)
    
    print(n)
```

    1
    2
    3
    4
    5
    


```python
Price
```




    ['$10', '$9', '$9.50', '$9.40', '$10']




```python
Address
```




    ['2109 W. Chicago Ave.',
     '800 W. Randolph St.',
     '445 N. Clark St.',
     '914 Noyes St., Evanston',
     '825 W. Fulton Mkt.']



#### <font color='blue'> # 만약 문제가 없다면, 전체 정보를 한번에 다 가져오기 </font>


```python
Price    = []
Address  = []
Phone    = []
Homepage = []

for n in df.index:
    html = urlopen(df['URL'][n])
    soup = BeautifulSoup(html, 'lxml')
    
    taginfo = soup.find('p', 'addy').get_text()
    taginfo = taginfo[taginfo.find('$'):]
    
    price = re.search('\$\d+\.(\d+)?', taginfo).group()
    # price update
    if price.endswith('.'):
        price = price[:-1]
        
    address = '일단보류'    # Street, City
    
    phone = re.search('\d{3}[-]\d{3}[-]\d{4}', taginfo)
    if phone is not None:
        phone = phone.group()    
        
    infolist = taginfo.split(', ')
    if infolist[-1].endswith('.com') or infolist[-1].endswith('.net'):
        homepage = infolist[-1]
    else:
        homepage = 'No Homepage'

    start = len(price)
    if phone is None:
        phone = 'No Contact'
        end = taginfo.find(homepage)
    else:
        end = taginfo.find(phone)

    address = taginfo[start:end] 
    # address update
    address = address[:-2]
    if address.startswith('.'):
        address = address[1:]
    address = address.strip()
    
    Price.append(price)
    Address.append(address)
    Phone.append(phone)
    Homepage.append(homepage)
    
    print('webpage crawling...{}'.format(n))
```

    webpage crawling...1
    webpage crawling...2
    webpage crawling...3
    webpage crawling...4
    webpage crawling...5
    webpage crawling...6
    webpage crawling...7
    webpage crawling...8
    webpage crawling...9
    webpage crawling...10
    webpage crawling...11
    webpage crawling...12
    webpage crawling...13
    webpage crawling...14
    webpage crawling...15
    webpage crawling...16
    webpage crawling...17
    webpage crawling...18
    webpage crawling...19
    webpage crawling...20
    webpage crawling...21
    webpage crawling...22
    webpage crawling...23
    webpage crawling...24
    webpage crawling...25
    webpage crawling...26
    webpage crawling...27
    webpage crawling...28
    webpage crawling...29
    webpage crawling...30
    webpage crawling...31
    webpage crawling...32
    webpage crawling...33
    webpage crawling...34
    webpage crawling...35
    webpage crawling...36
    webpage crawling...37
    webpage crawling...38
    webpage crawling...39
    webpage crawling...40
    webpage crawling...41
    webpage crawling...42
    webpage crawling...43
    webpage crawling...44
    webpage crawling...45
    webpage crawling...46
    webpage crawling...47
    webpage crawling...48
    webpage crawling...49
    webpage crawling...50
    


```python
Price
```




    ['$10',
     '$9',
     '$9.50',
     '$9.40',
     '$10',
     '$7.25',
     '$16',
     '$10',
     '$9',
     '$17',
     '$11',
     '$5.49',
     '$14',
     '$10',
     '$13',
     '$4.50',
     '$11.95',
     '$11.50',
     '$6.25',
     '$15',
     '$5',
     '$6',
     '$8',
     '$5.99',
     '$7.52',
     '$11.95',
     '$7.50',
     '$12.95',
     '$7',
     '$21',
     '$9.79',
     '$9.75',
     '$13',
     '$7.95',
     '$9',
     '$9',
     '$8',
     '$8',
     '$7',
     '$6',
     '$7.25',
     '$11',
     '$6',
     '$9',
     '$5.49',
     '$8',
     '$6.50',
     '$7.50',
     '$8.75',
     '$6.85']




```python
Address
```




    ['2109 W. Chicago Ave.',
     '800 W. Randolph St.',
     '445 N. Clark St.',
     '914 Noyes St., Evanston',
     '825 W. Fulton Mkt.',
     '100 E. Walton St.',
     '1639 S. Wabash Ave.',
     '2211 W. North Ave.',
     '3619 W. North Ave.',
     '3267 S. Halsted St.',
     '2537 N. Kedzie Blvd.',
     'Multiple locations',
     '3124 N. Broadway',
     '3455 N. Southport Ave.',
     '2657 N. Kedzie Ave.',
     '1120 W. Grand Ave.',
     '1141 S. Jefferson St.',
     '333 E. Benton Pl.',
     '1411 N. Wells St.',
     '1747 N. Damen Ave.',
     '3209 W. Irving Park Rd.',
     'Multiple locations',
     '5347 N. Clark St.',
     '2954 W. Irving Park Rd.',
     'Multiple locations',
     '191 Skokie Valley Rd., Highland Park',
     'Multiple locations',
     '1818 W. Wilson Ave.',
     '2517 W. Division St.',
     '218 W. Kinzie St.',
     'Multiple locations',
     '1547 N. Wells St.',
     '415 N. Milwaukee Ave.',
     '1840 N. Damen Ave.',
     '1220 W. Webster Ave.',
     '5357 N. Ashland Ave.',
     '1834 W. Montrose Ave.',
     '615 N. State St.',
     'Multiple locations',
     '241 N. York Rd., Elmhurst',
     '1323 E. 57th St.',
     '655 Forest Ave., Lake Forest',
     'Hotel Lincoln, 1816 N. Clark St.',
     '100 S. Marion St., Oak Park',
     '26 E. Congress Pkwy.',
     '2018 W. Chicago Ave.',
     '25 E. Delaware Pl.',
     '416 N. York St., Elmhurst',
     '65 E. Washington St.',
     '3351 N. Broadway']




```python
Phone
```




    ['773-772-0406',
     '312-929-4580',
     '312-334-3688',
     '847-475-9400',
     '312-445-8977',
     '312-649-6717',
     '312-360-9500',
     '773-276-2100',
     '773-772-8435',
     '312-929-2486',
     '773-489-9554',
     'No Contact',
     '773-661-9166',
     '773-883-2525',
     '773-276-7110',
     '312-666-0730',
     '312-939-2855',
     '773-234-3449',
     '312-944-0459',
     '773-489-1747',
     '773-539-8038',
     'No Contact',
     '773-275-5725',
     '773-539-5321',
     'No Contact',
     '847-831-0600',
     'No Contact',
     '773-293-2489',
     '773-862-8313',
     '312-624-8154',
     'No Contact',
     '312-624-9430',
     '312-829-6300',
     '773-681-9914',
     '773-883-1313',
     '773-275-4297',
     '773-334-5664',
     '312-265-0434',
     'No Contact',
     '630-516-3354',
     '773-538-7372',
     '847-234-8800',
     '312-254-4665',
     '708-725-7200',
     '312-922-2233',
     '773-384-9930',
     '312-896-2600',
     '630-359-5234',
     '312-726-2020',
     '773-868-4000']




```python
Homepage
```




    ['theoldoaktap.com',
     'aucheval.tumblr.com',
     'rickbayless.com',
     'alsdeli.net',
     'publicanqualitymeats.com',
     'No Homepage',
     'acadiachicago.com',
     'birchwoodkitchen.com',
     'cemitaspuebla.com',
     'nanaorganic.com',
     'lulacafe.com',
     'ricobenespizza.com',
     'frognsnail.com',
     'crosbyskitchenchicago.com',
     'longmanandeagle.com',
     'bariitaliansubs.com',
     'mannysdeli.com',
     'eggysdiner.com',
     'oldjerusalemchicago.com',
     'hotchocolatechicago.com',
     'No Homepage',
     'dawalikitchen.com',
     'bigjoneschicago.com',
     'lapanechicago.com',
     'pastoralartisan.com',
     'maxs-deli.com',
     'luckysandwich.com',
     'cityprovisions.com',
     'papascachesabroso.com',
     'No Homepage',
     'hannahsbretzel.com',
     'lafournette.com',
     'paramountroom.com',
     'meltsandwichshoppechicago.com',
     'floriole.com',
     'No Homepage',
     'troquetchicago.com',
     'grahamwich.com',
     'saigonsisters.com',
     'rosaliasdeli.com',
     'zhmarketcafe.com',
     'themarkethouse.com',
     'No Homepage',
     'marionstreetcheesemarket.com',
     'cafecitochicago.com',
     'chickpeaonthego.com',
     'goddessandgrocer.com',
     'eatmyzenwich.com',
     'tonipatisserie.com',
     'phoebesbakery.com']




```python
len(df), len(Price), len(Address), len(Phone), len(Homepage)
```




    (50, 50, 50, 50, 50)



#### <font color='blue'> # 기존 데이터에 칼럼(가격, 주소) 추가하기 </font>


```python
df['Price'] = Price
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
      <th>Cafe</th>
      <th>Menu</th>
      <th>URL</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Address'] = Address
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
      <th>Cafe</th>
      <th>Menu</th>
      <th>URL</th>
      <th>Price</th>
      <th>Address</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
      <td>2109 W. Chicago Ave.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9</td>
      <td>800 W. Randolph St.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.50</td>
      <td>445 N. Clark St.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.40</td>
      <td>914 Noyes St., Evanston</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
      <td>825 W. Fulton Mkt.</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Phone'] = Phone
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
      <th>Cafe</th>
      <th>Menu</th>
      <th>URL</th>
      <th>Price</th>
      <th>Address</th>
      <th>Phone</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
      <td>2109 W. Chicago Ave.</td>
      <td>773-772-0406</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9</td>
      <td>800 W. Randolph St.</td>
      <td>312-929-4580</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.50</td>
      <td>445 N. Clark St.</td>
      <td>312-334-3688</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.40</td>
      <td>914 Noyes St., Evanston</td>
      <td>847-475-9400</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
      <td>825 W. Fulton Mkt.</td>
      <td>312-445-8977</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Homepage'] = Homepage
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
      <th>Cafe</th>
      <th>Menu</th>
      <th>URL</th>
      <th>Price</th>
      <th>Address</th>
      <th>Phone</th>
      <th>Homepage</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
      <td>2109 W. Chicago Ave.</td>
      <td>773-772-0406</td>
      <td>theoldoaktap.com</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9</td>
      <td>800 W. Randolph St.</td>
      <td>312-929-4580</td>
      <td>aucheval.tumblr.com</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.50</td>
      <td>445 N. Clark St.</td>
      <td>312-334-3688</td>
      <td>rickbayless.com</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.40</td>
      <td>914 Noyes St., Evanston</td>
      <td>847-475-9400</td>
      <td>alsdeli.net</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
      <td>825 W. Fulton Mkt.</td>
      <td>312-445-8977</td>
      <td>publicanqualitymeats.com</td>
    </tr>
  </tbody>
</table>
</div>




```python
cols = list(df)
cols
```




    ['Cafe', 'Menu', 'URL', 'Price', 'Address', 'Phone', 'Homepage']




```python
cols.index('URL')
```




    2




```python
cols[6]
```




    'Homepage'




```python
# cols.insert(6, cols.pop(cols.index('URL')))
cols.append(cols.pop(cols.index('URL')))
cols
```




    ['Cafe', 'Menu', 'Price', 'Address', 'Phone', 'Homepage', 'URL']




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
      <th>Cafe</th>
      <th>Menu</th>
      <th>URL</th>
      <th>Price</th>
      <th>Address</th>
      <th>Phone</th>
      <th>Homepage</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
      <td>2109 W. Chicago Ave.</td>
      <td>773-772-0406</td>
      <td>theoldoaktap.com</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9</td>
      <td>800 W. Randolph St.</td>
      <td>312-929-4580</td>
      <td>aucheval.tumblr.com</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.50</td>
      <td>445 N. Clark St.</td>
      <td>312-334-3688</td>
      <td>rickbayless.com</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$9.40</td>
      <td>914 Noyes St., Evanston</td>
      <td>847-475-9400</td>
      <td>alsdeli.net</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
      <td>$10</td>
      <td>825 W. Fulton Mkt.</td>
      <td>312-445-8977</td>
      <td>publicanqualitymeats.com</td>
    </tr>
  </tbody>
</table>
</div>



#### <font color='blue'> # ix 를 사용하면 컬럼과 레코드전체가 옮겨진다. </font>


```python
df = df.ix[:, cols]
df.head()
```

    C:\Python\Anaconda3-50\lib\site-packages\ipykernel_launcher.py:1: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
      """Entry point for launching an IPython kernel.
    




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
      <th>Cafe</th>
      <th>Menu</th>
      <th>Price</th>
      <th>Address</th>
      <th>Phone</th>
      <th>Homepage</th>
      <th>URL</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>$10</td>
      <td>2109 W. Chicago Ave.</td>
      <td>773-772-0406</td>
      <td>theoldoaktap.com</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>$9</td>
      <td>800 W. Randolph St.</td>
      <td>312-929-4580</td>
      <td>aucheval.tumblr.com</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>$9.50</td>
      <td>445 N. Clark St.</td>
      <td>312-334-3688</td>
      <td>rickbayless.com</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>$9.40</td>
      <td>914 Noyes St., Evanston</td>
      <td>847-475-9400</td>
      <td>alsdeli.net</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>$10</td>
      <td>825 W. Fulton Mkt.</td>
      <td>312-445-8977</td>
      <td>publicanqualitymeats.com</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df.loc[:, cols]
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
      <th>Cafe</th>
      <th>Menu</th>
      <th>Price</th>
      <th>Address</th>
      <th>Phone</th>
      <th>Homepage</th>
      <th>URL</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Old Oak Tap</td>
      <td>BLT</td>
      <td>$10</td>
      <td>2109 W. Chicago Ave.</td>
      <td>773-772-0406</td>
      <td>theoldoaktap.com</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Au Cheval</td>
      <td>Fried Bologna</td>
      <td>$9</td>
      <td>800 W. Randolph St.</td>
      <td>312-929-4580</td>
      <td>aucheval.tumblr.com</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Xoco</td>
      <td>Woodland Mushroom</td>
      <td>$9.50</td>
      <td>445 N. Clark St.</td>
      <td>312-334-3688</td>
      <td>rickbayless.com</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Al’s Deli</td>
      <td>Roast Beef</td>
      <td>$9.40</td>
      <td>914 Noyes St., Evanston</td>
      <td>847-475-9400</td>
      <td>alsdeli.net</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Publican Quality Meats</td>
      <td>PB&amp;L</td>
      <td>$10</td>
      <td>825 W. Fulton Mkt.</td>
      <td>312-445-8977</td>
      <td>publicanqualitymeats.com</td>
      <td>http://www.chicagomag.com/Chicago-Magazine/Nov...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 50 entries, 1 to 50
    Data columns (total 7 columns):
    Cafe        50 non-null object
    Menu        50 non-null object
    Price       50 non-null object
    Address     50 non-null object
    Phone       50 non-null object
    Homepage    50 non-null object
    URL         50 non-null object
    dtypes: object(7)
    memory usage: 5.6+ KB
    

#### <font color='blue'> # 추가로 변경작업한 데이터 파일로 저장하기 </font>


```python
df.to_csv('data/chicagomag_info2.csv', sep=',', encoding='UTF-8')
```


```python
# % ls data
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
