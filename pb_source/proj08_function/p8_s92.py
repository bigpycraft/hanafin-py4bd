
# 서재의 책
book1 = {'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False }
book2 = {'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True  }
book3 = {'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True  }
book4 = {'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False }
book5 = {'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True  }


#global books
books = list()      # 책 목록 선언

def readBook(dict_book):
    books.append(dict_book)
    #return books


def getThickBook(books_list, pages=100):
    books_title = list()
    for book in books_list:
        if book['쪽수'] > pages:
            books_title.append(book['제목'])
    return  books_title


def getRecommendBook(books_list):
    books_title = list()
    for book in books_list:
        if book['추천유무']:
            books_title.append(book['제목'])
    return  books_title


def getPublishCompany(books_list):
    company = set()
    for book in books_list:
        company.add(book['출판사'])
    return  company

def getAllPages(books_list):
    pages = 0
    for book in books_list:
        pages += book['쪽수']
    return pages

print('책 목록 : ', books)

readBook(book1)
readBook(book2)
readBook(book3)
readBook(book4)
readBook(book5)

for book in books :
    print(book)

print('\n* 두꺼운책 목록 리스트')
result_books = getThickBook(books, 250)
for book in result_books :
    print(book)

print('\n* 출판사 리스트')
pub_companies = getPublishCompany(books)
for company in pub_companies :
    print(company)



pages = getAllPages(books)
print('\n* 읽은책의 총 페이지수 :', pages)
