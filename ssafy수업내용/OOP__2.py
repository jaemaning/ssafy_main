class Person:

    def __init__(self, name, age, money, num):
        # public
        self.name = name
        self.age = age
        # protected
        self._money = money
        # private
        self.__num = num

    def get_money(self):
        return self._money

    def get_num(self, password):

        if password == "1234":
            return self.__num
        else:
            return "비밀번호가 틀렸습니다."
    
p1 = Person('홍길동', 30, '1억',940320)

print(p1.age)
# print(p1._money) ## 파이썬 내부에선 가능하지만 실제로 접근하려면 접근 x
print(p1.get_money())
# print(p1.__num) # 에러
print(p1.get_num("1244"))
print(p1.get_num('1234'))

# 밖에서 private 접근
print(p1._Person__num) 
