#=======================Animal=======================
class Animal:


    def __init__(self, name_animal, alive = True, fed = False):
        self.name = name_animal
        self.alive = alive      # живой
        self.fed = fed          # сытый

#--------------''' наследники Animal'''
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} ест {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False



#=======================Plant=======================
class Plant:
     # съедобность
    def __init__(self, name_plant,edible = False):
        self.name = name_plant
        self.edible = edible
#--------------''' наследники Plant'''
class Flower(Plant):
    pass # параметры наследования не изменяются


class Fruit(Plant):
    def __init__(self, name, edible = True ):
        self.name = name
        self.edible = True

# flower1 = Flower('Хризантема')
# fruit1 = Fruit('apple')
# print(flower1.edible)
# print(fruit1.edible)
# print(fruit1.name)

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)