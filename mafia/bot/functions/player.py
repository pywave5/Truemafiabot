from dataclasses import dataclass
from typing import Optional
from mafia.bot.functions.roles import Role

@dataclass
class Player:
    id: int
    name: str
    role: Optional[Role] = None
    is_alive: bool = True

    def kill(self) -> None:
        if self.is_alive:
            self.is_alive = False

    def revive(self) -> None:
        if not self.is_alive:
            self.is_alive = True

    @property
    def is_player_alive(self) -> bool:
        return self.is_alive

    def get_name(self) -> str:
        return self.name

    def get_role(self) -> dict:
        return {
            "role": self.role.name if self.role else None,
            "info": self.role.info if self.role else None,
        }
