#!/usr/bin/env python
"""Test module for the Game class"""

import unittest
import unittest.mock as mock

from game import Game


class TestGame(unittest.TestCase):
    """Test class for Game"""

    def test_start_new_game_prompts_for_number_of_players(self):
        gameDisplayer = mock.MagicMock()
        game = Game(gameDisplayer)
        gameDisplayer.prompt_for_players.assert_any_call()

    def test_start_new_game_prompts_players_in_turn_for_action(self):
        gameDisplayer = mock.MagicMock()
        gameDisplayer.prompt_for_players.return_value =  ["alex", "bob"]
        game = Game(gameDisplayer)

        expected_first_calls = [mock.call("alex"), mock.call("bob"), mock.call("alex")]
        self.assertEqual(gameDisplayer.prompt_for_action.call_args_list[:3],
                          expected_first_calls)



if __name__ == "__main__":
    unittest.main()
