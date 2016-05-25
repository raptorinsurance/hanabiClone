#!/usr/bin/env python

import unittest
import unittest.mock as mock

from game import Game

class TestGame(unittest.TestCase):

    def test_start_new_game_prompts_for_number_of_players(self):
        gameDisplayer = mock.Mock()
        game = Game(gameDisplayer)
        gameDisplayer.prompt_for_players.assert_any_call()


if __name__ == "__main__":
    unittest.main()
