from dataclasses import dataclass
from mafia.bot.functions.roles import Role

@dataclass
class Player:
    user_id: int
    role: Role = None
    is_alive: bool = True