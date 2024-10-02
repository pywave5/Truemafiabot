class Mafia:
    def __init__(self,
                 players: list,
                 time: str):
        self._players = players
        self._time = time


    def start_game(self) -> bool:
<<<<<<<<< Temporary merge branch 1
        return len(self._players) > 4
=========
        return len(self._players) > 4

    def end_game(self) -> None:
        return self._players.clear()
