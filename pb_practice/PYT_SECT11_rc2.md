
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>데이터베이스, DB SQL</font>
>  
- 데이터베이스 및 테이블 생성
- 데이터 생성, INSERT
- 데이터 조회, SELECT
- 데이터 갱신, UPDATE
- 데이터 삭제, DELETE


```python
import sqlite3  

db_name = './database/my_books.db'
```

### 테이블 생성


```python
def create_table(db_name, db_sql):
    """
    데이터베이스 테이블을 생성하는 함수
    Args:
        db_name : Database Name
        db_sql  : Query for creating Table
    Returns : None
    """
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name)  

    # 커서 확보
    cur = conn.cursor()  

    # 테이블 생성
    cur.execute(db_sql)

    # 데이터베이스 반영
    conn.commit()       

    # 데이터베이스 커넥션 닫기
    conn.close()        

# if __name__ == "__main__":  # 외부에서 호출 시
#     create_table()          # 테이블 생성 함수 호출

```


```python
create_table(db_name, db_sql=None)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-3-c107ca95d8a3> in <module>()
    ----> 1 create_table(db_name, db_sql=None)
    

    <ipython-input-2-c4f899a9c114> in create_table(db_name, db_sql)
         14 
         15     # 테이블 생성
    ---> 16     cur.execute(db_sql)
         17 
         18     # 데이터베이스 반영
    

    ValueError: operation parameter must be str



```python
db_sql  = '''
CREATE TABLE my_books (
    title text,
    published_date text,
    publisher text,
    pages integer,
    recommendation integer
)
'''

create_table(db_name, db_sql)
```
> pip install sqlite
> pip install dataset

> sqlite3 ./database/my_books.db

sqlite> .help
sqlite> .databases
sqlite> .tables
sqlite> .schema my_books
CREATE TABLE my_books (
    title text,
    published_date text,
    publisher text,
    pages integer,
    recommendation integer
);
sqlite> .quit

### 데이터 등록


```python
import sqlite3  

# 데이터 입력 함수
def insert_books(db_name):
    """
    데이터베이스 테이블에 데이터를 등록하는 함수
    Args:
        db_name : Database Name
    Returns : None 
    """
    
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name) 
    
    # 커서 확보
    cur = conn.cursor()  

    # 데이터 입력 SQL1
    db_sql = "INSERT INTO my_books VALUES ('메가트랜드', '2002.03.02','A', 200, 0)"
    cur.execute(db_sql)

    # 데이터 입력 SQL2
    db_sql = 'INSERT INTO my_books VALUES (?, ?, ?, ?, ?)'
    cur.execute(db_sql, ('인더스트리 4.0', '2016.07.09','B', 584, 1))

    # # 데이터 입력 SQL3
    books = [
        ('유니콘 스타트업', '2011.07.15','A', 248, 1),
        ('빅데이터 마케팅', '2012.08.25','A', 296, 1),
        ('사물인터넷 전망', '2013.08.22','B', 526, 0)
    ]
    cur.executemany(db_sql, books)

    # 데이터베이스 반영
    conn.commit()       

    # 커넥션 닫기
    conn.close()        

# if __name__ == "__main__":          # 외부에서 호출 시
#     insert_books()                  # 데이터 입력 함수 호출

```


```python
insert_books(db_name)
```

### 데이터 조회


```python
import sqlite3

def select_all_books(db_name):
    """
    전체 데이터를 조회하는 함수
    Args:
        db_name : Database Name
    Returns : None 
    """
    
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name) 
    
    # 커서 확보
    cur = conn.cursor()  

    # 조회용 SQL 실행
    db_sql = "SELECT * FROM my_books"
    cur.execute(db_sql) 

    # 조회한 데이터 불러오기
    print('[1] 전체 데이터 출력하기')
    books = cur.fetchall()                          

    # 데이터 출력하기
    for book in books:                              
        print(book)

    # 커넥션 닫기
    conn.close()                                    

# if __name__ == "__main__":       # 외부에서 호출 시
#     select_all_books()           # 전체 조회용 함수 호출
#     print('=============================================')

```


```python
select_all_books(db_name)
```

    [1] 전체 데이터 출력하기
    ('메가트랜드', '2002.03.02', 'A', 200, 0)
    ('인더스트리 4.0', '2016.07.09', 'B', 584, 1)
    ('유니콘 스타트업', '2011.07.15', 'A', 248, 1)
    ('빅데이터 마케팅', '2012.08.25', 'A', 296, 1)
    ('사물인터넷 전망', '2013.08.22', 'B', 526, 0)
    


```python
# 일부 조회용 함수
def select_some_books(db_name, number):
    """
    일부 데이터를 조회하는 함수
    Args:
        db_name : Database Name
        number  : Count of data to query
    Returns : None 
    """
    
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name) 
    
    # 커서 확보
    cur = conn.cursor()  
    
    # 조회용 SQL 실행
    db_sql = "SELECT * FROM my_books"
    cur.execute(db_sql) 

    # 조회한 데이터 일부 불러오기
    print('[2] 데이터 일부 출력하기')
    books = cur.fetchmany(number)                   

    # 데이터 출력하기
    for book in books:
        print(book)

    # 커넥션 닫기
    conn.close()                                    

# if __name__ == "__main__":         # 외부에서 호출 시
#     select_some_books(3)           # 일부 조회용 함수 호출
#     print('=============================================')

```


```python
select_some_books(db_name, number=3)
```

    [2] 데이터 일부 출력하기
    ('메가트랜드', '2002.03.02', 'A', 200, 0)
    ('인더스트리 4.0', '2016.07.09', 'B', 584, 1)
    ('유니콘 스타트업', '2011.07.15', 'A', 248, 1)
    


```python
# 1개 조회용 함수
def select_one_book(db_name):
    """
    최상단 하나의 데이터를 조회하는 함수
    Args:
        db_name : Database Name
    Returns : None 
    """
    
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name) 
    
    # 커서 확보
    cur = conn.cursor()  
    
    # 조회용 SQL 실행
    db_sql = "SELECT * FROM my_books"
    cur.execute(db_sql) 
    
    # 데이터 한개 출력하기
    print('[3] 1개 데이터 출력하기')
    print(cur.fetchone())                          

    # 커넥션 닫기
    conn.close()                                   

# if __name__ == "__main__":        # 외부에서 호출 시
#     select_one_book()             # 1개 조회용 함수 호출
#     print('=============================================')


```


```python
select_one_book(db_name) 
```

    [3] 1개 데이터 출력하기
    ('메가트랜드', '2002.03.02', 'A', 200, 0)
    


```python
# 쪽수 많은 책 조회용 함수
def find_big_books(db_name):
    """
    조건에 맞는 데이터를 조회하는 함수
    조건 : 페이지수가 300쪽보다 큰 데이터
    Args:
        db_name : Database Name
    Returns : None 
    """
    
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name) 
    
    # 커서 확보
    cur = conn.cursor()  
    
    # 조회용 SQL 실행
    db_sql = "SELECT title, pages FROM my_books "
    db_sql+= "WHERE pages > 300"
    cur.execute(db_sql) 

    # 조회한 데이터 불러오기
    print('[4] 페이지 많은 책 출력하기')
    books = cur.fetchall()                          

    # 데이터 출력하기
    for book in books:                              
        print(book)

    # 커넥션 닫기
    conn.close()                                    

# if __name__ == "__main__":          # 외부에서 호출 시
#     find_big_books()                # 쪽수 많은 책 조회용 함수 호출
#     print('=============================================')
```


```python
find_big_books(db_name)
```

    [4] 페이지 많은 책 출력하기
    ('인더스트리 4.0', 584)
    ('사물인터넷 전망', 526)
    

### 데이터 갱신


```python
import sqlite3 

def update_books(db_name):
    """
    데이터를 수정하는 함수
    Args:
        db_name : Database Name
    Returns : None 
    """
    
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name) 
    
    # 커서 확보
    cur = conn.cursor()  

    # 데이터 수정 SQL ( 제목이 ? 인 책의 추천 유무를 ? 로 변경하라 )
    db_sql = "UPDATE my_books SET recommendation=? WHERE title=? "
    
    # 수정 SQL 실행
    cur.execute(db_sql, (1, '메가트랜드'))

    # 데이터베이스 반영
    conn.commit()
    
    # 커넥션 닫기
    conn.close()

# if __name__ == "__main__":        # 외부에서 호출 시
#     select_one_book()
#     update_books()                # 데이터 수정 함수 호출
#     print('[데이터 수정 완료] ================== ')
#     select_one_book()

```


```python
select_one_book(db_name)
update_books(db_name)
print('[데이터 수정 완료] ================== ')
select_one_book(db_name)
```

    [3] 1개 데이터 출력하기
    ('메가트랜드', '2002.03.02', 'A', 200, 0)
    [데이터 수정 완료] ================== 
    [3] 1개 데이터 출력하기
    ('메가트랜드', '2002.03.02', 'A', 200, 1)
    

### 데이터 삭제


```python
import sqlite3 

# 데이터 삭제용 함수
def delete_books_by_title(db_name, title):
    """
    책제목에 해당하는 데이터를 삭제하는 함수
    Args:
        db_name : Database Name
        title   : Title of the book to be removed
    Returns : None 
    """
    
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name) 
    
    # 커서 확보
    cur = conn.cursor()  

    # 데이터 삭제 SQL
    db_sql = "DELETE FROM my_books "
    db_sql+= "WHERE title = ?      "

    # 수정 SQL 실행
    print('db_sql:', db_sql)
    print('title:', title)
    cur.execute(db_sql, (title,))

    # 데이터베이스 반영
    conn.commit() 
    
    # 커넥션 닫기
    conn.close() 

 
```


```python
select_all_books(db_name)  
title = '메가트랜드'
delete_books_by_title(db_name, title)   
print('[데이터 삭제 완료] ================== ')
select_all_books(db_name) 
```

    [1] 전체 데이터 출력하기
    ('메가트랜드', '2002.03.02', 'A', 200, 1)
    ('인더스트리 4.0', '2016.07.09', 'B', 584, 1)
    ('유니콘 스타트업', '2011.07.15', 'A', 248, 1)
    ('빅데이터 마케팅', '2012.08.25', 'A', 296, 1)
    ('사물인터넷 전망', '2013.08.22', 'B', 526, 0)
    db_sql: DELETE FROM my_books WHERE title = ?      
    title: 메가트랜드
    [데이터 삭제 완료] ================== 
    [1] 전체 데이터 출력하기
    ('인더스트리 4.0', '2016.07.09', 'B', 584, 1)
    ('유니콘 스타트업', '2011.07.15', 'A', 248, 1)
    ('빅데이터 마케팅', '2012.08.25', 'A', 296, 1)
    ('사물인터넷 전망', '2013.08.22', 'B', 526, 0)
    


```python
def delete_books(db_name, col_name, col_val):
    """
    조건에 맞는 데이터를 삭제하는 함수
    Args:
        db_name  : Database Name
        col_name : Column Name
        col_val  : Column Value
    Returns : None 
    """
    
    # 데이터베이스 커넥션 생성
    conn = sqlite3.connect(db_name) 
    
    # 커서 확보
    cur = conn.cursor()  


    # 데이터 삭제 SQL
    # db_sql = "DELETE FROM my_books "
    # db_sql+= "WHERE {} = '{}' "
    # db_sql = db_sql.format(col_name, col_val)
    # cur.execute(db_sql)    
    
    # # 데이터 삭제 SQL
    db_sql = 'DELETE FROM my_books '
    db_sql+= 'WHERE {} = ? '
    db_sql = db_sql.format(col_name)

    # 수정 SQL 실행
    cur.execute(db_sql, (col_val,))
    
    # 데이터베이스 반영
    conn.commit() 
    
    # 커넥션 닫기
    conn.close() 
    
    
# if __name__ == "__main__":     # 외부에서 호출 시
#     select_all_books()         # 테이블 전체 데이터 확인
#     delete_books()             # 데이터 삭제 함수 호출
#     print('[데이터 삭제 완료] ================== ')
#     select_all_books()         # 테이블 전체 데이터 확인

```


```python
select_all_books(db_name)  
col_name = 'publisher'
col_val  = 'A'
delete_books(db_name, col_name, col_val)
print('[데이터 삭제 완료] ================== ')
select_all_books(db_name) 
```

    [1] 전체 데이터 출력하기
    ('인더스트리 4.0', '2016.07.09', 'B', 584, 1)
    ('유니콘 스타트업', '2011.07.15', 'A', 248, 1)
    ('빅데이터 마케팅', '2012.08.25', 'A', 296, 1)
    ('사물인터넷 전망', '2013.08.22', 'B', 526, 0)
    [데이터 삭제 완료] ================== 
    [1] 전체 데이터 출력하기
    ('인더스트리 4.0', '2016.07.09', 'B', 584, 1)
    ('사물인터넷 전망', '2013.08.22', 'B', 526, 0)
    


```python
select_all_books(db_name)  
col_name = 'title'
col_val  = '사물인터넷 전망'
delete_books(db_name, col_name, col_val)
print('[데이터 삭제 완료] ================== ')
select_all_books(db_name) 
```

    [1] 전체 데이터 출력하기
    ('인더스트리 4.0', '2016.07.09', 'B', 584, 1)
    ('사물인터넷 전망', '2013.08.22', 'B', 526, 0)
    [데이터 삭제 완료] ================== 
    [1] 전체 데이터 출력하기
    ('인더스트리 4.0', '2016.07.09', 'B', 584, 1)
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
