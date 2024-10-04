class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frr'
    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance += dy
        

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
    def get_pos(self):
        position = (self.x_distance, self.y_distance)
        return position
    def voice(self):
        print(self.sound)


#-----------------------------------------
h1 = Horse()
h1.run(5)
print(f'конь пробежал {h1.x_distance}')
#-----------------------------------------
p1 = Pegasus()
p1.move(1,2)
print(f'пегас пробежал {p1.x_distance} и пролетел {p1.y_distance}')
#-----------------------------------------

print(Pegasus.mro()) # наследование класса
print('-' * 50,'\n')

# ========================================= Test Case ============================================

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
