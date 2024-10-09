import json
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Role:
    name: str
    alignment: str
    info: str
    has_night_action: bool
    has_day_action: bool
    number_of_targets: int
    priority: int
    sends_mafia_kill: bool
    can_self_target: bool
    shots: int
    max_count: int

    @staticmethod
    def load_data():
        file_path = Path(__file__).parent / "data" / "role.json"
        with open(file_path, "r", encoding="UTF-8") as file:
            return json.load(file)

class Mafia(Role):
    def __init__(self):
        data = self.load_data()["mafia"]
        super().__init__(
            name=data["name"],
            alignment=data["alignment"],
            info=data["info"],
            has_night_action=data["has_night_action"],
            has_day_action=data["has_day_action"],
            number_of_targets=data["number_of_targets"],
            priority=data["priority"],
            sends_mafia_kill=data["sends_mafia_kill"],
            can_self_target=data["can_self_target"],
            shots=data["shots"],
            max_count=data["max_count"]
        )