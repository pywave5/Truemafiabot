from aiogram.fsm.state import StatesGroup, State

class GameState(StatesGroup):
    vote_to_game = State()
    game_started = State()
    game_over = State()