from aiogram.types import Message
from app import dp
from utilities.registration import registration
from utilities.user_information import user_information
from keyboards.main_keyboard import main_keyboard
from utilities.user_states import Registration
from aiogram.dispatcher import FSMContext
from utilities.misc import rate_limit

@rate_limit(limit=1)
@dp.message_handler(commands=['start'])
async def command_start(msg: Message):
    if user_information(msg.from_user.id) == 0:
        await msg.answer(f'Добро пожаловать, {msg.from_user.first_name}!\n\nЭтот бот создан для облегеченного и ускоренного доступа к расписанию.\n\nВозможны баги и недоработки, осторожно :)\n\nСоздатель: @artzse', parse_mode='Markdown')
        await msg.answer('Напишите номер своей группы.')
        await Registration.group_index.set()
    else:
        data = user_information(msg.from_user.id)
        text = f"С возвращением, {msg.from_user.first_name}!\n\nНомер группы: {data['group_index']}\nНомер зачётки: {data['grade_book']}\n\nСоздатель: @artzse"
        await msg.answer(text, reply_markup=main_keyboard)

@rate_limit(limit=1)
@dp.message_handler(state=Registration.group_index)
async def getting_group_index(msg: Message, state: FSMContext):
    await state.update_data(group_index = msg.text)
    await msg.answer('Отлично!\nТеперь напишите номер вашей зачётки.')
    await Registration.next()

@rate_limit(limit=1)
@dp.message_handler(state=Registration.grade_book)
async def getting_grade_book(msg: Message, state: FSMContext):
    await state.update_data(grade_book = msg.text)
    data = await state.get_data()
    registration(msg.from_user.id, msg.from_user.username, msg.from_user.first_name, data['group_index'], data['grade_book'])
    await msg.answer('Вы успешно зарегистрировались!', reply_markup=main_keyboard)
    await state.finish()