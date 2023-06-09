from app import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from keyboards.term_keyboard import term_keyboard
from keyboards.main_keyboard import main_keyboard
from utilities.user_states import SelectTerm
from aiogram.dispatcher import FSMContext
from utilities.grade_book import get_grade_book

@dp.message_handler(Text(equals='💯 Успеваемость', ignore_case=True))
async def command_get_grade(msg: Message):
    await msg.answer('Выберете интересующий семестр', reply_markup=term_keyboard)
    await SelectTerm.select_term.set()

@dp.message_handler(state=SelectTerm.select_term)
async def get_grade(msg: Message, state: FSMContext):
    text = get_grade_book(msg.from_user.id, msg.text)
    await msg.answer(text, parse_mode='Markdown', reply_markup=main_keyboard)
    await state.finish()