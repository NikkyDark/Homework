from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = 'Введите ваш токен:'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Calories')
async def start_calculation(message: types.Message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def get_growth(message: types.Message, state: UserState):
    async with state.proxy() as data:
        data['age'] = message.text
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: UserState):
    async with state.proxy() as data:
        data['growth'] = message.text
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


if __name__ == '__main__':
    executor.start_polling(dp)
