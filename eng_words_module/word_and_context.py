from bs4 import BeautifulSoup
from parse_html import parse_html

try:
    def get_word_and_context(word: str, index: int = 0):
        url = "https://context.reverso.net/translation/english-ukrainian/" + word

        html_content = parse_html(url)
        soup = BeautifulSoup(html_content, 'html.parser')

        string_eng = soup.find(class_="src ltr").find('span')
        result_eng = string_eng.text.replace(word, f'[ {word} ]').strip()

        string_ukr = (soup.find('button', attrs={'data-text': True}))
        result_ukr = string_ukr['data-text'].replace(
            '<em>', '[ ').replace('</em>', ' ]')

        return f"{word.upper()}\n▫️: {result_eng}\n◾️: {result_ukr}"
    
    def get_another_context(word: str):
        get_word_and_context(word)
except:
    print("Failed to fetch the webpage: ")
    html_content = None

