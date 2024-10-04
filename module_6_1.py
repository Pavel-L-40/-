#=======================Animal========================
class Animal:
    alive = True  # живой
    fed = False  # сытый
    def __init__(self, name_animal):
        self.name = name_animal

    def eat(self, food):
        if food.edible:
            print(f'{self.name} ест {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


#--------------''' наследники Animal'''-------------
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
#===================================================


#=======================Plant=======================
class Plant:
    edible = False # съедобность
    def __init__(self, name_plant):
        self.name = name_plant

#--------------''' наследники Plant'''-------------
class Flower(Plant):
    pass # параметры наследования не изменяются


class Fruit(Plant):
    def __init__(self, name_plant, edible = True):
        super().__init__(name_plant)
        self.edible = edible

# ---End code---


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

# a3 = Predator('King_Kong', fed = True)
# print(a3.fed)
