#!/usr/bin/env python

from player import Player

class Game():

    def __init__(self, number_of_players):
        self.players = range(number_of_players)

    def get_players(self):
        return self.players


if __name__ == "__main__":
    game()
