import os
import asyncio

from aiogram import Bot, Dispatcher
from bot.handlers.user import user

async def main() -> None:
    bot = Bot(token=os.getenv("TESTS_TOKEN_API"))
    dp = Dispatcher()
    dp.include_router(user)

    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")