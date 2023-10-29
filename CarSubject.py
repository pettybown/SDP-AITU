from abc import ABC
from typing import List
from CarObserver import CarObserver


class CarSubject(ABC):
    def __init__(self):
        self.observers: List[CarObserver] = []

    def add_observer(self, observer: CarObserver):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer: CarObserver):
        self.observers.remove(observer)

    def notify(self, order_id: int):
        for observer in self.observers:
            observer.update(order_id)