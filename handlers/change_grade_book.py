from app import dp
from aiogram.dispatcher.filters import Text
from utilities.user_states import ChangeGradeBook
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from utilities.change_grade_book import change_grade_book
from aiogram.types import ReplyKeyboardRemove
from keyboards.main_keyboard import main_keyboard

@dp.message_handler(Text(equals='Изменить номер зачётки', ignore_case=True))
async def command_change_group_index(msg: Message):
    await msg.answer("Введите новый номер зачётки", reply_markup=ReplyKeyboardRemove())
    await ChangeGradeBook.new_grade_book.set()

@dp.message_handler(state=ChangeGradeBook.new_grade_book)
async def commit_group_index(msg: Message, state: FSMContext):
    change_grade_book(msg.from_user.id, msg.text)
    await msg.answer('Новый номер зачётки успешно установлен!', reply_markup=main_keyboard)
    await state.finish()