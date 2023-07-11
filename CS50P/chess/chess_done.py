# GLOBAL VARIABLES
#white library
white_coordinations = []

# white type
white_type = ["pawn", "rook"]

# white name
white_name = []

# black library
black_coordinations = []

# can_take liberary
can_take = []

# describe invalid message
def invalid ():
    print("Invalid input")

#----main

def main():
    white_input()
    black_input()
    fight()
    results()

#-------white
# define whit input function whitch use global variables and output user choose.

def white_input():

    global white_type
    global white_coordinations
    global white_name

    while len (white_coordinations) == 0:
        white_name = input(f"Choose a white piece ({white_type[0]} or {white_type[1]}): ")
        while white_name in white_type:
            white_coordinations = input("Enter the location of the white piece (e.g. a1): ")
            if len(white_coordinations) == 2 and white_coordinations[0] in "abcdefgh" and white_coordinations[1] in "12345678":
                    break
            else:
                 invalid()
        else:
            invalid()


#-------black

def black_input():
    def black_over():
        print ("Black piece turn is over. Black pieces is in:", " and ".join(black_coordinations))

    global black_coordinations
    black_coord = []
    while len (black_coordinations) < 16:
        black_coord = input("Enter the location of the black piece (e.g. a1) or 'done' to finish: ")
        if black_coord == "done":
            if len (black_coordinations) == 0:
                print ("You have to enter atleast one black piece. ")
            else:
                black_over()
                break
        elif len(black_coord) != 2 or black_coord[0] not in "abcdefgh" or black_coord[1] not in "12345678":
            invalid()
        elif black_coord == white_coordinations:
            print ("This place is taken by white piece. Try once again. ")
        elif black_coord in black_coordinations:
            print ("This place is taken by black piece. Try once again. ")
        else:
            black_coordinations.append(black_coord)
            print(f"Added black piece at {black_coord}")
    else:
        black_over()


# Define black_pieces as emty. It has to take place in abcdefgh and 12345678 - done
# Define enter of black pieces by user input - done
# Black pieces can't be more than 16 - done
# If black pieces is 16 - show resuls - done
# if black piece is equal to 0 - ask once again - done
# black piece is equal to black piece - done
# if black piece is equal to white piece - show error - done
# if black piece is wrong format - show error - done
# if black piece is "done" - end loop - done
# if black piece is correct - update - done
# update main dictionary with values


#------- fight
def fight():
    def update():
        can_take.append(black_piece)
    def eliminate():
        pass

    global can_take

    for black_piece in black_coordinations:
        if white_name == "pawn":
            if abs(ord(white_coordinations[1]) - ord(black_piece[1])) == 1 and white_coordinations[0] - black_piece[0] == -1 :
                update()
        elif white_name == "rook":
            if (white_coordinations[0] == black_piece[0]) or (white_coordinations[1] == black_piece[1]):
                update()
                eliminate()


# create list can_take
# check if white piece is pawn or rook
# check which black pieces pawn can take and add to can_take list
# check which black pieces rook can take and add to can_take list


#------ results
def results (can_take):
    global can_take

    if len(can_take) > 0 :
        print("White can take these black piece:", " and ".join(can_take))

    else:
        print("White cannot take any black pieces" )

# if list is emty print "White can't take"
# if list is not emty print values with text "white can take these"



main()