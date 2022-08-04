from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from utils.about_bot_pic import bot_pic
from keyboards.inline import InlineAbout
from filters.PrivateFilter import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    await message.answer_photo(bot_pic(), caption="Бот для удаления фона в фотографии.\n\nПринцип работы очень прост: Вы отправляете фото боту, а он вам вернет её в формате .png без заднего фона.\nПримечание: отправляйте фото с хорошим контрастом тонов. Это повысит качество обработки фото.\n\nТакже у бота появилась новая функция: вы отправляете ему ссылку на какое-либо фото из браузера, а он вернет вам само фото.\n\nБота создал: @frogy_cat\n\nСпасибо, чтоы пользуетесь нашим ботом!", reply_markup=InlineAbout.Sharing)
