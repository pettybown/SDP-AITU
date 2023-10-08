from abc import abstractmethod, ABC
class IPizzaBase(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass
class PizzaBase(IPizzaBase):
    def __init__(self, cost):
        self.cost = cost
    def cost(self):
        return self.cost
class IDecorator(IPizzaBase):
    @abstractmethod
    def name(self) -> str:
        pass
class PizzaSalyami(IDecorator):
    def __init__(self,  traditional : IPizzaBase, pizza_cost):
        self.__traditional = traditional
        self.__cost = pizza_cost
        self.__name = "Пицца Салями"

    def cost(self) -> float:
        return (self.__cost + self.__traditional.cost()) * 100.5
    def name(self) -> str:
        return self.__name
class PizzaBolognese(IDecorator):
    def __init__(self, thin : IPizzaBase, pizza_cost : int):
        self.__thin = thin
        self.__cost = pizza_cost
        self.__name = "Пицца Болоньезе"
    def cost(self) -> float:
        return (self.__cost + self.__thin.cost) * 100.25

    def name(self) -> str:
        return self.__name

def print_pizza(pizza : IDecorator) -> None:
    print(f"Ваша пицца {pizza.name()}, ее стоимость с учетом теста = {pizza.cost()} тенге")
pizza = PizzaBase(10)
Bolongnese = PizzaBolognese(pizza, 10)
print_pizza(Bolongnese)

