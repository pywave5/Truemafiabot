from dataclasses import dataclass
from player import Player

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