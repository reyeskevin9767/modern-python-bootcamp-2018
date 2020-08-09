
# * Test
from card import Card
from deck import Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        self.assertEqual(self.card.value, "Hearts")
        self.assertEqual(self.card.suit, 'A')

    def test_repr(self):
        self.assertEqual(repr(self.card), "Hearts of A")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck(self):
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_suffiecient_cards(self):
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insuffiecient_cards(self):
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()

#     def test_deal_card(self):
#         self.assertEqual(self.deck.deal_card().__repr__(), 'K of Spades')
#     def test_deal_hand(self):
#         self.assertEqual(self.deck._deal(4).__repr__(), '[K of Hearts, K of Diamonds, K of Clubs, K of Spades]')
#     def test_suffle(self):

#         self.assertEqual(self.deck.shuffle(), "Only full decks can be shuffled")

#     # def shuffle(self):
#     #     if self.count() < 52:
#     #         raise ValueError("Only full decks can be shuffled")
#     #     shuffle(self.cards)
#     #     return self

#     # def deal_hand(self, hand_size):
#     #     return self._deal(hand_size)
#     # def deal_card(self):
#     #     return self._deal(1)[0]
#     # def _deal(self, num):
#     #     count = self.count()
#     #     acutal = min([count,num])
#     #     if count == 0:
#     #         raise ValueError('All cards have been dealt')
#     #     cards = self.cards[-acutal:]
#     #     self.cards = self.cards[:-acutal]
#     #     return cards

# # class RobotTests(unittest.TestCase):
# #     def setUp(self):
# #         self.mega_man = Robot("Mega Man", battery=50)
# #     def test_charge(self):
# #         self.mega_man.charge()
# #         self.assertEqual(self.mega_man.battery, 100)

# #     def test_say_name(self):
# #         self.mega_man = Robot("Mega Man", battery=50)
# #         self.assertEqual(self.mega_man.say_name(),
# #                          "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
# #         self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()
