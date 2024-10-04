class MafiaManager:
    def __init__(self,
                 players: dict,
                 time: str):
        self._players = players
        self._time = time

    def start_game(self):
        return len(self._players) > 4

    def end_game(self) -> None:
        return self._players.clear()

    def append_player(self, user_id: int, role: str) -> None:
        self._players[user_id] = {"is_alive": True, "role": role}

    def remove_player(self, user_id: int) -> None:
        self._players.pop(user_id, None)

    def kill_player(self, user_id: int) -> str:
        if user_id in self._players:
            self._players[user_id]["is_alive"] = False
            return f"{user_id} - был убит."