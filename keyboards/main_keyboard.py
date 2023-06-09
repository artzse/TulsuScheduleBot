from aiogram.types import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row('◀️ Вчера', '⏺️ Сегодня', '️▶️ Завтра').row('⏭️ На неделю').row('💯 Успеваемость').row('⚙️️ Настройки')