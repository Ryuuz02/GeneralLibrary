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


class linked_lst:
    class node:
        def __init__(self, val, prev, nex):
            self.data = [prev, val, nex]

        def __getitem__(self, idx):
            return self.data[idx]

        def __setitem__(self, idx, val):
            self.data[idx] = val

        def next(self):
            return self.data[2]

        def prev(self):
            return self.data[0]

        def val(self):
            return self.data[1]

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, val):
        if len(self) not in (0, 1):
            new_node = self.node(val, self.tail, self.head)
            self.tail[2] = new_node
            self.tail = new_node
            self.head[0] = self.tail
        elif len(self) == 0:
            self.head = self.tail = self.node(val, None, None)
        else:
            self.tail = self.node(val, self.head, self.head)
            self.head[0] = self.head[2] = self.tail
        self.size += 1

    def prepend(self, val):
        if len(self) not in (0, 1):
            new_node = self.node(val, self.tail, self.head)
            self.head[0] = new_node
            self.head = new_node
            self.tail[2] = self.head
        elif len(self) == 0:
            self.append(val)
        else:
            self.size += 1
            self.head = self.node(val, self.tail, self.tail)
            self.tail[0] = self.tail[2] = self.head

    def __getitem__(self, idx):
        try:
            return self.data[idx][1]
        except IndexError:
            print("Index out of range")
            return None

    def __str__(self):
        str_lst = [str(self.head.val())]
        iterated_node = self.head.next()
        while iterated_node != self.head:
            str_lst.append(str(iterated_node.val()))
            iterated_node = iterated_node.next()
        return str(str_lst)

    def __repr__(self):
        lst_repr = [self.head.val()]
        iterated_node = self.head.next()
        while iterated_node != self.head:
            lst_repr.append(iterated_node.val())
            iterated_node = iterated_node.next()
        return lst_repr


class animal:
    def __init__(self, name, animal_class, intelligence="Simple", population="Safe", habitat="Land", diet="Herbivore",
                 egg_laying=False, legs=4, flight=False):
        self.name = name
        self.celltype = "Eukaryotic"
        self.aclass = animal_class
        self.habitat = habitat
        self.intelligence = intelligence
        self.population = population
        self.diet = diet
        self.egg_laying = egg_laying
        self.legs = legs
        self.flight = flight


class plant:
    def __init__(self, growth_type="Tree", parastic=False, ):
        self.growth_type = growth_type
        self.celltype = "Eukaryotic"
        self.parasitic = parastic


class bacteria:
    def __init__(self, name):
        self.name = name
        self.celltype = "Prokaryotic"


class virus:
    def __init__(self, name):
        self.celltype = None
        self.name = name


class bird(animal):
    def __init__(self, name, intelligence="Simple", population="safe", habitat="Air", legs=2, diet="herbivore",
                 egg_laying=True, flight=True):
        super().__init__(name, "Bird", intelligence, population, habitat, diet, egg_laying, legs, flight)


class mammal(animal):
    def __init__(self, name, intelligence="Simple", population="safe", habitat="Land", legs=4, diet="omnivore",
                 egg_laying=False, flight=False):
        super().__init__(name, "Mammal", intelligence, population, habitat, diet, egg_laying, legs, flight)


class fish(animal):
    def __init__(self, name, intelligence="Simple", population="safe", habitat="Water", legs=0, diet="carnivore",
                 egg_laying=True, flight=False):
        super().__init__(name, "Fish", intelligence, population, habitat, diet, egg_laying, legs, flight)


class amphibian(animal):
    def __init__(self, name, intelligence="Simple", population="safe", habitat="Water", legs=2, diet="carnivore",
                 egg_laying=True, flight=False):
        super().__init__(name, "Bird", intelligence, population, habitat, diet, egg_laying, legs, flight)


class reptile(animal):
    def __init__(self, name, intelligence="Simple", population="safe", habitat="Land", legs=4, diet="carnivore",
                 egg_laying=True, flight=False):
        super().__init__(name, "Reptile", intelligence, population, habitat, diet, egg_laying, legs, flight)


"""
# Example of usage
test_board = checkerboard()
test_board.create_board("chess")
test_board.print_board()
"""

"""
test_lst = linked_lst()
test_lst.prepend(2)
test_lst.prepend(1)
test_lst.append(3)
test_lst.prepend(0)
test_lst.append(4)
test_lst.append(5)
test_lst.prepend(-1)
test_lst.append(6)
print(test_lst)
"""

ostrich = bird("Ostrich", flight=False)
print(ostrich.name)
