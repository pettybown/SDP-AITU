from abc import ABC, abstractmethod
from random import randint

class MonopolyGame(ABC):
    @abstractmethod
    def play(self):
        pass

class BasicMonopolyGame(MonopolyGame):
    def __init__(self):
        self.players = []
        self.current_player = 0
        self.board = "West Monopoly"

    def play(self):
        while True:
            print(f"Rolling dices: ..., and dices show {randint(2, 12)}")
            print(f"Now your turn {basic_game.players[randint(0,1)].name}")
            print("Will you throw dices?")
            action = input()

            if action == "yes":
                continue
            else:
                exit()

class MonopolyGameDecorator(MonopolyGame, ABC):
    def __init__(self, game):
        self._game = game

class LuxuryEditionDecorator(MonopolyGameDecorator):
    def play(self):
        self._game.play()
        print("Luxury edition features are included.")

class SpeedyVersionDecorator(MonopolyGameDecorator):
    def play(self):
        self._game.play()
        print("Speedy version rules are applied.")

class Player:
    def __init__(self, name, initial_balance=1500):
        self.name = name
        self.balance = initial_balance

if __name__ == "__main__":
    basic_game = BasicMonopolyGame()
    player1 = Player("Nurali")
    player2 = Player("Rahat")
    basic_game.players = [player1, player2]

    print("Playing Basic Monopoly Game:")
    print(basic_game.play())
