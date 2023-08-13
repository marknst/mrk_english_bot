from aiogram import Bot, types, Dispatcher, executor
import asyncio
import config
from eng_words_module import word_and_context

bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply(f'Hello! Available commands:\n /random_word - Use to get random word, context to it and translate.')

@dp.message_handler(commands=['random_word'])
async def send_random_word_and_context(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=word_and_context.get_word_and_context())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)