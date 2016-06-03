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
        expected_calls.append(mock.call("Please enter the name of the first player: "))
        expected_calls.append(mock.call("Please enter the name of the second player: "))
        mock_input.assert_has_calls(expected_calls)

    def test_ask_for_third_player(self, mock_input):
        self.game_displayer.prompt_for_players()
        expected_calls = []
        expected_calls.append(mock.call("Would you like to add a third player?"))
        mock_input.assert_has_calls(expected_calls)

    def test_return_players_when_no_extra_players_requested(self, mock_input):
        expected_players = ["Alex", "Bob"]
        mock_input.side_effect = expected_players.append("n")
        actual_players = self.game_displayer.prompt_for_players()
        self.assertEqual(expected_players, actual_players)






if __name__ == "__main__":
    unittest.main()
