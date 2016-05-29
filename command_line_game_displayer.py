class CommandLineGameDisplayer(object):

    def __init__(self):
        pass

    def get_input(text):
        """Wrapper for input to allow patching for unit tests"""
        return input(text)

    def prompt_for_players(self):
        pass
