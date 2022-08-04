from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Удалить фон✂️🖼"),
    ],

        [
            KeyboardButton(text="Дополнительноℹ️")
    ],
        ],
    resize_keyboard=True
)


Additional = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Информация о боте❔")
    ],
        [
            KeyboardButton(text="Написать разработчикам💬")
    ],
        [
            KeyboardButton(text="Назад🔙")
    ],
        ],
    resize_keyboard=True
)