from keyboards.default import RBGbotKeyboard
from states.Feetback import FtBack
from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from data.config import ADMINS
from filters.PrivateFilter import IsPrivate


@dp.message_handler(IsPrivate(), Text("Write to admin💬"))
async def bot_text_to_admin(message: types.Message):
    await message.answer(f"Пожалуйста, введите своё сообщение...")
    await FtBack.ft_text.set()

@dp.message_handler(IsPrivate(), state = FtBack.ft_text)
async def text_to_admin(message: types.Message, state: FSMContext):
    await state.update_data({"ft_text" : str(message.text)})
    await message.answer("Ваше сообщение принято! Спасибо, что помогаете нам и даёте развиваться!", reply_markup=RBGbotKeyboard.Menu)
    
    data = await state.get_data()
    ft_text = data.get("ft_text")
    await state.finish()
    for admin in ADMINS:
        await dp.bot.send_message(admin, f"Сообщение от @{message.from_user.username} ({message.from_user.id}):\n\n\"{ft_text}\" ")
