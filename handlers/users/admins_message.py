# from aiogram import types
# from loader import dp
# from filters.AdminFilter import IsAdmin
# from filters.PrivateFilter import IsPrivate


# @dp.message_handler(IsPrivate(), IsAdmin())
# async def adm_sends_message(message: types.Message):
#     lst = list(message.text.split())
#     print(lst)
#     print(lst[0])
#     print(lst[1:])
#     print(message.text)
#     print(message.text[0])
#     print(message.text[1:])
#     await dp.bot.send_message(chat_id=lst[0], text=lst[1:])