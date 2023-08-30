start_text = f"""
    🌼 Hello! AVAILABLE COMMANDS:\n
    /random_word - Get a random word, context and translation.
    /start_search - Bot gets into the search mode.
    /cancel - Exit from the search mode.
    /change_language - Change bot language"""
cancel_text = """
    🟠 You just turned off the search mode.\n
    Now you can use next commands: 
    /random_word - Get a random word, context and translation.
    /start_search - Bot gets into the search mode.
    /change_language - Change bot language"""
change_lang_text = "Choose bot language: "
start_search_text = """
    🟢 You just turned on the search mode.\n
    Enter a word or few words in English or Ukrainian.\n
    To turn off, use /cancel."""
new_lang_text = "Bot language - English"


# def change_lang(lang: str):
#     if lang == "English":

#         start_text = f"""
#             🌼 Hello! AVAILABLE COMMANDS:\n
#             /random_word - Get a random word, context and translation.
#             /start_search - Bot gets into the search mode.
#             /cancel - Exit from the search mode."""
#         cancel_text = """
#             🟠 You just turned off the search mode.\n
#             Now you can use next commands:
#             /random_word - Get a random word, context and translation.
#             /start_search - Bot gets into the search mode."""
#         change_lang_text = "Choose bot language: "
#         start_search_text = """
#             🟢 You just turned on the search mode.\n
#             To turn off, use /cancel.\n
#             Enter a word or few words in English or Ukrainian."""
#         new_lang_text = "Bot language - English"

#     if lang == "Українська":

#         start_text = f"""
#             🌼 Привіт! НАЯВНІ КОМАНДИ:\n
#             /random_word - Отримати випадкове слово, контекст до нього та переклад на українську.
#             /start_search - Бот стає в режим пошуку.
#             /cancel - Вийти з режиму пошуку."""
#         cancel_text = """
#             🟠 Ви вийшли з режиму пошуку.\n
#             Тепер ви можете використовувати команди: 
#             /random_word - Використай, щоб отримати випадкове слово, контекст до нього та переклад на українську.
#             /start_search - Бот стає в режим пошуку слів."""
#         change_lang_text = "Оберіть мову бота: "
#         new_lang_text = "Мова бота - Українська"
#         start_search_text = """
#             🟢 Ви увійшли в режим пошуку.\n
#             Щоб завершити, використайте /cancel.\n
#             Введіть слово або кілька слів англійською або українською."""

#     else:
#         new_lang_text
