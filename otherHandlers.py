from aiogram.types import ContentType
import cars_db
from main import dp
import button
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Command


USER_ID = None


class FSMSearch(StatesGroup):
    search_st = State()


class FSMAuthorization(StatesGroup):
    password = State()


@dp.message_handler(Command('start'))
async def echo(message: types.Message):
    fullname = cars_db.search_tg_user_id(message.from_user.id)
    if fullname and not fullname[2]:
        await message.answer(f'Добро пожаловать {fullname[0].title()} {fullname[1].title()}', reply_markup=button.search)
    elif fullname and fullname[2] == 1:
        await message.answer(f"""Вы заблокированны 
Причина блокировки: {fullname[3]}""", reply_markup=button.ReplyKeyboardRemove())
    else:
        await message.answer('Вы не авторизованы', reply_markup=button.authorize)


@dp.message_handler(text='Авторизация')
async def search_fn(message: types.Message):
    await message.answer('Ведите пароль', reply_markup=button.ReplyKeyboardRemove())
    await FSMAuthorization.password.set()


@dp.message_handler(state=FSMAuthorization.password)
async def password_search(message: types.Message, state: FSMContext):
    global USER_ID
    USER_ID = cars_db.search_password(message.text)
    if USER_ID:
        await message.answer('Поделитесь контактом', reply_markup=button.tel_num)

    else:
        await message.answer('Неверный Пароль', reply_markup=button.authorize)
    await state.finish()


@dp.message_handler(content_types=ContentType.CONTACT)
async def password_search(message: types.Message):
    phone_number = message.contact.phone_number
    if message.contact:
        cars_db.add_user_id(message.from_user.id, phone_number, USER_ID)
        await message.answer('Вы успешно авторизованы', reply_markup=button.search)


@dp.message_handler(text='Поиск 🔍')
async def search_fn(message: types.Message):
    await message.answer('Ведите Имя или Номер Автомобиля', reply_markup=button.ReplyKeyboardRemove())
    await FSMSearch.search_st.set()


@dp.message_handler(state=FSMSearch.search_st)
async def search_fn_state(message: types.Message, state: FSMContext):
    result = cars_db.search_employee(message.text)
    print(result)
    if result:
        for i in result:
            await message.answer(f"""Имя: {i[0]}
Фамилия: {i[1]}
Автомобиль: {i[2]}
Номер Автомобиля: {i[3]}
Цвет: {i[4]}
""", reply_markup=button.search)
    else:
        await message.answer(f'По вашему запросу "{message.text}" \nНичего не найдено', reply_markup=button.search)
    await state.finish()


@dp.message_handler(text='🔼')
@dp.message_handler(text='🔽')
@dp.message_handler(text='Посмотреть свободные места ✅')
async def change_places_fn(message: types.Message):
    free = 'Свободные места: '
    busy = 'Занятые места: '
    total = 'Общее кол. мест: '
    if message.text == '🔼':
        if cars_db.plus() == 0:
            await message.answer(f'🤬', reply_markup=button.search)
            await message.answer(f'Нет свободных мест!!!', reply_markup=button.search)
    elif message.text == '🔽':
        if cars_db.minus() == 0:
            await message.answer(f'😎', reply_markup=button.search)
            await message.answer(f'Нет авто на парковке', reply_markup=button.search)
    spaces = cars_db.all_spaces()
    free += str(spaces[2])
    busy += str(spaces[1])
    total += str(spaces[0])
    await message.answer(f'{free}\n{busy}\n{total}', reply_markup=button.search)
