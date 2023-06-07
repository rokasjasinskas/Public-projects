##################################################################################
War Card Game
##################################################################################

This is a children's card game implementation of the classic game called "War." The program is developed using Object-Oriented Programming (OOP) principles.

##################################################################################
Game Rules
##################################################################################

The game follows the standard rules of the War card game. Here's a brief overview:

The deck is divided equally among the players.

Each player places their top card face-up on the table simultaneously. The player with the highest card value takes all the cards played and adds them to the bottom of their deck.

If there is a tie in card values, a "war" occurs. Each player places three additional cards face-down and one card face-up. The player with the highest face-up card wins the war and takes all the cards played.

If a player runs out of cards during a war, they lose the game.

The game continues until one player has all the cards and is declared the winner.





##################################################################################
Requirements
##################################################################################


##################################################################################
Functional Requirements
##################################################################################

The program should simulate the War card game for two players.

The game should be interactive, displaying the current state and progress of the game.

The program should allow players to make moves by entering a command.

The game should handle ties and wars according to the standard rules.

The program should track the number of cards each player has during the game.

The game should end when one player has all the cards and display the winner.

##################################################################################
Technical Requirements
##################################################################################

The program should be implemented using Python and follow the Object-Oriented Programming (OOP) paradigm.

The code should be modular and organized into classes and functions.

The implementation should utilize Git for version control, with regular commits and descriptive commit messages.

The code should be well-documented with inline comments and a clear structure.

The program should provide clear instructions and error handling for user interactions.

The README file should contain clear setup instructions, game rules, and requirements.






##################################################################################
Structure
##################################################################################


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
	
# def winner: 
	# compare player 1 and player 2 decs size. 
	# if player decs = 0
		# lost
	# else:
		# Won
		# return player name

# def main
	# input player 1 and player 2 names
	# mix of cards
	# players gets cards
	# try unit one of players dec is != 0; 
		# goes round - return number of cards in dec
	# Announce winner
