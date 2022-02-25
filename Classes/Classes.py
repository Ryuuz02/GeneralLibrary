# imports shuffle to shuffle the deck
from random import shuffle
from colorama import Back, Fore


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


# Class for cards in a deck
class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    # Overwrites the way it prints
    def __str__(self):
        return str(self.number) + " of " + self.suit


# Class for a chessboard, preset height/width of 8, but can be changed
class checkerboard:
    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width
        self.board = []
        self.create_board()

    # Function to make the board, alternates each spots colors between white/black
    def create_board(self, boardtype="empty"):
        self.board = []
        for row in range(0, self.height):
            self.board.append([])
            for col in range(0, self.width):
                if boardtype == "checkers":
                    if (row + col) % 2 == 0:
                        self.board[row].append(spot("white"))
                    elif row <= 2:
                        self.board[row].append(spot("black", Fore.WHITE + " ● "))
                    elif row >= 5:
                        self.board[row].append(spot("black", Fore.RED + " ● "))
                    else:
                        self.board[row].append(spot("black"))
                elif boardtype == "chess":
                    chess_layout = [" R ", " N ", " B ", " Q ", " K ", " B ", " N ", " R "]
                    if row == 0:
                        if (row + col) % 2 == 0:
                            self.board[row].append(spot("white", Fore.RED + chess_layout[col]))
                        else:
                            self.board[row].append(spot("black", Fore.RED + chess_layout[col]))
                    elif row == 1:
                        if (row + col) % 2 == 0:
                            self.board[row].append(spot("white", Fore.RED + " P "))
                        else:
                            self.board[row].append(spot("black", Fore.RED + " P "))
                    elif row == 6:
                        if (row + col) % 2 == 0:
                            self.board[row].append(spot("white", Fore.CYAN + " P "))
                        else:
                            self.board[row].append(spot("black", Fore.CYAN + " P "))
                    elif row == 7:
                        if (row + col) % 2 == 0:
                            self.board[row].append(spot("white", Fore.CYAN + chess_layout[col]))
                        else:
                            self.board[row].append(spot("black", Fore.CYAN + chess_layout[col]))
                    else:
                        if (row + col) % 2 == 0:
                            self.board[row].append(spot("white"))
                        else:
                            self.board[row].append(spot("black"))
                elif boardtype == "empty":
                    if (row + col) % 2 == 0:
                        self.board[row].append(spot("white"))
                    else:
                        self.board[row].append(spot("black"))

    # Function to print out the board
    def print_board(self):
        for row in range(0, self.height):
            print((Back.RESET + "").join(self.row_to_str_lst(row)) + Back.RESET)

    # Converts an entire row to a list of strings
    def row_to_str_lst(self, row_num):
        convert_lst = []
        for space in self.board[row_num]:
            convert_lst.append(space.symbol)
        return convert_lst


# Class for a space in the board
class spot:
    def __init__(self, color, symbol=Fore.WHITE + "   "):
        color = color.lower()
        # Depending on what color it needs to be, changes the background to match
        if color == "white":
            self.symbol = Back.WHITE + symbol
        elif color == "black":
            self.symbol = Back.BLACK + symbol


# Example of usage
test_board = checkerboard()
test_board.create_board("chess")
test_board.print_board()
