import random

# initialize game board
board = [[" ", " ", " "] for _ in range(3)]

# print the current state of the board
def print_board():
    for row in board:
        print("|".join(row))

# prompt user for move, validate input, and update board
def user_move():
    while True:
        move = input("Enter your move (in the form x,y): ")
        try:
            x, y = movessplit(",")
            x, y = int(x), int(y)
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Invalid move! x and y must be between 0 and 2.")
            elif board[x][y] != " ":
                print("That spot is already taken! Try again.")
            else:
                board[x][y] = "X"
                break
        except ValueError:
            print("Invalid move! Please enter two integers separated by a comma.")


# generate computer move and update board
def computer_move():
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if board[x][y] == " ":
            board[x][y] = "O"
            break

# check if game is over (win or tie)
def game_over():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print_board()
            print(board[i][0] + " wins!")
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print_board()
            print(board[0][i] + " wins!")
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print_board()
        print(board[0][0] + " wins!")
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print_board()
        print(board[0][2] + " wins!")
        return True
    for row in board:
        for val in row:
            if val == " ":
                return False
    print_board()
    print("It's a tie!")
    return True

# main function that loops until game is over
def main():
    while not game_over():
        print_board()
        user_move()
        computer_move()

# call main function to start game
main()