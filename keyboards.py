from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

lang_menu = InlineKeyboardMarkup(row_width=2)

lang_eng = InlineKeyboardButton(text='English', callback_data='lang_eng')
lang_ukr = InlineKeyboardButton(text='Українська', callback_data='lang_ukr')

lang_menu.insert(lang_eng)
lang_menu.insert(lang_ukr)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_lang = ReplyKeyboardMarkup(resize_keyboard=True)



btn_random_word = KeyboardButton(text='/random_word')
btn_start_find_words = KeyboardButton(text='/start_search')
btn_another_context = KeyboardButton(text='/another_context')
btn_cancel = KeyboardButton(text='/cancel')
btn_eng = KeyboardButton(text="English")
btn_ukr = KeyboardButton(text="Українська")


kb.add(btn_random_word, btn_start_find_words, btn_another_context)
kb_cancel.add(btn_another_context).add(btn_cancel)
kb_lang.add(btn_eng, btn_ukr)
