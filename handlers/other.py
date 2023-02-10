from aiogram import types
from create_bot import dp,Dispatcher

#@dp.message_handler()
async def echo_send(message : types.Message):
    await message.reply("Are you gay?")

def registration_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
