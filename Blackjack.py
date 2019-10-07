import pyCardDeck
from typing import List
from getch import getch, pause
from Player import Player

import sys
import time

class Blackjack:

  def __init__(self, players: List[Player]):
    self.deck = pyCardDeck.Deck()
    self.deck.load_standard_deck()
    self.players = players
    self.scores = {}
    print("Created a game with {} players".format(len(self.players)))
  
  def blackjack(self):
    """
    The main blackjack game sequence.

    Each player takes an entire turn before moving on.

    If each player gets a turn and no one has won, the player or players
    with the highest score below 21 are declared the winner.
    """
    print("Setting up...")
    time.sleep(1)
    print("Shuffling...")
    time.sleep(1)
    self.deck.shuffle()
    print("All shuffled!")
    print("Dealing...")
    self.deal()
    print("\nLet's play!")

    for player in self.players:
      print("{}'s turn: ".format(player.name))
      self.play_turn(player)
    else:
      print("That's the last turn. Determining the winner...")
      self.find_winner()
  
  def deal(self):
    """
    Deals two cards to each player.
    """
    for _ in range(2):
      for player in self.players:
        time.sleep(1)
        new_card = self.deck.draw()
        player.hand.append(new_card)
        print("Dealt {} the {}.".format(player.name, str(new_card)))
  
  def find_winner(self):
    """
    Finds the highest score, then finds which player(s) have that score,
    and reports them as the winner.
    """
    winners = []
    try:
      win_score = max(self.scores.values())
      for key in self.scores.keys():
        if self.scores[key] == win_score:
          winners.append(key)
        else:
          pass
        
      win_string = " & ".join(winners)
      print("And the winner is... {}!".format(win_string))
    except ValueError:
      print("Dealer won!")
  
  def hit(self, player):
    """
    Adds a card to the player's hand and states which card was drawn.
    """
    new_card = self.deck.draw()
    player.hand.append(new_card)
    print("Drew the {}".format(str(new_card)))
  
  def play_turn(self, player):
    """
    An individual player's turn.

    If a player's  cards are an ace and a ten or court card,
    the player has a blackjack and wins.

    If a player's cards total more than 21, the player loses.

    Otherwise, it takes accepts a key input to determine whether to hit or stand.  
    """
    points = self.sum_hand(player)
    if points == 21:
      print("{} wins!".format(player.name))
      sys.exit(0) # End if someone wins
    elif points > 21:
      print("Bust!")
      return

    command = getch()
    while command != 'h' and command != 's':
      print("Invalid command. Press 'S' to stand 'H' to hit.")
      print("{}'s turn: ".format(player.name))
      command = getch()
    
    if command == 'h':
      print("Hit.")
      self.hit(player)
    elif command == 's':
      print("Standing at {} points.".format(str(points)))
      self.scores[player.name] = points
      
  
  def sum_hand(self, player):
    """
    Converts ranks of cards into point values for scoring purposes.
    'K', 'Q', and 'J' are converted to 10.
    'A' is converted to 1 (for simplicity), but if the first hand is an ace
    and a 10-valued card, the player wins with a blackjack.
    """
    vals = [card.rank for card in player.hand]
    int_vals = []

    while len(vals) > 0:
      value = vals.pop()
      try:
        int_vals.append(int(value))
      except ValueError:
        if value in ['K', 'Q', 'J']:
          int_vals.append(10)
        elif value == 'A':
          int_vals.append(1)
    
    if int_vals == [1, 10] or int_vals == [10, 1]:
      print("Blackjack!")
      return (21)
    else:
      points = sum(int_vals)
      print("{}'s current score: {}".format(player.name, str(points)))
      return (points)