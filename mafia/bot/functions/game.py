class Mafia:
    def __init__(self,
                 players: list,
                 time: str):
        self._players = players
        self._time = time


    def start_game(self) -> bool:
        return len(self._players) > 4
    def end_game(self) -> None:
        return self._players.clear()

    def append_player(self, user_id: int) -> None:
        return self._players.append(user_id)

    def remove_player(self, user_id: int) -> None:
        return self._players.pop(user_id)