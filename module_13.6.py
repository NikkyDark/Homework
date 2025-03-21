from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = 'Введите ваш токен:'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

key_start = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='/start')
button2 = KeyboardButton(text='info')
key_start.add(button1, button2)

key_gender = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Мужской', callback_data='5')
button4 = InlineKeyboardButton(text='Женский', callback_data="-161")
key_gender.add(button3)
key_gender.add(button4)

key_setting = InlineKeyboardMarkup(resize_keyboard=True)
button5 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button6 = InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
key_setting.add(button5)
key_setting.add(button6)

genders = 5
err_age = "Введите возраст, от 1 до 100 лет"
err_number = "Введите число!"


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    calories = State()


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    text = ("Для мужчин: (вес*10)+(рост*6.25)-(возраст*5)+5\n"
            "Для женщин: (вес*10)+(рост*6.25)-(возраст*5)-161\n")
    await call.message.answer(text)
    await call.answer()


@dp.message_handler(text="info")
async def get_info(message):
    text = ('Домашнее задание по теме "Инлайн клавиатуры".'
            '\nЦель: научиться создавать Inline клавиатуры и кнопки на них в Telegram-bot.'
            '\nЗадача "Ещё больше выбора":'
            '\nСтудент Бобачев Никита Дмитриевич.'
            '\nДата работы над заданием: 19.03.2025г.')
    await message.answer(text)


@dp.callback_query_handler(text=["5"])
@dp.callback_query_handler(text=["161"])
async def start_message(call):
    genders_ = float(call)
    await call.answer()
    await call.message.answer("Выберите опцию", reply_markup=key_setting)
    await call.answer()
    return genders_


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите возраст: ")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    counting = await state.get_data()
    rep_age = str(counting['age']).replace(",", ".")
    try:
        set_ages = float(rep_age)
        if set_ages <= 100:
            await state.update_data(age=set_ages)
            await message.answer('Введите свой рост (число):')
            await UserState.growth.set()
        else:
            await message.answer(err_age)
            return set_age()
    except ValueError:
        await message.answer(err_age)
        return set_age()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    counting = await state.get_data()
    rep_growth = str(counting['growth']).replace(",", ".")
    try:
        set_growths = float(rep_growth)
        await state.update_data(growth=set_growths)
        await message.answer('Введите свой вес (число):')
        await UserState.weight.set()
    except ValueError:
        await message.answer(err_number)
        return set_growth()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    counting = await state.get_data()
    rep_weight = str(counting['weight']).replace(",", ".")
    try:
        set_weights = float(rep_weight)
        set_growths = counting['growth']
        set_ages = counting['age']
        calories = float(10 * set_weights + 6.25 * set_growths - 5 * set_ages + genders)
        await message.answer(f'Ваша норма калорий: {round(calories, 2)}')
        await state.finish()
    except ValueError:
        await message.answer(err_number)
        return set_weight()


@dp.message_handler(commands="start")
async def start(message):
    text = 'Привет, я бот помогающий твоему здоровью!\nВыберите ваш пол:'
    await message.answer(text, reply_markup=key_gender)


@dp.message_handler(commands=['start'])
async def start(message):
    text = 'Привет, я бот помогающий твоему здоровью!\nВыберите ваш пол:'
    await message.answer(text, reply_markup=key_gender)


@dp.message_handler()
async def all_messages(message):
    await message.answer('Нажмите кнопку "start", или "info" чтобы начать общение.', reply_markup=key_start)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
