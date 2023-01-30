class Person:
    
    ## class가 실행될 때 자동으로 실행되는 함수(메서드) - 생성자 메서드
    def __init__(self, name, age):
        # 인스턴스 변수 초기값 설정
        self.name = name
        self.age = age

    ## class로 생성된 인스턴스가 string 형태로 호출될때 리턴되는 함수(메서드)
    def __str__(self):
        # 객체를 문자열로 어떻게 표현할지
        return f"제 이름은 {self.name} 입니다"

    # parameter 1개(o) 필요, 비교 대상 객체
    def __eq__(self, o):
        if self.age == o.age:
            return True
        else:
            return False

    
Person.gender = "남"
me = Person("kim",30)
isaac = Person("isaac",19)
me.gender = "여"

이병헌 = Person("이병헌",30)
이병헌2 = Person('이병헌2',30)

print(me.name,me.age)
print(me)
print(isaac.gender, me.gender)

print(이병헌 == 이병헌2, 이병헌 is 이병헌2)