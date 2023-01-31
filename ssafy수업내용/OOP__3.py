class Calculator:
    # getter setter 는 세트로 다니며, public에는 사용 할 수 없다. (method 이름과 중복되기때문)
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property  ## getter
    def b(self):
        return self._b
    
    @b.setter  ## setter
    def b(self, new_b):
        if new_b == 0:
            print("0으로는 바꿀수 없습니다.")
            return

        self._b = new_b

    def divide(self):
        return self._a / self._b

    

c = Calculator(10, 5)
c.b = 10
c.b = 0
print(c.divide())