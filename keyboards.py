from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


btn_lang_eng = InlineKeyboardButton(text='English', callback_data='lang_eng')
btn_lang_ukr = InlineKeyboardButton(
    text='Українська', callback_data='lang_ukr')
bnt_random_word = InlineKeyboardButton(
    text="Random word", callback_data="/random_word")
btn_another_context = InlineKeyboardButton(
    text="Another context", callback_data="/another_context")
btn_change_lang = InlineKeyboardButton(
    text="Change language", callback_data="/change_language")
btn_to_menu = InlineKeyboardButton(text='Menu', callback_data='/menu')



lang_menu = InlineKeyboardMarkup(row_width=2)
lang_menu.insert(btn_lang_eng)
lang_menu.insert(btn_lang_ukr)


kb = InlineKeyboardMarkup()
kb.insert(btn_change_lang)
kb.insert(bnt_random_word)
kb.insert(btn_another_context)


word_kb = InlineKeyboardMarkup(row_width=3)
word_kb.insert(btn_to_menu)
word_kb.insert(bnt_random_word)
word_kb.insert(btn_another_context)

