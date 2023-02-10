from aiogram.utils import executor
from create_bot import dp

async def on_startup(_):
    print('Бот готов')

from handlers import client, admin, other

client.registration_handlers_client(dp)
#admin.registration_handlers_client(dp)
other.registration_handlers_other(dp)
executor.start_polling(dp,skip_updates=True,on_startup=on_startup)