from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Remove background✂️🖼"),
    ],
        [
            KeyboardButton(text="About❔")
    ],
        [
            KeyboardButton(text="Write to admin💬")
    ],
        ],
    resize_keyboard=True
)