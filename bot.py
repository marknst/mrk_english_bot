import logging
import config
import typing
from aiogram import Bot, types, Dispatcher, executor
from eng_words_module import most_popular_words, word_and_context
from keyboards import kb, lang_menu, word_kb
from sqlite.db import Database
from localization import localization

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher(bot)
db = Database('sqlite\database.db')



last_start_message = None

# Start command
@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    global last_start_message
    await message.delete()

    try:
        if last_start_message['message_id']:
            await bot.delete_message(message.chat.id, last_start_message['message_id'])
    except:
        print('There is no /start messages earlier')

    if not db.user_exists(message.from_user.id):
        last_start_message = await bot.send_message(message.chat.id, "Choose bot language: ", reply_markup=lang_menu)
    else:
        user_lang = db.get_lang(message.from_user.id)
        last_start_message = await bot.send_message(message.chat.id, text=localization(user_lang)['start_text'], reply_markup=kb)


@dp.callback_query_handler(text_contains='/menu')
async def go_to_menu(callback: types.CallbackQuery):
    user_lang = db.get_lang(callback.from_user.id)


    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=last_start_message.message_id,
        text=localization(user_lang)['start_text'],
        reply_markup=kb
    )    


# Search words
@dp.message_handler(content_types=types.ContentType.TEXT)
async def search_words(message: types.Message):
    global last_start_message
    await message.delete()

    user_word = message.text
    if user_word.startswith('/'):
        await message.answer("Please enter words without '/'")
    else:
        db.update_last_word(message.from_user.id, user_word)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=last_start_message.message_id, text=word_and_context.get_word_and_context(user_word), reply_markup=word_kb)


# Get context and translate using random word
@dp.callback_query_handler(text_contains='/random_word')
async def get_random_word_and_context(callback: types.CallbackQuery):

    word = most_popular_words.get_random_word()
    db.update_last_word(callback.from_user.id, word)

    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text=word_and_context.get_word_and_context(word),
        reply_markup=word_kb
    )


# Get another context of chosen word
context_index = 0


@dp.callback_query_handler(text_contains='/another_context')
async def get_another_context(callback: types.CallbackQuery):

    global context_index
    context_index += 1

    try:
        another_context = word_and_context.get_another_context(
            db.get_last_word(callback.from_user.id), context_index)
    except:
        context_index = 0
        another_context = word_and_context.get_another_context(
            db.get_last_word(callback.from_user.id), context_index)

    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text=another_context,
        reply_markup=word_kb
    )


# Change bot language
@dp.callback_query_handler(text_contains='/change_language')
async def change_bot_language(callback: types.CallbackQuery):

    user_lang = db.get_lang(callback.from_user.id)

    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text=localization(user_lang)['change_lang_text'],
        reply_markup=lang_menu)


# Callback that waits for 'lang_' callback data
@dp.callback_query_handler(text_contains='lang_')
async def set_bot_language(callback: types.CallbackQuery):

    global user_lang
    user_lang = callback.data[5:]
    if not db.user_exists(callback.from_user.id):
        db.add_user(callback.from_user.id, user_lang)
    else:
        db.update_lang(callback.from_user.id, user_lang)

    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text=localization(user_lang)['start_text'],
        reply_markup=kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
