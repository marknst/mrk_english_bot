from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from localization import localization


def lang_menu(user_language='eng'):

    btn_lang_eng = InlineKeyboardButton(
        text='English', callback_data='lang_eng')
    btn_lang_ukr = InlineKeyboardButton(
        text='Українська', callback_data='lang_ukr')

    lang_menu = InlineKeyboardMarkup(row_width=2)
    lang_menu.insert(btn_lang_eng)
    lang_menu.insert(btn_lang_ukr)

    return lang_menu


def main_kb(user_language='eng'):

    btn_change_lang = InlineKeyboardButton(
        text=localization(user_language)['btn_change_lang'], callback_data="/change_language")
    bnt_random_word = InlineKeyboardButton(
        text=localization(user_language)['bnt_random_word'], callback_data="/random_word")
    btn_another_context = InlineKeyboardButton(
        text=localization(user_language)['btn_another_context'], callback_data="/another_context")

    kb = InlineKeyboardMarkup()
    kb.insert(btn_change_lang)
    kb.insert(bnt_random_word)
    kb.insert(btn_another_context)

    return kb

def word_kb(user_language='eng'):

    btn_to_menu = InlineKeyboardButton(
        text=localization(user_language)['btn_to_menu'], callback_data='/menu')
    bnt_random_word = InlineKeyboardButton(
        text=localization(user_language)['bnt_random_word'], callback_data="/random_word")
    btn_another_context = InlineKeyboardButton(
        text=localization(user_language)['btn_another_context'], callback_data="/another_context")

    word_kb = InlineKeyboardMarkup(row_width=3)
    word_kb.insert(btn_to_menu)
    word_kb.insert(bnt_random_word)
    word_kb.insert(btn_another_context)

    return word_kb









