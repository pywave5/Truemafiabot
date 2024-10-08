from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
from aiogram.enums.parse_mode import ParseMode

from mafia.bot.filters.current_chat import CurrentChat

from mafia.bot.functions.game import MafiaManager

user = Router()
mafia = MafiaManager()

@user.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(f"Привет! я бот-ведущий игры Мафия!")

@user.message(CurrentChat(), Command("game"))
async def cmd_game(message: Message) -> None:
    mafia.append_player(message.from_user.id)
    mafia.append_player(1)
    mafia.append_player(2)
    mafia.append_player(3)

    await message.answer(f"{mafia.start_game()}",
                         parse_mode=ParseMode.HTML)

    user_role = mafia.get_player_role(message.from_user.id)

    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=f"Ваша роль - <b>{user_role['role']}</b>\n"
             f"<blockquote>{user_role['info']}</blockquote>",
        parse_mode=ParseMode.HTML
    )