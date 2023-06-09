from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from environs import Env
from sqlite3 import connect


###### Чтение .env
env = Env()
env.read_env('./.env')
BOT_TOKEN = env('BOT_TOKEN')

##### Создание переменных бота
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

##### Создание базы данных
con = connect('./data/db.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS "users"("id" INTEGER NOT NULL UNIQUE, "username" TEXT, "first_name" TEXT, "group_index" TEXT, "grade_book" TEXT, PRIMARY KEY("id"));')
con.commit()
con.close()

# Подключение middleware
import middlewares
middlewares.setup(dp)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)