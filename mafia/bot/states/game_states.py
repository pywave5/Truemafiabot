from aiogram.fsm.state import StatesGroup, State

class GameState(StatesGroup):
    game_started = State()
    game_over = State()