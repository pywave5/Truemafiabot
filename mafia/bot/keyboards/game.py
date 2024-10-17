from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class KeyboardsControl:
    async def create_inline_keyboard(self,
                                     text: str,
                                     callback_data: str | None,
                                     url: str | None
                                     ) -> InlineKeyboardMarkup:
        ikb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=text,
                                  callback_data=callback_data,
                                  url=url)]
        ])

        return ikb