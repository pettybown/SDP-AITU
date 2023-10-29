from random import choice
from typing import List

from Car import Car
from CarSubject import CarSubject


class Factory(CarSubject):
    def __init__(self):
        super().__init__()
        self.orders: List[Car] = []
        self.finish_order: List[Car] = []

    def take_order(self, order: Car):
        print(f"Завод принял заказ на {order}")
        self.orders.append(order)

    def get_order(self, order_id: int):
        order = None
        for it in self.finish_order:
            if it.id == order_id:
                order = it
                break
        self.finish_order.remove(order)
        return order

    def processing_order(self):
        if self.orders:
            order = choice(self.orders)
            self.orders.remove(order)
            self.finish_order.append(order)
            print(f"Завод выполнил {order}")
            self.notify(order.id)
        else:
            print("Завод завершил все заказы")