from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Sharing = InlineKeyboardMarkup(
inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш канал", url="https://t.me/python_b_end"),
    ],
        [
            InlineKeyboardButton(text="Поделиться ботом", switch_inline_query="\n\nДоброго времени суток!🙃\nЭто бот для удаления фотографии.🌚")
    ],
],
)