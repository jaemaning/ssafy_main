# 자동차 클래스의 기능
class Car:

    cnt = 0

    # 자동차 클래스의 속성
    # 자동차 총수, 자동차의 차량번호, 자동차의 이름, 자동차의 속도
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.speed = 0
        Car.cnt += 1

    # 자동차의 속도를 파라미터만큼 증가시키는 메서드
    def accelerate(self,sp):
        self.speed += sp

    # 자동차의 속도를 파라미터만큼 감소시키는 메서드
    def slow_down(self,sp):
        self.speed -= sp

    # 차량 인스턴스를 비교 할때 차량번호가 같으면 True 아니면 False 반환
    def __eq__(self, o):
        if self.number == o.number:
            return True
        else:
            return False

    # 자동차 클래스를 print를 통해 출력할때는
    # "이름 : 자동차이름, 차량번호 : 차량번호, 속도 : 속도"
    def __str__(self):
        return f"자동차 이름 : {self.name}, 자동자 번호 : {self.number}, 속도 : {self.speed}"



avante = Car("avante",4885)
carnival = Car("Carnival",4885)

avante.accelerate(100)
avante.slow_down(50)

print(avante)
print(Car.cnt)
print(avante==carnival)