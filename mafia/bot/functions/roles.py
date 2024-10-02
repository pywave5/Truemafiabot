import random

class Role:
    def __init__(self,
                 name: str,
                 alignment: str,
                 info: str,
                 has_night_action: bool,
                 has_day_action: bool,
                 number_of_targets: int,
                 priority: int,
                 sends_mafia_kill: bool,
                 can_self_target: bool,
                 shots: int):
        self.name = name
        self.alignment = alignment
        self.info = info
        self.has_night_action = has_night_action
        self.has_day_action = has_day_action
        self.number_of_targets = number_of_targets
        self.priority = priority
        self.sends_mafia_kill = sends_mafia_kill
        self.can_self_target = can_self_target
        self.shots = shots
        self.is_alive = True

    def kill(self, user_id: int):
        self.is_alive = False
        return f"{user_id} - был убит."