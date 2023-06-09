from aiogram.types import ReplyKeyboardMarkup

settings_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row('Изменить номер группы').row('Изменить номер зачётки').row('Назад')