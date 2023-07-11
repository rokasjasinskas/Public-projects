import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

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

    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_card(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            return None

    def get_card_count(self):
        return len(self.cards)


def main():
    player1_name = input("Player 1 name: ")
    player2_name = input("Player 2 name: ")

    deck = Deck()

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    while deck.cards:
        player1.add_card(deck.draw_card())
        player2.add_card(deck.draw_card())

    round_count = 0

    while player1.get_card_count() > 0 and player2.get_card_count() > 0:
        round_count += 1
        print(f"Round {round_count}:")

        card1 = player1.remove_card()
        card2 = player2.remove_card()


        print(f"{player1.name} plays {card1}")
        print(f"{player2.name} plays {card2}")

        if card1.rank > card2.rank:
            player1.add_cards([card1, card2])
            print(f"{player1.name} wins the round!")
        elif card1.rank < card2.rank:
            player2.add_cards([card1, card2])
            print(f"{player2.name} wins the round!")
        else:
            print("War!")
#def start
# create dec of cards
# put them in random order
# return dec as library



            war_cards = [card1, card2]
            war_continue = True

            while war_continue:
                if player1.get_card_count() < 3 or player2.get_card_count() < 3:
                    war_continue = False
                    break

                for _ in range(3):
                    war_cards.append(player1.remove_card())
                    war_cards.append(player2.remove_card())

                war_card1 = player1.remove_card()
                war_card2 = player2.remove_card()

                war_cards.extend([war_card1, war_card2])

                print(f"{player1.name} plays {war_card1}")
                print(f"{player2.name} plays {war_card2}")

                if war_card1.rank > war_card2.rank:
                    player1.add_cards(war_cards)
                    print(f"{player1.name} wins the war!")
                    war_continue = False
                elif war_card1.rank < war_card2.rank:
                    player2.add_cards(war_cards)
                    print(f"{player2.name} wins the war!")
                    war_continue = False
                else:
                    print("War continues!")

    if player1.get_card_count() == 0:
        print(f"{player2.name} wins the game!")
    elif player2.get_card_count() == 0:
        print(f"{player1.name} wins the game!")
    else:
        print("It's a tie! The game ends in a draw.")

if __name__ == "__main__":
    main()
