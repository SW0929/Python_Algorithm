class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # 다중 상속시 맨 처음 선언한 클래스만 init 호출
        super().__init__
        # 다중 상속시 각각 명시적으로 초기화 해줘야 함.
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()