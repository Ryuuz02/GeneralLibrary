# imports shuffle to shuffle the deck
from random import shuffle


# Deck class, for cards
class deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
        self.numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.create_deck()

    # Creates each combination of number/suit and puts it in the cards list
    def create_deck(self):
        self.cards = []
        for suit in self.suits:
            for number in self.numbers:
                self.cards.append(card(suit, number))

    # Prints each card from the deck
    def print_deck(self):
        for deck_card in self.cards:
            print(deck_card)

    # Shuffles the deck 10 times (for true randomness)
    def shuffle_deck(self):
        for i in range(10):
            shuffle(self.cards)


class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    # Overwrites the way it prints
    def __str__(self):
        return str(self.number) + " of " + self.suit


# Makes a new deck
test_deck = deck()
# Shuffles the deck
test_deck.shuffle_deck()
# Prints the deck
test_deck.print_deck()
