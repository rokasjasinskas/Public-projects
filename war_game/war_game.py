import random

class Card:
    def init(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def str(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def init(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, card1, card2):
        self.cards.extend(card1, card2)

    def remove_card(self, card):
        for i, c in enumerate(self.cards):
            if c == card:
                return self.cards.pop(i)
        return None

    def get_card_count(self):
        return len(self.cards)



class game: 
    @staticmethod 
    def comparison(1card, 2card):
        if 1card = 2card: 
            war(1card, 2card)
        else:
           Player.add_cards (1card, 2card) 

    def war_game: 
        try: 
            deck1 = 
            deck2 = 
    
    def war: 
        pass

    def end_game: 
        pass 









#def start
# create dec of cards
# put them in random order
# return dec as library


#def get_card:
# split to two parts 
# Part 1 is player 1 
# Part 2 is player 2 
# return players decs as library 



#def round(player 1, player2):
# if input = begin, round starts
	# top card from each deck is picked and compared 
	# cards are putted into round library --- not sure than I should implent it before or after comparison
	# if players cards is higher:
		# takes both of cards
		#its library is updated with round library. 
	# elif players cards are equal:
		# additional card from each dect is added
		# one more additiona card from each dect is added to round library 
		# last added cards is compared player whose card is higher takes both of cards - its library is updated with round library
	# return number of cards in decs after round
#else: 
	#sys.exit



#def winner:
# compare player 1 and player 2 decs size. 
# if player decs = 0
	# lost
# else:
	# Won
	# return player name


#def main
# input player 1 and player 2 names
# mix of cards
# players gets cards
# try unit one of players dec is != 0; 
	# goes round - return number of cards in dec
# Announce winner