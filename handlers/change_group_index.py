from app import dp
from aiogram.dispatcher.filters import Text
from utilities.user_states import ChangeGroupIndex
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from utilities.change_group_index import change_group_index
from aiogram.types import ReplyKeyboardRemove
from keyboards.main_keyboard import main_keyboard

@dp.message_handler(Text(equals='Изменить номер группы'))
async def command_change_group_index(msg: Message):
    await msg.answer("Введите новый номер группы", reply_markup=ReplyKeyboardRemove())
    await ChangeGroupIndex.new_group_index.set()

@dp.message_handler(state=ChangeGroupIndex.new_group_index)
async def commit_group_index(msg: Message, state: FSMContext):
    change_group_index(msg.from_user.id, msg.text)
    await msg.answer('Новый номер группы успешно установлен!', reply_markup=main_keyboard)
    await state.finish()