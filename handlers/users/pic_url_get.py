from aiogram import types
from loader import dp
from utils.getting_picture import get_picture
from filters.PrivateFilter import IsPrivate


@dp.message_handler(IsPrivate())
async def from_url_get_pic(message: types.Message):
    await message.answer_photo(photo=get_picture(str(message.text)))

        