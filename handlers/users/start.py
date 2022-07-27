from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.PrivateFilter import IsPrivate
from keyboards.default import RBGbotKeyboard
from loader import dp


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}😃!", reply_markup=RBGbotKeyboard.Menu)
