from aiogram.types import Message
from app import dp
from utilities.schedule_parser import schedule_parser
from aiogram.dispatcher.filters import Text
from datetime import datetime, timedelta
from utilities.misc import rate_limit

@rate_limit(limit=2)
@dp.message_handler(Text(equals='◀️ Вчера'))
async def yesterday(msg: Message):
    await msg.answer(text=schedule_parser((msg.from_user.id), (datetime.today() - timedelta(days=1)).strftime('%d.%m.%Y')), parse_mode='Markdown')

@rate_limit(limit=2)
@dp.message_handler(Text(equals='⏺️ Сегодня'))
async def today(msg: Message):
    await msg.answer(text=schedule_parser((msg.from_user.id), datetime.today().strftime('%d.%m.%Y')), parse_mode='Markdown')

@rate_limit(limit=2)
@dp.message_handler(Text(equals='️▶️ Завтра'))
async def tomorrow(msg: Message):
    await msg.answer(text=schedule_parser((msg.from_user.id), (datetime.today() + timedelta(days=1)).strftime('%d.%m.%Y')), parse_mode='Markdown')

@rate_limit(limit=2)
@dp.message_handler(Text(equals='⏭️ На неделю'))
async def week(msg: Message):
    for i in range(6):
        await msg.answer(text=schedule_parser((msg.from_user.id), (datetime.today() + timedelta(days=i)).strftime('%d.%m.%Y')), parse_mode='Markdown')