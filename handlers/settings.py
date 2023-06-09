from aiogram.types import Message
from app import dp
from aiogram.dispatcher.filters import Text
from utilities.misc import rate_limit
from utilities.user_information import user_information
from keyboards.settings_keyboard import settings_keyboard

@rate_limit(limit=2)
@dp.message_handler(Text(equals='⚙️️ Настройки'))
async def settings(msg: Message):
    data = user_information(msg.from_user.id)
    await msg.answer(f"Ваша группа: {data['group_index']}\nВаша зачётка: {data['grade_book']}", reply_markup=settings_keyboard)