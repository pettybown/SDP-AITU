from abc import ABC, abstractmethod
class Temperature(ABC):
    @abstractmethod
    def get_temperature(self):
        pass