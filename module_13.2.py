from aiogram import Bot, Dispatcher, executor, types

TOKEN = Youre token

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Обработчик команды /start."""
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message: types.Message):
    """Обработчик любых сообщений не являющихся командами."""
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp)
