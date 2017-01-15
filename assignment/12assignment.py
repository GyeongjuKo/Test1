## 사람 클래스 - 이름, 나이, 성별
## 직장 동료 클래스(사람 클래스 이용) - 추가 직급
## 클래스, 상속 활용

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Coworker(Person):
    position = "assistant_manager"
    def __init__(position):
        self.position = position
