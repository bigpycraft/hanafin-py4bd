# Arbitrary Arguments, 가변 인자 리스트 활용
def introduceMyFamily(my_name, *family_names, **family_info):
    print('안녕하세요, 저는 %s 입니다.'%(my_name))
    print('-'*35)
    print('제 가족들의 이름은 아래와 같아요. ')
    for name in family_names:
        print('* %s ' % (name), end='\t')
    else:
        print()
    print('-' * 35)
    for key in family_info.keys():
        print('- %s : %s ' %(key, family_info[key]))

introduceMyFamily('진수', '희영', '찬영', '준영', '채영',
                  주소='롯데캐슬', 가훈='극기상진', 소망='세계일주')

