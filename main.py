class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата с помощью кредитной карты: {amount} тенге")

class KaspiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата через Kaspi: {amount} тенге")

class Order:
    def __init__(self, total_amount, payment_strategy):
        self.total_amount = total_amount
        self.payment_strategy = payment_strategy

    def checkout(self):
        self.payment_strategy.pay(self.total_amount)



if __name__ == "__main__":
    order = Order(1000, CreditCardPayment())

    order.checkout()
