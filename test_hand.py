#!/usr/bin/env python

import unittest

from hand import Hand
from card import Card

class TestHand(unittest.TestCase):

    def test_new_hand(self):
        hand = Hand()
        cards_in_hand = hand.get_cards()
        self.assertEqual(cards_in_hand, [])

    def test_add_card(self):
        hand = Hand()
        card = Card()
        hand.add_card(card)
        cards_in_hand = hand.get_cards()
        self.assertEquals(len(cards_in_hand), 1)

if __name__ == "__main__":
    unittest.main()
