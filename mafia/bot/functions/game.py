import json
import random
from pathlib import Path

from player import Player

class MafiaManager:
    def __init__(self, players: list[Player] = None):
        self._players = players if players is not None else []
        self._time: str = "Ночь"

        file_path = Path(__file__).parent / "dicts" / "game.json"
        with open(file_path, "r", encoding="UTF-8") as file:
            self.data = json.load(file)

    def start_game(self) -> str:
        if len(self._players) > 4:
            self.__set_user_roles()
            return self.data["start_game"]
        else:
            return self.data["not_enough_players"]

    def end_game(self):
        self._players.clear()

    def append_player(self, user_id: int) -> None:
        self._players.append(Player(user_id=user_id))

    def remove_player(self, user_id: int) -> None:
        self._players = [p for p in self._players if p.user_id != user_id]

    def kill_player(self, user_id: int) -> str:
        for player in self._players:
            if player.user_id == user_id and player.is_alive:
                player.is_alive = False
                return self.data["player_killed"].format(user_id=user_id)
        return self.data["and_so_dead"].format(user_id=user_id)

    def revive_player(self, user_id: int) -> str:
        for player in self._players:
            if player.user_id == user_id and not player.is_alive:
                player.is_alive = True
                return self.data["player_revived"].format(user_id=user_id)
        return self.data["and_so_alive"].format(user_id=user_id)

    def get_gametime(self) -> str:
        return self.data["game_time"].format(time=self._time)

    def set_time(self) -> str:
        self._time = "День" if self._time == "Ночь" else "Ночь"
        return self.data["set_time"].format(time=self._time)

    def get_player_role(self, user_id: int) -> str:
        for player in self._players:
            if player.user_id == user_id:
                return player.role
        return self.data["role_not_found"]

    def __set_user_roles(self) -> None:
        for player in self._players:
            random_role = random.choice(self.data["roles"])
            player.role = random_role
