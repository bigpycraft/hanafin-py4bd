# 객체지향의 꽃, 상속 Inheritance

# 부모클래스, Human
class Human:
    country = 'Korea'

    def __init__(self, name):
        self.name = name

    def eat_meal(self):
        print(self.name + ' is eating meal!!')


# Human의 자식클래스인 BookReader 클래스
class BookReader(Human):
    def read_book(self):
        print(self.name + ' is reading Book!!')


# Human의 자식클래스인 DrumPlayer 클래스
class DrumPlayer(Human):
    def play_drum(self):
        print(self.name + ' is playing Drum!!')


br = BookReader('Chanyoung')
br.eat_meal()

dp = DrumPlayer('Juneyoung')
dp.eat_meal()

print()
print('br.__class__ :', br.__class__)                    # br 인스턴스의 타입 확인
print('BookReader.__class__ :', BookReader.__class__)    # BookReader 클래스의 타입 확인
print('BookReader.__bases__ :', BookReader.__bases__)    # BookeReader 클래스의 부모클래스 확인
print('Human.__class__ :', Human.__class__)              # Human 클래스의 타입 확인
print('Human.__bases__ :', Human.__bases__)              # Human 클래스의 부모클래스 확인



