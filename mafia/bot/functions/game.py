import json
from pathlib import Path

class MafiaManager:
    def __init__(self, players: list[dict] = None):
        self._players = players if players is not None else []
        self._time: dict = {0: "Ночь", 1: "День"}

        file_path = Path(__file__).parent / "dicts" / "game.json"

        with open(file_path, "r", encoding="UTF-8") as file:
            self.data = json.load(file)

    def start_game(self) -> str:
        if len(self._players) > 4:
            return self.data["start_game"]
        else:
            return self.data["not_enough_players"]

    def end_game(self):
        return self._players.clear()

    def append_player(self, user_id: int, role: str) -> None:
        self._players.append({"user_id": user_id, "is_alive": True, "role": role})

    def remove_player(self, user_id: int) -> None:
        self._players.pop(user_id)

    def kill_player(self, user_id: int) -> str:
        if user_id in self._players and self._players[user_id]["is_alive"]:
            self._players[user_id]["is_alive"] = False
            return self.data["player_killed"].format(user_id=user_id)
        else:
            return self.data["and_so_dead"].format(user_id=user_id)

    def revive_player(self, user_id: int) -> str:
        if user_id in self._players and not self._players[user_id]["is_alive"]:
            self._players[user_id]["is_alive"] = True
            return self.data["player_revived"].format(user_id=user_id)
        else:
            return self.data["and_so_alive"].format(user_id=user_id)

    def get_gametime(self) -> str:
        current_time = 0 if self._time[0] else 1
        return self.data["game_time"].format(time=self._time[current_time])

    def set_time(self) -> str:
        current_time = 0 if self._time[0] else 1
        new_time = (current_time + 1) % 2
        return self.data["set_time"].format(time=self._time[new_time])

    def get_player_role(self, user_id: int) -> str:
        for player in self._players:
            if player["user_id"] == user_id:
                return player["role"]
        return self.data["role_not_found"]