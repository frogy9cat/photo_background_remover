from aiogram import Bot, types
from aiogram.dispatcher.filters.builtin import Text
from keyboards.inline import InlineAbout
from loader import dp
from data.config import BOT_TOKEN
from utils.removeBG import rasm_remove 
from utils.about_bot_pic import bot_pic
from filters.PrivateFilter import IsPrivate


@dp.message_handler(IsPrivate(), Text("Remove background✂️🖼"))
async def remove_command(message: types.Message):

    await message.reply("Пожалуйста, отправьте мне фото👀")


@dp.message_handler(IsPrivate(), Text("About❔"))
async def about_command(message: types.Message):
    await message.answer_photo(bot_pic(), caption="Бот для удаления фона в фотографии.\n\nПринцип работы очень прост: Вы отправляете фото боту, а он вам вернет её в формате .png без заднего фона.\nПримечание: отправляйте фото с хорошим контрастом тонов. Это повысит качество обработки фото.\n\nТакже у бота появилась новая функция: вы отправляете ему ссылку на какое-либо фото из браузера, а он вернет вам само фото.\nБота создал: @frogy_cat\n\nСпасибо, чтоы пользуетесь нашим ботом!", reply_markup=InlineAbout.Sharing)


bot = Bot(token=BOT_TOKEN)

@dp.message_handler(IsPrivate(), content_types=types.ContentTypes.PHOTO)
async def wikipedia_bot(message: types.Message):
    await message.answer(f"Идёт обработка фото...")
    photo_id = message.photo[-1].file_id
    photo_info = await bot.get_file(photo_id)
    file_path = photo_info["file_path"]
    photos_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
    rasm = rasm_remove(photos_url)
    if rasm:
        await message.reply_photo(rasm,caption='Version with white background⬆️')
        await message.reply_document(('request.png',rasm),caption='PNG format')

    await message.answer("Removing background completed!✅")