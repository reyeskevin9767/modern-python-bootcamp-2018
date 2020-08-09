
# * Deck Iterable

from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):
        suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        values = ("A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        acutal = min([count, num])
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-acutal:]
        self.cards = self.cards[:-acutal]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


d = Deck()
d.shuffle()
# card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# print(hand)
# print(d.cards)

for card in d:
    print(card)
