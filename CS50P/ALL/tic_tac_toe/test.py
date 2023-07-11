# Define the chessboard size
CHESSBOARD_SIZE = 8

# Define the white piece choices
WHITE_PIECES = ['pawn', 'rook']

# Define the chessboard dictionary
chessboard = {}

# Define a function to check if a given piece can be taken by a white piece
def can_take(piece1, pos1, piece2, pos2):
    # Convert the positions to row and column indices
    row1, col1 = ord(pos1[0]) - ord('a'), int(pos1[1]) - 1
    row2, col2 = ord(pos2[0]) - ord('a'), int(pos2[1]) - 1

    # Check if the two pieces are in the same row or column
    if row1 == row2 or col1 == col2:
        # Check if there are no other pieces blocking the way
        step_row = 0 if row1 == row2 else 1 if row1 < row2 else -1
        step_col = 0 if col1 == col2 else 1 if col1 < col2 else -1
        for r, c in zip(range(row1 + step_row, row2, step_row), range(col1 + step_col, col2, step_col)):
            if (r, c) in chessboard:
                return False
        # Check if the other piece is of the correct type to be taken
        if piece1 == 'pawn':
            return col1 == col2 + 1 and row1 == row2 + 1 or col1 == col2 - 1 and row1 == row2 + 1
        elif piece1 == 'rook':
            return True
    else:
        return False

# Ask the user to input a white piece
while True:
    white_input = input('Enter a white piece ({}): '.format('/'.join(WHITE_PIECES)))
    try:
        piece, pos = white_input.split()
        if piece in WHITE_PIECES and pos[0] in 'abcdefgh' and int(pos[1]) in range(1, CHESSBOARD_SIZE + 1):
            chessboard[pos] = piece
            break
        else:
            print('Invalid input. Please enter a valid white piece.')
    except ValueError:
        print('Invalid input. Please enter a valid white piece.')

# Ask the user to input black pieces
while True:
    black_input = input('Enter a black piece, or "done" to finish: ')
    if black_input.lower() == 'done':
        break
    try:
        piece, pos = black_input.split()
        if pos in chessboard:
            print('Invalid input. There is already a piece at that position.')
        elif piece not in WHITE_PIECES and pos[0] in 'abcdefgh' and int(pos[1]) in range(1, CHESSBOARD_SIZE + 1):
            chessboard[pos] = piece
            print('Added black piece: {} {}'.format(piece, pos))
        else:
            print('Invalid input. Please enter a valid black piece.')
    except ValueError:
        print('Invalid input. Please enter a valid black piece.')

# Find the black pieces that the white piece can take
print('Black pieces that the white piece can take:')
for pos, piece in chessboard.items():
    if piece in WHITE_PIECES:
        if can_take(piece, pos, 'black', list(chessboard.keys())[list(chessboard.values()).index('black')]):
            print('- {} {}'.format(piece, pos))
