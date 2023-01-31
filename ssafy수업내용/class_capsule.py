class Person:
    def __init__(self):
        self._age = 0

    @property  # age getter decorator
    def age(self):  ## Getter
        print('getter 호출')
        return self._age
    

    @age.setter  # age setter decorator
    def age(self, age):   ## Setter
        print('setter 호출')
        self._age = age


    # age = property(get_age, set_age)


p1 = Person()

# print(p1.get_age())

# p1.set_age(25)
# print(p1.get_age())


p1.age = 25
print(p1.age)

