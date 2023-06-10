import random
import sys


def create_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + " of " + suit)
    random.shuffle(deck)
    return deck


def get_cards(deck):
    player1 = deck[:26]
    player2 = deck[26:]
    return player1, player2


def compare_cards(card1, card2):
    ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    rank1 = card1.split()[0]
    rank2 = card2.split()[0]
    if ranks[rank1] > ranks[rank2]:
        return 1
    elif ranks[rank1] < ranks[rank2]:
        return 2
    else:
        return 0


def round(player1, player2, round_library):
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    round_library.extend([card1, card2])
    result = compare_cards(card1, card2)
    if result == 1:
        player1.extend(round_library)
        return len(player1), len(player2)
    elif result == 2:
        player2.extend(round_library)
        return len(player1), len(player2)
    else:
        if len(player1) < 4 or len(player2) < 4:
            sys.exit("Not enough cards to continue the game.")
        round_library.extend(player1[:3])
        round_library.extend(player2[:3])
        del player1[:4]
        del player2[:4]
        return len(player1), len(player2)


def winner(player1, player2):
    if len(player1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def main():
    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")
    deck = create_deck()
    player1, player2 = get_cards(deck)
    round_library = []
    while len(player1) != 0 and len(player2) != 0:
        print(f"\n{player1_name}: {len(player1)} cards | {player2_name}: {len(player2)} cards")
        input_value = input("Enter 'begin' to start the next round or 'auto' to play automatically: ")
        if input_value.lower() == "begin" or input_value.lower() == "auto":
            num_cards_player1, num_cards_player2 = round(player1, player2, round_library)
            print(f"{player1_name} played: {round_library[-2]}")
            print(f"{player2_name} played: {round_library[-1]}")
            print(f"{player1_name} has {num_cards_player1} cards remaining.")
            print(f"{player2_name} has {num_cards_player2} cards remaining.")
            round_library = []
    print("\nGame Over!")
    print(f"{winner(player1, player2)} wins!")


if __name__ == "__main__":
    main()
