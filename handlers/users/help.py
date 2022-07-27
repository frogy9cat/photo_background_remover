from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.default import RBGbotKeyboard

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "Для подробной информации нажмите на \"About❔\""
    await message.answer(text, reply_markup=RBGbotKeyboard.Menu)
