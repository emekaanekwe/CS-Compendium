
import numpy

class Cards:
    def __init__(self):
        self.cards = []
        self.deck = []

    def make_card(self):
        card = {"acion-name": "action",
                "number": 1}
        self.cards.append(card)
        return card

    # put card in deck list
    def make_deck(self):
        for i in range(1, len(self.deck)+1):
            card = self.make_card()
            self.deck.append(card)
        return self.deck

    def add_card_to_deck(self, card):
        self.deck.append(card)
        return self.deck
