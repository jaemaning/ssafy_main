class Car:

    def __init__(self, name, num):
        self.name = name
        self.num = num

    def horn(self):
        print("빵빵")
        print(self.name,self.num)


class Avante(Car):

    def __init__(self, name, num, ava):
        super().__init__(name, num)
        self.ava = ava
    
    def horn(self):  ## 오버라이딩
        print(self.name, self.num, self.ava)
    

class Sonate(Car):
    pass

class Carnival(Car):
    pass

ava = Avante('avante', 4885, 'ava')
ava.horn()

s = Sonate('sonata', 1234)
s.horn()

print(Avante.mro())