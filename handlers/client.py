from aiogram import types
from create_bot import bot,Dispatcher

#@dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Я — бот Relax Weekend в ПГНИУ!\nЯ расскажу тебе о мероприятии и запишу на мастер-классы.\nЧем могу помочь? :)')

#@dp.message_handler(commands=['write'])
async def WiteMK(message : types.Message):
    MK=[]
    MK.append("то")
    MK.append("сё")
    MK.append("пятое")
    MK.append("десятое")
    await bot.send_message(message.from_user.id,MK)

def registration_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])
    dp.register_message_handler(WiteMK, commands=['write'])
