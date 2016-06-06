MIN_PLAYERS = 2
MAX_PLAYERS = 5
YES_VALUES = ["yes", "y"]
NO_VALUES = ["no", "n"]

def get_input(text):
    """Wrapper for input to allow patching for unit tests"""
    return input(text)

class CommandLineGameDisplayer(object):

    def __init__(self):
        self.players = []

    def prompt_for_players(self):
        for i in range(MAX_PLAYERS):
            next_player_index = len(self.players) + 1
            if next_player_index > MIN_PLAYERS:
                add_another_player = self._add_nth_player_prompt(next_player_index)
                if not add_another_player:
                    break
            self._prompt_for_nth_player(next_player_index)
        return self.players

    def _add_nth_player_prompt(self, player_number):
        another_player_prompt = ("Would you like to add player {player_number}?"
            .format(player_number=player_number))
        response = get_input(another_player_prompt)
        if response in YES_VALUES:
            return True
        return False

    def _prompt_for_nth_player(self, player_number):
        name_prompt = ("Please enter the name of player {player_number}: "
            .format(player_number=player_number))
        self.players.append(get_input(name_prompt))

#TODO make max and min players configurable in init
