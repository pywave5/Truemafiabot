import json
import random
from pathlib import Path

from mafia.bot.functions.player import Player
from mafia.bot.functions.roles import Role


class MafiaManager:
    def __init__(self, players: list[Player] = None):
        self._players = players if players is not None else []
        self._time: str = "Ночь"

        file_path = Path(__file__).parent / "data" / "game.json"
        with open(file_path, "r", encoding="UTF-8") as file:
            self.data = json.load(file)

        self.roles = self.load_roles()

    def load_roles(self):
        file_path = Path(__file__).parent / "data" / "role.json"
        with open(file_path, "r", encoding="UTF-8") as file:
            return json.load(file)

    def start_game(self) -> str:
        if len(self._players) >= 4:
            self.__set_user_roles()
            return self.data["start_game"]
        else:
            return self.data["not_enough_players"]

    def end_game(self):
        self._players.clear()

    def append_player(self, user_id: int, name: str) -> None:
        self._players.append(Player(user_id=user_id, name=name))

    def remove_player(self, user_id: int) -> None:
        self._players = [p for p in self._players if p.user_id != user_id]

    def kill_player(self, user_id: int) -> str:
        for player in self._players:
            if player.user_id == user_id and player.is_alive:
                player.is_alive = False
                return self.data["player_killed"].format(name=player.name)
            return self.data["and_so_dead"].format(name=player.name)

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

    def get_player_role(self, user_id: int) -> dict:
        for player in self._players:
            if player.user_id == user_id:
                return {
                    "role": player.role.name,
                    "info": player.role.info
                }

    def __set_user_roles(self) -> None:
        role_data = list(self.roles.values())
        for player in self._players:
            random_role_data = random.choice(role_data)
            player.role = Role(
                name=random_role_data["name"],
                alignment=random_role_data["alignment"],
                info=random_role_data["info"],
                has_night_action=random_role_data["has_night_action"],
                has_day_action=random_role_data["has_day_action"],
                number_of_targets=random_role_data["number_of_targets"],
                priority=random_role_data["priority"],
                sends_mafia_kill=random_role_data["sends_mafia_kill"],
                can_self_target=random_role_data["can_self_target"],
                shots=random_role_data["shots"],
                max_count=random_role_data["max_count"],
            )

    def format_players_list(self) -> str:
        result = []
        for idx, player in enumerate(self._players, start=1):
            result.append(f"{idx}. {player.name}")
        return "\n".join(result)

    def get_players(self) -> list:
        return self._players

    def player_in_game(self, user_id: int) -> bool:
        return any(player.user_id == user_id for player in self._players)