import asyncio
from data.config import ADMINS
from filters.PrivateFilter import IsPrivate
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot



@dp.message_handler(Command('count'), chat_id = ADMINS)
async def bot_count_users(message: types.Message):
    count = db.count_users()[0]
    await message.answer(f"Пользователей бота: {count}")





@dp.message_handler(IsPrivate(), Command("allusers"), chat_id = ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    allusers=''
    for i, user in enumerate(users):
        allusers+=f"{i+1}.{user[1]} ({user[0]})\n"
    await message.answer(allusers)




#.........................DATA BASE DELETE....................................
@dp.message_handler(IsPrivate(), Command("DeleteDataBase"), chat_id = ADMINS)
async def bot_delete_data_base(message: types.Message, state: FSMContext):
    await message.answer(f"Пожалуйста, введите пароль создателя...")
    await state.set_state("allowing for DDB")


@dp.message_handler(state = "allowing for DDB")
async def deleting_accepted(message: types.Message, state: FSMContext):
    state.finish()
    if message.text == "та самая":
        db.delete_users()
        await message.answer("new start?)")
#_______________________________________________________________________________





@dp.message_handler(IsPrivate(), Command("commands"), chat_id = ADMINS)
async def bot_commands_for_admins(message: types.Message):
    text = "/count - the number of all users;\n/allusers - show all users and ids;\n/touser - send message to user."

    await message.answer(text)






        
@dp.message_handler(IsPrivate(), text="/advert")
async def send_ad_command(message: types.Message, state: FSMContext):
    await message.answer("Отправьте рекламу...")
    await state.set_state("advertisement")


@dp.message_handler(state = "advertisement", content_types=types.ContentType.ANY)
async def sending_advert(message: types.Message, state: FSMContext):
    state.finish()
    users = db.select_all_users()
    count = db.count_users()[0]
    for user in users:
        user_id = user[0]
    await bot.copy_message(user_id, message.chat.id, message.message_id)
    await message.answer(f"Реклама была отправлена {count} пользователям.")