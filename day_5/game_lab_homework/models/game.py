import random
from models.player import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def player2_as_computer():
        return Player("Player2", random.choice(["rock", "paper", "scissors"]))

    def determine_winner(player1, player2):
        if player1.choice == player2.choice:
            return None
        elif player1.choice == "rock":
            if player2.choice == "scissors":
                return player1
            else:
                return player2
        elif player1.choice == "paper":
            if player2.choice == "rock":
                return player1
            else:
                return player2
        elif player1.choice == "scissors":
            if player2.choice == "paper":
                return player1
            else:
                return player2
        