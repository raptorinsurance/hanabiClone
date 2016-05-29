#!/usr/bin/env python
import unittest
import unittest.mock as mock
from command_line_game_displayer import CommandLineGameDisplayer


class TestCommandLineGameDisplayer(unittest.TestCase):

    @mock.patch('CommandLineGameDisplayer.get_input', return_value="alex")
    def test_players_prompt(self):
        game_displayer = CommandLineGameDisplayer()
        players = game_displayer.prompt_for_players()
        self.assertEqual(players, ["alex", "bob"])



if __name__ == "__main__":
    unittest.main()
