# 부모클래스, Animal
class Animal:
    tribe = '동물'
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print('나는', self.tribe,  self.name, '입니다.')

# Animal의 자식클래스, Carnivore 클래스
class Carnivore(Animal):
    def __init__(self, name):
        self.name = name
        self.tribe = '육식동물'

    def favoriteFood(self):
        print('나는 고기를 좋아합니다.')

# Animal의 자식클래스, Herbivore 클래스
class Herbivore(Animal):
    def __init__(self, name):
        self.name = name
        self.tribe = '초식동물'

    def favoriteFood(self):
        print('나는 풀을 좋아합니다.')

print('-' * 50, "\n[Carnivore 객체 생성]")
tiger = Carnivore('호랑이')
tiger.getInfo()
tiger.favoriteFood()

print('-' * 50, "\n[Herbivore 객체 생성]")
rabit = Herbivore('토끼')
rabit.getInfo()
rabit.favoriteFood()
