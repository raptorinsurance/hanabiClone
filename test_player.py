#!/usr/bin/env python
import unittest

from player import Player

class TestPlayer(unittest.TestCase):

    def test_create_player(self):
        player = Player()

if __name__ == "__main__":
    unittest.main()
