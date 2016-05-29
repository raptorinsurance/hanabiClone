#!/usr/bin/env python

import itertools
import command_line_game_displayer as displayer

class Game(object):

    def __init__(self, displayer):
        self.displayer = displayer
        self.players = displayer.prompt_for_players()
        self.start_game()

    def start_game(self):
        # TODO: max_calls currently only there to prevent inifinite loop,
        # replace with win condition tester
        max_calls = 10
        for player in itertools.islice(itertools.cycle(self.players), 0, max_calls):
            self.displayer.prompt_for_action(player)


if __name__ == "__main__":
    displayer = displayer.Displayer()
    game = Game(displayer)
