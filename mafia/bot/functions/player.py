from dataclasses import dataclass
from roles import Role

@dataclass
class Player:
    user_id: int
    role: Role
    is_alive: bool = True