from DealerCenter import DealerCenter
from Factory import Factory

if __name__ == "__main__":
    names = ['Allur', 'Bergimber',
             'Sakamato']
    factory = Factory()
    dealers = [DealerCenter(name, factory) for name in names]
    for dealer in dealers:
        print("*" * 30)
        dealer.create_order()
    print("*" * 4 + "Завод приступает к выполнению заказов" + 4 * "*")
    for _ in range(4):
        print("*" * 30)
        factory.processing_order()
