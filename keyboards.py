from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_lang = ReplyKeyboardMarkup(resize_keyboard=True)


btn_random_word = KeyboardButton(text='/random_word')
btn_start_find_words = KeyboardButton(text='/start_search')
btn_cancel = KeyboardButton(text='/cancel')
btn_eng = KeyboardButton(text="English")
btn_ukr = KeyboardButton(text="Українська")


kb.add(btn_random_word, btn_start_find_words)
kb_cancel.add(btn_cancel)
kb_lang.add(btn_eng, btn_ukr)
