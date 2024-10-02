class Mafia:
    def __init__(self,
                 players: list,
                 time: str):
        self._players = players
        self._time = time

    def start_game(self):
        return len(self._players) > 4