from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
TOKEN = '5205719838:AAGw93tE1rpFgIQmJiBUTZGQE95DSgBp9uc'
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


if __name__ == '__main__':
	from otherHandlers import dp
	executor.start_polling(dp, skip_updates=True)
