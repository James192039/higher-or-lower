# -*- coding: utf-8 -*-
import random

class Card:
    
    #Represents a playing card with a suit and rank.
    suits = ["♠", "♦", "♣", "♥"]
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
    def __int__(self):
        val = Card.ranks.index(self.rank) + 1
        return val

class Deck:

    #Initializes a Deck object with a full deck of 52 cards.
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def debug_print_deck(self):
        for card in self.cards:
            print(card.card_str())
    #Return the first card in cards list, display the card, remove the card from the cards list
    def deal(self, num_cards = 1):
        print(self.cards[0].card_str())
        return self.cards.pop(0)
    #returns true if nextCard > nextCard (inc. rank order), else returns False
    def checkHigh(self, currentCard, nextCard):
        if int(nextCard) < int(currentCard):
            return False
        elif int(nextCard) > int(currentCard) or (int(nextCard)==int(currentCard) and Card.suits.index(nextCard.suit) < Card.suits.index(currentCard.suit)):
            return True
        else:
            return False
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.currentCard=None
        self.active = True

playerNum = None
while not playerNum:
    try: 
        playerNum = int(input("How many players: "))
    except:
        print("Input an integer")
players = []
for i in range(playerNum):
    players.append(Player(input("Enter a name for player %s: "%(i+1))))

deck=Deck()
deck.shuffle()

for player in players:
    print(f"{player.name}'s starting card:")
    player.currentCard = deck.deal()
deck=Deck()
deck.shuffle()
while len(deck.cards)>0 and any([player.active for player in players]):
    for currentPlayer in players:
        print("-------------------NEXT PLAYER---------------------")
        if currentPlayer.active:
            print(f"Current Player: {currentPlayer.name}\nCurrent score: {currentPlayer.score}\nCurrent card: {currentPlayer.currentCard}")
            playerInput = input("Will the next card be higher or lower \n(rank order for face value ties = ♠, ♦, ♣, ♥)\n").lower()
            while playerInput not in ["higher", "high", "h", "lower", "low","l"]:
                playerInput = input("please input higher or lower: ")
            nextCard = deck.deal()
            isHigher = deck.checkHigh(currentPlayer.currentCard, nextCard)
            if (playerInput in ["higher", "high", "h"] and isHigher) or (playerInput in ["lower", "low","l"] and not isHigher):
                print("Correct")
                print(currentPlayer.score)
                currentPlayer.score = currentPlayer.score + 1
                print(currentPlayer.score)
                currentPlayer.currentCard = nextCard
            else:
                print("Incorrect")
                currentPlayer.score = 0
                currentPlayer.active=False
                continue
            playerInput = input("Continue playing (your score resets to 0 on an incorrect guess): ").lower()
            while not playerInput in ["y","yes","n","no"]:
                playerInput = input("Enter y, yes, n, or no: ")
            if playerInput in ["n", "no"]:
                currentPlayer.active=False
                continue
        else:
            print(f"{currentPlayer.name} is out and will be skipped")
print("""-------------------GAME END---------------------
Player Scores:""")
for i in players:
        print(f"Name: {i.name}, Score: {i.score}")
