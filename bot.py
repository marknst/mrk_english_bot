import logging
import config
from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from eng_words_module import most_popular_words, word_and_context
from keyboards import kb, kb_cancel, lang_menu
from sqlite.db import Database
from localization import _

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=storage)
db = Database('sqlite\database.db')


class UserStatesGroup(StatesGroup):
    user_word = State()


async def send_start_message(user_id, lang, kb):
    await bot.send_message(user_id, text=_(lang)['start_text'], reply_markup=kb)

# Start command


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id, "Choose bot language: ", reply_markup=lang_menu)
    else:
        lang = db.get_lang(message.from_user.id)
        await message.answer(text=_(lang)['start_text'], reply_markup=kb)


# Exit from all states
@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    lang = db.get_lang(message.from_user.id)
    await message.answer(text=_(lang)['cancel_text'], reply_markup=kb)


# Callback that waits for 'lang_' callback data
@dp.callback_query_handler(text_contains='lang_')
async def set_bot_language(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    global user_lang
    user_lang = callback.data[5:]
    if not db.user_exists(callback.from_user.id):
        db.add_user(callback.from_user.id, user_lang)
        await bot.send_message(callback.from_user.id, text=_(user_lang)['new_lang_text'])
    else:
        db.update_lang(callback.from_user.id, user_lang)
        await bot.send_message(callback.from_user.id, text=_(user_lang)['new_lang_text'])
    await send_start_message(callback.from_user.id, user_lang, kb)


# Change bot language
@dp.message_handler(commands=['change_language'])
async def change_bot_language(message: types.Message):
    lang = db.get_lang(message.from_user.id)
    await bot.send_message(message.from_user.id, text=_(lang)['change_lang_text'], reply_markup=lang_menu)


# Get context and translate using random word
@dp.message_handler(commands=['random_word'])
async def get_random_word_and_context(message: types.Message):
    chat_id = message.from_user.id
    word = most_popular_words.get_random_word()
    await bot.send_message(chat_id=chat_id, text=word_and_context.get_word_and_context(word))


# Go to waiting for user word state
@dp.message_handler(commands=['start_search'])
async def get_user_word_and_context(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.set_state(UserStatesGroup.user_word)
    await message.answer(text=_(lang)['start_search_text'], reply_markup=kb_cancel)


# User word waiting state and than get context and translate
@dp.message_handler(state=UserStatesGroup.user_word)
async def wait_user_word(message: types.Message):
    chat_id = message.from_user.id
    word = message.text
    await bot.send_message(chat_id=chat_id, text=word_and_context.get_word_and_context(word))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
