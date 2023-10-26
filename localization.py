localizations = {
    'eng': {
        'start_text': 
            "🌼 Welcome to Enlish words bot!\n\n"\
            "✏️Enter any word to get context + translate to it.\n\n"
            "Or use next features:\n"\
            "🎲 'Random word' : Random word, context and translation.\n"\
            "🔄 'Another context' : Get another context for last word.\n"\
            "🈳 'Change language' : Change bot language.\n",
        'change_lang_text': "Choose bot language: ",
        'new_lang_text': "Bot language - English",
        'bnt_random_word': 'Random word',
        'btn_another_context': 'Another context',
        'btn_change_lang': 'Change language',
        'btn_to_menu': 'Menu',
    },
    'ukr': {
        'start_text':
            "🌼 Вітаю в English words bot!\n\n"\
            "✏️ Введіть слово щоб отримати контекст до нього та переклад.\n\n"
            "Або скористайся наступними функціями:\n"\
            "🎲 'Випадкове слово' : Випадкове слово, контекст + переклад.\n"\
            "🔄 'Інший контекст' : Отримати інший контекст до останнього слова.\n"\
            "🈳 'Змінити мову' : Змінити мову бота.\n",
        'change_lang_text': "Оберіть мову бота: ",
        'new_lang_text': "Мова бота - Українська",
        'bnt_random_word': 'Випадкове слово',
        'btn_another_context': 'Інший контекст',
        'btn_change_lang': 'Змінити мову',
        'btn_to_menu': 'Меню',
    }
}


def localization(lang='eng'):
    global localizations
    return localizations[lang]
