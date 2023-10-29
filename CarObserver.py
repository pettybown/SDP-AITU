from abc import ABC, abstractmethod


class CarObserver(ABC):
    @abstractmethod
    def update(self, car):
        ...