from aiogram import Bot, types
from aiogram.dispatcher.filters.builtin import Text
from keyboards.default import RBGbotKeyboard
from keyboards.inline import InlineAbout
from loader import dp
from data.config import BOT_TOKEN
from utils.removeBG import bg_remove
from utils.about_bot_pic import bot_pic
from filters.PrivateFilter import IsPrivate


@dp.message_handler(IsPrivate(), Text("Удалить фон✂️🖼"))
async def remove_command(message: types.Message):

    await message.reply("Пожалуйста, отправьте мне фото👀")


@dp.message_handler(IsPrivate(), Text("Информация о боте❔"))
async def about_command(message: types.Message):
    await message.answer_photo(bot_pic(), caption="Бот для удаления фона в фотографии.\n\nПринцип работы очень прост: Вы отправляете фото боту, а он вам вернет её в формате .png без заднего фона.\nПримечание: отправляйте фото с хорошим контрастом тонов. Это повысит качество обработки фото.\n\nТакже у бота появилась новая функция: вы отправляете ему ссылку на какое-либо фото из браузера, а он вернет вам само фото.\n\nБота создал: @frogy_cat\n\nСпасибо, чтоы пользуетесь нашим ботом!", reply_markup=InlineAbout.Sharing)


bot = Bot(token=BOT_TOKEN)

@dp.message_handler(IsPrivate(), content_types=types.ContentTypes.PHOTO)
async def deleting_bg_process(message: types.Message):
    await message.answer(f"Идёт обработка фото...")
    photo_id = message.photo[-1].file_id
    photo_info = await bot.get_file(photo_id)
    file_path = photo_info["file_path"]
    photos_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
    pic = bg_remove(photos_url)
    if pic:
        await message.reply_photo(pic,caption='Version with white background⬆️')
        await message.reply_document(('request.png',pic),caption='PNG format')

    await message.answer("Removing background completed!✅", reply_markup=RBGbotKeyboard.Menu)




@dp.message_handler(IsPrivate(), Text("Назад🔙"))
async def back_command(message: types.Message):
    await message.answer(text="Вы в главном меню.", reply_markup=RBGbotKeyboard.Menu)


@dp.message_handler(IsPrivate(), Text("Дополнительноℹ️"))
async def additional_info_button(message: types.Message):
    await message.answer(text= "Вы в разделе \"Дополнительноℹ️\".",reply_markup=RBGbotKeyboard.Additional)