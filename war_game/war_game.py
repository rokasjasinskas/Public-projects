

class Deck: 
	rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
	suit = ["Spades", "Hearts", "Diamonds", "Clubs"]

	def __init__(self, suit, rank): 
		self.suit = suit
		self.rank = rank


	def hold_deck():
		cards = []
		for suit in Deck.suit: 
			for rank in Deck.rank:
				cards.append(suit, rank)
		print(cards)

		

Deck.hold_deck()
















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