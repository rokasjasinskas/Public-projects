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
        return self.cards.pop(0)

    def get_card_count(self):
        return len(self.cards)

class Game:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def deal_cards(self):
        for _ in range(len(self.deck.cards)):
            if len(self.player1.cards) == len(self.player2.cards):
                card = self.deck.draw_card()
                self.player1.add_card(card)
            else:
                card = self.deck.draw_card()
                self.player2.add_card(card)

    def play_round(self):
        card1 = self.player1.remove_card()
        card2 = self.player2.remove_card()

        print(f"{self.player1.name} plays: {card1}")
        print(f"{self.player2.name} plays: {card2}")

        if card1.rank > card2.rank:
            self.player1.add_cards([card1, card2])
            print(f"{self.player1.name} wins the round!")
        elif card1.rank < card2.rank:
            self.player2.add_cards([card1, card2])
            print(f"{self.player2.name} wins the round!")
        else:
            print("War!")
            self.play_war()

    def play_war(self):
        war_cards = []

        for _ in range(3):
            if self.player1.get_card_count() > 0 and self.player2.get_card_count() > 0:
                war_cards.append(self.player1.remove_card())
                war_cards.append(self.player2.remove_card())

        if self.player1.get_card_count() == 0:
            self.player2.add_cards(war_cards)
            print(f"{self.player1.name} ran out of cards. {self.player2.name} wins!")
        elif self.player2.get_card_count() == 0:
            self.player1.add_cards(war_cards)
            print(f"{self.player2.name} ran out of cards. {self.player1.name} wins!")
        else:
            card1 = self.player1.remove_card()
            card2 = self.player2.remove_card()
            war_cards.extend([card1, card2])
            print(f"{self.player1.name} plays: {card1}")
            print(f"{self.player2.name} plays: {card2}")

            if card1.rank > card2.rank:
                self.player1.add_cards(war_cards)
                print(f"{self.player1.name} wins the war!")
            elif card1.rank < card2.rank:
                self.player2.add_cards(war_cards)
                print(f"{self.player2.name} wins the war!")
            else:
                self.play_war()

    def play_game(self):
        self.deal_cards()
        round_count = 1

        while self.player1.get_card_count() > 0 and self.player2.get_card_count() > 0:
            print(f"Round {round_count}:")
            self.play_round()
            round_count += 1

        if self.player1.get_card_count() == 0:
            print(f"{self.player2.name} wins the game!")
        else:
            print(f"{self.player1.name} wins the game!")

# Example usage
game = Game("Player 1", "Player 2")
game.play_game()
