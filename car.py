class Car:

    def __init__(self,name,number,speed):
        self.name = name
        self.number = number
        self.speed = speed

    def accelerate(self,sp):
        self.speed += sp


    def slow_down(self,sp):
        self.speed -= sp


    def __eq__(self, o):
        if self.number == o.number:
            return True
        else:
            return False

    def __str__(self):
        return f"자동차 이름 : {self.name}, 자동자 번호 : {self.number}, 속도 : {self.speed}"


# 자동차 클래스의 속성
# 자동차 총수, 자동차의 차량번호, 자동차의 이름, 자동차의 속도
# 자동차 클래스의 기능
# 자동차의 속도를 파라미터만큼 증가시키는 메서드
# 자동차의 속도를 파라미터만큼 감소시키는 메서드
# 자동차 클래스를 print를 통해 출력할때는
# "이름 : 자동차이름, 차량번호 : 차량번호, 속도 : 속도"


avante = Car("avante",4885,0)

avante.accelerate(100)
avante.slow_down(50)

print(avante)