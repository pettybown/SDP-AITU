from CarType import CarType


class Car:
    car_id: int = 1
    def __init__(self, car_type : CarType):
        self.id = Car.car_id
        self.type = car_type
        Car.car_id += 1
    def __str__(self):
        return f"машину под моделью {self.type}"