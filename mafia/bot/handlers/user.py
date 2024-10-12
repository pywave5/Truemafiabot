from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext

from mafia.bot.filters.current_chat import CurrentChat
from mafia.bot.states.game_states import GameState
from mafia.bot.functions.game import MafiaManager

user = Router()
mafia = MafiaManager()

@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Привет! я бот-ведущий игры Мафия!")
    await state.clear()

@user.message(CurrentChat(), Command("game"))
async def cmd_game(message: Message, state: FSMContext) -> None:
    mafia.append_player(message.from_user.id, message.from_user.first_name)
    mafia.append_player(1, "player_1")
    mafia.append_player(2, "player_2")
    mafia.append_player(3, "player_3")

    await message.answer(f"{mafia.start_game()}",
                         parse_mode=ParseMode.HTML)

    await message.answer(f"{mafia.format_players_list()}")

    user_role = mafia.get_player_role(message.from_user.id)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=f"Ваша роль - <b>{user_role['role']}</b>\n"
             f"<blockquote>{user_role['info']}</blockquote>",
        parse_mode=ParseMode.HTML
    )
    await state.set_state(GameState.game_started)

@user.message(CurrentChat(), Command("quit"))
async def cmd_quit(message: Message, state: FSMContext) -> None:
    await message.answer("Игра окончена!")
    mafia.end_game()
    await state.clear()