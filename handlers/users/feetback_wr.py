from keyboards.default import RBGbotKeyboard
from states.Feetback import FtBack
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.dispatcher.filters.builtin import Text, Command
from aiogram import types
from data.config import ADMINS
from filters.PrivateFilter import IsPrivate

#....................................FEETBACK TO USER..................................................................................

@dp.message_handler(IsPrivate(), Text("Написать разработчикам💬"))
async def bot_text_to_admin(message: types.Message):
    await message.answer(f"Пожалуйста, введите своё сообщение...")
    await FtBack.ft_text.set()

@dp.message_handler(IsPrivate(), state = FtBack.ft_text)
async def text_to_admin(message: types.Message, state: FSMContext):
    await state.update_data({"ft_text" : str(message.text)})
    await message.answer("Ваше сообщение принято. Спасибо, что помогаете нам и даёте развиваться!", reply_markup=RBGbotKeyboard.Additional)
    
    data = await state.get_data()
    ft_text = data.get("ft_text")
    await state.finish()
    for admin in ADMINS:
        await dp.bot.send_message(admin, f"Сообщение от @{message.from_user.username} ({message.from_user.id}):\n\n\"{ft_text}\" ")
#________________________________________________________________________________________________________________________________________





#......................................ANNWER GO FEETBACK................................................
@dp.message_handler(IsPrivate(), Command('touser'), chat_id = ADMINS)
async def bot_cho(message: types.Message, state: FSMContext):
    await message.answer('Сообщение пользователю...')
    
    await state.set_state("touser")

@dp.message_handler(state="touser")
async def bt_echo(message: types.Message, state: FSMContext):
    await state.finish()
    text= message.text.split()
    id=int(text[0])

    await bot.send_message(chat_id=id,text=message.text[10:])
#_________________________________________________________________________________________________________