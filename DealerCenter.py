from random import choice

from Car import Car
from CarObserver import CarObserver
from CarType import CarType
from Factory import Factory


class DealerCenter(CarObserver):
    def __init__(self, name: str, factory: Factory):
        self.factory = factory
        self.name = name
        self.car: Car = None

    def update(self, order_id: int):
        if self.order is not None:
            if order_id == self.order.id:
                print(f"Дилерский Центер {self.name} принял "
                      f"{self.factory.get_order(order_id)}")
                self.factory.remove_observer(self)

    def create_order(self):
        car_type = choice([CarType.Bmw,
                             CarType.Mercedes,
                             CarType.Audi])
        self.order = Car(car_type.name)
        print(f"Дилерский Центер {self.name} сделал заказ на {self.order}")
        self.factory.add_observer(self)
        self.factory.take_order(self.order)