# -*- coding: utf-8 -*-
import random

class Card:
    
    #Represents a playing card with a suit and rank.
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, rank):

        if not (suit in Card.suits and rank in Card.ranks):
            raise ValueError("Invalid card: " + str(suit) + " " + str(rank))

        self.suit = suit
        self.rank = rank
    #output card in rank suit format, e.g. 7♠
    def __str__(self):
        return f"{self.rank}{self.suit}"
    #Output a card like a physical card
    def card_str(self):
        if self.rank == "10":
            return f"""
            ┌─────┐
            │10   │
            │  {self.suit}  │
            │   10│
            └─────┘
            """
        else:
            return f"""
            ┌─────┐
            │{self.rank}    │
            │  {self.suit}  │
            │    {self.rank}│
            └─────┘
            """

class Deck:

    #Initializes a Deck object with a full deck of 52 cards.
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def debug_print_deck(self):
        for card in self.cards:
            print(card.card_str())
    
    def deal(self, num_cards = 1):
        pass
    
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

playerNum = None
while not playerNum:
    try: 
        playerNum = int(input("How many players: "))
    except:
        print("Input an integer")
players = []
for i in range(playerNum):
    players.append(Player(input("Enter a name for player %s: "%(i+1))))
for i in players:
    print(i.name)
deck=Deck()
deck.shuffle()

