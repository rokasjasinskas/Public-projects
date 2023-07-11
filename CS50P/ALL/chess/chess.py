# Define the two pieces that the user can choose from
PIECES = ['pawn', 'rook']

# Ask the user for the white piece and its location
while True:
    white_piece = input(f"Choose a white piece ({PIECES[0]} or {PIECES[1]}): ")
    if white_piece in PIECES:
        break
    else:
        print("Invalid input. Please choose either 'pawn' or 'rook'.")
while True:
    white_coords = input("Enter the location of the white piece (e.g. a1): ")
    if len(white_coords) == 2 and white_coords[0] in 'abcdefgh' and white_coords[1] in '12345678':
        break
    else:
        print("Invalid input. Please enter a valid coordinate (e.g. a1).")

# Ask the user for the black pieces
black_pieces = []

while len(black_pieces) < 16:
    black_piece = input("Enter the location of a black piece, or 'done' if finished: ")
    if black_piece == 'done':
        if len(black_pieces) == 0:
            print("You must add at least one black piece.")
        else:
            break
    elif len(black_piece) != 2 or black_piece[0] not in 'abcdefgh' or black_piece[1] not in '12345678':
        print("Invalid input. Please enter a valid coordinate (e.g. a1).")
    elif black_piece in black_pieces:
        print("This black piece has already been added.")
    elif black_piece == white_coords:
        print("You cannot place a black piece on the same square as the white piece." )
    else:
        black_pieces.append(black_piece)
        print(f"Added black piece at {black_piece}.")

# Determine which black pieces the white piece can take
can_take = []
for black_piece in black_pieces:
    if white_piece == 'pawn':
        # Check if the white pawn can take the black piece diagonally
        if abs(ord(white_coords[0]) - ord(black_piece[0])) == 1 and white_coords[1] != black_piece[1]:
            can_take.append(black_piece)
    elif white_piece == 'rook':
        # Check if the white rook can take the black piece horizontally or vertically
        if white_coords[0] == black_piece[0] or white_coords[1] == black_piece[1]:
            can_take.append(black_piece)

# Print the black pieces that the white piece can take
if len(can_take) == 0:
    print("The white piece cannot take any black pieces.")
else:
    print(f"The white piece can take the following black pieces: {', '.join(can_take)}.")