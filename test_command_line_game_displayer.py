#!/usr/bin/env python
import unittest
import unittest.mock as mock
from command_line_game_displayer import CommandLineGameDisplayer


@mock.patch('command_line_game_displayer.get_input')
class TestCommandLineGameDisplayer(unittest.TestCase):

    def setUp(self):
        self.game_displayer = CommandLineGameDisplayer()

    def test_player_name_prompt_first_two_players(self, mock_input):
        self.game_displayer.prompt_for_players()
        expected_calls = []
        expected_calls.append(mock.call("Please enter the name of player 1: "))
        expected_calls.append(mock.call("Please enter the name of player 2: "))
        mock_input.assert_has_calls(expected_calls)

    def test_ask_for_third_player(self, mock_input):
        self.game_displayer.prompt_for_players()
        expected_calls = []
        expected_calls.append(mock.call("Would you like to add player 3?"))
        mock_input.assert_has_calls(expected_calls)

    def test_return_players_when_no_extra_players_requested(self, mock_input):
        expected_players = ["Alex", "Bob"]
        mock_input.side_effect = expected_players + ["n"]
        actual_players = self.game_displayer.prompt_for_players()
        self.assertEqual(expected_players, actual_players)

    def test_add_extra_player_when_requested(self, mock_input):
        mock_input.side_effect = ["Alex", "Bob", "y", "Charlie", "n"]
        actual_players = self.game_displayer.prompt_for_players()
        mock_input.assert_any_call("Please enter the name of player 3: ")

    def test_ask_for_fourth_player(self, mock_input):
        mock_input.side_effect = ["Alex", "Bob", "y", "Charlie", "n"]
        self.game_displayer.prompt_for_players()
        mock_input.assert_called_with("Would you like to add player 4?")

    def test_no_prompt_for_six_players(self, mock_input):
        mock_input.side_effect = ["Alex", "Bob",
                                  "y", "Charlie",
                                  "y", "David",
                                  "y", "Earl"]
        actual_players = self.game_displayer.prompt_for_players()
        expected_players = ["Alex", "Bob", "Charlie", "David", "Earl"]
        self.assertEqual(expected_players, actual_players)

# TODO add test for non-yes/no responses




if __name__ == "__main__":
    unittest.main()
