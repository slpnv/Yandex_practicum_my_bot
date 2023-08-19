import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from background import keep_alive #импорт функции для поддержки работоспособности

# Вставьте ваш токен бота
TOKEN = '6097769249:AAGm64Zhk1Qm5zT_eRVZQgZ_J43XBO5E6xU'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    markup = get_menu_keyboard()
    await message.answer(f"Привет, {user.first_name}! Я бот, который поможет тебе узнать обо мне. "
                         "Выбери, что ты хочешь узнать, используя кнопки ниже. При использовании "
                         "команды /repose ты получишь ссылку на репозиторий с моим исходным кодом ", reply_markup=markup)

# Обработчик команды /repose
@dp.message_handler(commands=['repose'])
async def send_repository_link(message: types.Message):
    repository_link = "https://github.com/slpnv/Yandex_practicum_my_bot"  # ссылка на репозиторий
    await message.answer(f"Исходный код бота доступен в репозитории:\n{repository_link}")


# Обработчик кнопок
@dp.message_handler(lambda message: message.text == "Моё последнее селфи")
async def view_photos(message: types.Message):
    await bot.send_photo(message.chat.id, photo=open('selfie.jpeg', 'rb'))


@dp.message_handler(lambda message: message.text == "Фото из старшей школы")
async def view_photos_2(message: types.Message):
    await bot.send_photo(message.chat.id, photo=open('school_photo.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == "Узнать об увлечении")
async def about_hobby(message: types.Message):
    await message.answer("Моим главным увлечением является изучение искусственного интеллекта и "
                         "разработка полезных приложений на его основе, чтение художественной литратуры"
                         ", кинематограф и многое другое.")

@dp.message_handler(lambda message: message.text == "Прислать голосовое")
async def send_voice(message: types.Message):
    await bot.send_voice(message.chat.id, caption='Объяснение для бабушки, что такое GPT', voice=open('Объяснение-GPT.ogg', 'rb'))
    await bot.send_voice(message.chat.id, caption='Разница между SQL и NoSQL', voice=open('SQL_NoSQL.ogg', 'rb'))
    await bot.send_voice(message.chat.id, caption='История моей первой любви', voice=open('История любви.ogg', 'rb'))

# Получение клавиатуры с кнопками
def get_menu_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Моё последнее селфи", "Фото из старшей школы", "Узнать об увлечении", "Прислать голосовое")
    return markup

if __name__ == '__main__':
    from aiogram import executor
    keep_alive()#запускаем flask-сервер в отдельном
    executor.start_polling(dp, skip_updates=False)
