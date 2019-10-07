from Blackjack import Blackjack
from Player import Player


def main():
    print("Welcome to Blackjack!")
    num_players = int(input("How many players (1 to 7)? "))
    players = []
    for i in range(1, num_players + 1):
        name = input("Player {} name? ".format(i))
        players.append(Player(name))
    game = Blackjack(players)
    game.blackjack()


if __name__ == '__main__':
    main()