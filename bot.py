from aiogram import Bot, types, Dispatcher, executor
import config
from eng_words_module import word_and_context
from eng_words_module import most_popular_words
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import kb, kb_cancel, kb_lang
from localization import start_text, cancel_text, change_lang_text, new_lang_text, start_search_text


storage = MemoryStorage()
bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=storage)


class UserStatesGroup(StatesGroup):
    user_word = State()
    lang = State()


# Start command
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text=start_text, reply_markup=kb)


# Exit from all states
@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=cancel_text, reply_markup=kb)


# # Change bot language
# @dp.message_handler(commands=['change_language'])
# async def change_bot_language(message: types.Message, state: FSMContext):
#     await state.set_state(UserStatesGroup.lang)
#     await message.answer(change_lang_text, reply_markup=kb_lang)


# @dp.message_handler(state=UserStatesGroup.lang)
# async def wait_bot_lang(message: types.Message, state: FSMContext):
#     lang = message.text
#     await change_lang(lang)
#     await state.finish()
#     await message.answer(new_lang_text)


# Get context and translate using random word
@dp.message_handler(commands=['random_word'])
async def get_random_word_and_context(message: types.Message):
    chat_id = message.from_user.id
    word = most_popular_words.get_random_word()
    await bot.send_message(chat_id=chat_id, text=word_and_context.get_word_and_context(word))


# Go to waiting for user word state
@dp.message_handler(commands=['start_search'])
async def get_user_word_and_context(message: types.Message, state: FSMContext):
    await state.set_state(UserStatesGroup.user_word)
    await message.answer(text=start_search_text, reply_markup=kb_cancel)


# User word waiting state and than get context and translate
@dp.message_handler(state=UserStatesGroup.user_word)
async def wait_user_word(message: types.Message):
    chat_id = message.from_user.id
    word = message.text
    await bot.send_message(chat_id=chat_id, text=word_and_context.get_word_and_context(word))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
