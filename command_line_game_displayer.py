ORDINALS = ["first", "second", "third"]
MIN_PLAYERS = 2

def get_input(text):
    """Wrapper for input to allow patching for unit tests"""
    return input(text)

class CommandLineGameDisplayer(object):

    def __init__(self):
        self.players = []

    def prompt_for_players(self):
        for i in range(len(ORDINALS)):
            if len(self.players) == MIN_PLAYERS:
                self._another_player_prompt()
            self._prompt_for_nth_player()
        return self.players

    def _another_player_prompt(self):
        another_player_prompt = "Would you like to add a third player?"
        get_input(another_player_prompt)

    def _prompt_for_nth_player(self):
        name_prompt = ("Please enter the name of the {ordinal} player: "
            .format(ordinal=ORDINALS[len(self.players)]))
        self.players.append(get_input(name_prompt))
