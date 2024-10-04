class MafiaManager:
    def __init__(self, players: dict):
        self._players = players
        self._time: dict = {0: "Ночь", 1: "День"}

    def start_game(self) -> str:
        if len(self._players) > 4:
            return f"Игра начинается..."
        else:
            return f"<b>Игра не может начаться если игроков меньше 4</b>"

    def end_game(self):
        return self._players.clear()

    def append_player(self, user_id: int, role: str) -> None:
        self._players[user_id] = {"is_alive": True, "role": role}

    def remove_player(self, user_id: int) -> None:
        self._players.pop(user_id, None)

    def kill_player(self, user_id: int) -> str:
        if user_id in self._players and self._players[user_id]["is_alive"]:
            self._players[user_id]["is_alive"] = False
            return f"{user_id} - был убит."
        else:
            return f"{user_id} и так мертв."

    def revive_player(self, user_id: int) -> str:
        if user_id in self._players and not self._players[user_id]["is_alive"]:
            self._players[user_id]["is_alive"] = True
            return f"{user_id} - возродился!"
        else:
            return f"{user_id} еще не умер :)"

    def get_gametime(self) -> str:
        return f"Игровое время - {self._time}"

    def set_time(self) -> str:
        current_time = 0 if self._time[0] else 1
        new_time = (current_time + 1) % 2
        return f"Время суток установлено на - {self._time[new_time]}"