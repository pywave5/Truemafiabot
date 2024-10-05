from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
from aiogram.enums.parse_mode import ParseMode

from mafia.bot.filters.current_chat import CurrentChat

from mafia.bot.functions.game import MafiaManager

user = Router()
mafia = MafiaManager(players=[{}])

@user.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(f"Привет! я бот-ведущий игры Мафия!")

@user.message(CurrentChat(), Command("game"))
async def cmd_game(message: Message) -> None:
    await message.answer(f"{mafia.start_game()}",
                         parse_mode=ParseMode.HTML)
