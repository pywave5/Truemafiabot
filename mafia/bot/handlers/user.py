from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
from aiogram.fsm.context import FSMContext

from mafia.bot.filters.current_chat import CurrentChat
from mafia.bot.states.game_states import GameState
from mafia.bot.functions.game import MafiaManager
from mafia.bot.keyboards.game import KeyboardsControl

user = Router()
mafia = MafiaManager()
keyboards_control = KeyboardsControl()

@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Привет! я бот-ведущий игры Мафия!")
    await state.clear()

@user.message(CurrentChat(), Command("game"))
async def cmd_game(message: Message, state: FSMContext) -> None:
    await state.set_state(GameState.vote_to_game)
    await message.reply(text=mafia.data["vote_to_game"],
                        reply_markup=await keyboards_control.create_inline_keyboard(
                            text=mafia.data["game_join"],
                            callback_data=None,
                            url="https://google.com"
                        ))

@user.message(CurrentChat(), Command("quit"))
async def cmd_quit(message: Message, state: FSMContext) -> None:
    await message.answer("Игра окончена!")
    mafia.end_game()
    await state.clear()