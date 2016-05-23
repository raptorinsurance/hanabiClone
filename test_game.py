#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock

from game import Game

class TestGame(unittest.TestCase):

    def test_start_new_game_prompts_for_number_of_players(self):
        gameDisplayer = Mock()
        game = Game(gameDisplayer)


if __name__ == "__main__":
    unittest.main()
