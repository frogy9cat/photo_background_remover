from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.default import RBGbotKeyboard
from filters.PrivateFilter import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = "Для подробной информации нажмите на \"About❔\""
    await message.answer(text, reply_markup=RBGbotKeyboard.Menu)
