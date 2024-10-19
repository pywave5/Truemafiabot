from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class KeyboardsControl:
    @classmethod
    async def create_inline_keyboard(cls,
                                     text: str,
                                     callback_data: str | None,
                                     url: str | None
                                     ) -> InlineKeyboardMarkup:
        if not callback_data and not url:
            raise ValueError("Either 'callback_data' or 'url' must be provided")

        ikb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=text,
                                  callback_data=callback_data,
                                  url=url)]
        ])

        return ikb