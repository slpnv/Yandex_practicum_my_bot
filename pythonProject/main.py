import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

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
                         "Выбери, что ты хочешь узнать, используя кнопки ниже.", reply_markup=markup)

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

@dp.message_handler(lambda message: message.text == "Прислать войс")
async def send_voice(message: types.Message):
    await bot.send_voice(message.chat.id, voice=open('voice.ogg', 'rb'))

# Получение клавиатуры с кнопками
def get_menu_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Моё последнее селфи", "Фото из старшей школы", "Узнать об увлечении", "Прислать войс")
    return markup

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
