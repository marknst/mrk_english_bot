from bs4 import BeautifulSoup
from eng_words_module import make_result_clean
from parse_html import parse_html

try:
    def get_word_and_context(word: str):
        url = "https://context.reverso.net/translation/english-ukrainian/" + word

        html_content = parse_html(url)
        soup = BeautifulSoup(html_content, 'html.parser')

        string_eng = soup.find(class_="src ltr").find('span')
        result_eng = string_eng.text.replace(word, f'*{word}*').strip()

        string_ukr = str(soup.find(class_="add icon addentry"))
        result_ukr = make_result_clean.clean_result_ukr(string_ukr)

        return f"{word.upper()}\n▫️: {result_eng}\n◾️: {result_ukr}"
except:
    print("Failed to fetch the webpage: ")
    html_content = None

# if __name__ == '__main__':
#     get_word_and_context()
