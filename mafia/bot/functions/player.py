from dataclasses import dataclass
from mafia.bot.functions.roles import Role

@dataclass
class Player:
    user_id: int
    name: str
    role: Role = None
    is_alive: bool = True