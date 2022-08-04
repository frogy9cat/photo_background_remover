import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.PrivateFilter import IsPrivate
from keyboards.default import RBGbotKeyboard
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(f"Привет {message.from_user.full_name}!", reply_markup=RBGbotKeyboard.Menu)
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} был добавлен в базу данных.\nЧисло пользователей в боте: {count}."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

