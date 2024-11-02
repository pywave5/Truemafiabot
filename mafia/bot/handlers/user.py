from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command, CommandObject
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
async def cmd_join_game(message: Message, state: FSMContext, command: CommandObject) -> None:
    if not mafia.player_in_game(message.from_user.id):
        mafia.append_player(user_id=message.from_user.id,
                            name=message.from_user.first_name)
        await message.answer(f"Ты успешно присоединился к игре!")
    else:
        await message.answer(f"Ты уже в игре понимаешь? в игре :)")

@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Привет! я бот-ведущий игры Мафия!")
    await state.clear()

@user.message(CurrentChat(), Command("game"))
async def cmd_game(message: Message, state: FSMContext, bot) -> None:
    await state.set_state(GameState.vote_to_game)
    link = await create_start_link(bot, "game_join", encode=True)
    await message.reply(text=mafia.data["vote_to_game"],
                        reply_markup=await keyboards_control.create_inline_keyboard(
                            text=mafia.data["game_join"],
                            callback_data=None,
                            url=link
                        ))

@user.message(CurrentChat(), Command("quit"))
async def cmd_quit(message: Message, state: FSMContext) -> None:
    await message.answer("Игра окончена!")
    mafia.end_game()
    await state.clear()