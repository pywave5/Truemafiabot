from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
from aiogram.utils.deep_linking import create_start_link
from aiogram.fsm.context import FSMContext

from mafia.bot.filters.current_chat import CurrentChat
from mafia.bot.states.game_states import GameState
from mafia.bot.functions.game import MafiaManager
from mafia.bot.keyboards.game import KeyboardsControl

user = Router()
mafia = MafiaManager()
keyboards_control = KeyboardsControl()

@user.message(CommandStart(deep_link=True))
async def cmd_start(message: Message, state: FSMContext, bot) -> None:
    link = await create_start_link(bot, "game_join", encode=True)
    print(link) # https://t.me/rtmtrtortrbot?start=Z2FtZV9qb2lu
    await message.answer(f"Привет! я бот-ведущий игры Мафия!")
    await state.clear()

@user.message(CurrentChat(), Command("game"))
async def cmd_game(message: Message, state: FSMContext, bot) -> None:
    await state.set_state(GameState.vote_to_game)
    await message.reply(text=mafia.data["vote_to_game"],
                        reply_markup=await keyboards_control.create_inline_keyboard(
                            text=mafia.data["game_join"],
                            callback_data=None,
                            url="https://t.me/rtmtrtortrbot?start=game_join"
                        ))

@user.message(CurrentChat(), Command("quit"))
async def cmd_quit(message: Message, state: FSMContext) -> None:
    await message.answer("Игра окончена!")
    mafia.end_game()
    await state.clear()