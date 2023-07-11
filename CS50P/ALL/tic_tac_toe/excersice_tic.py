# we will need to initialise and store the boar state - information about where move have been made
board_state = get_new_board_state()

#since we will be using a loop to repeatedly make moves until the games end, we will use a variable to track wheher the game should contine.
game_in_progress = True

while game_in_progress:
    player_move = ask_for_user_input()

    # We update the board state with the player's move
    board_state = update_board_state(board_state)

    if player_has_won:
        # The player made a winning move, we need to end the game and annouce it, print the board state and ensure the loop ends, ending the program
        game_in_progress = False
        print("You have won!")
        print_board (board_state)
    else:
        # If the game hasn't ended, get the computer's move. The function will need to know the board state to choose a valid move
        computer_move = get_computer_move(board_state)

        #we update the board state and check if there was a win
        board_state = update_board_state (board_state, computer_move)
        computer_has_won = check_for_win(board_state)

        if computer_has_won:
            # The computer won. So same thing as when the player won
            game_in_progress = False
            print("You have won!")
            Print_board(board_state)

# Listing the functions we will need to implement:
def get_new_board_state():
    pass

def ask_for_use_input():
    pass

def check_for_win(board_state):
    pass

def update_board_state(board_state, move):
    pass

def get_computer_move (board_state):
    pass

def print_board (board_state):
    pass
