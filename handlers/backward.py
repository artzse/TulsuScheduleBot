from app import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from keyboards.main_keyboard import main_keyboard

@dp.message_handler(Text(equals='Назад'))
async def command_backward(msg: Message):
    text = 'Возвращаемся в главное меню...'
    await msg.answer(text, reply_markup=main_keyboard)