import requests
import random
from bs4 import BeautifulSoup
from eng_words_module import words

def random_word():
    return random.choice(words.eng_words)

def random_user_agent():
    user_agent_list = [
        'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    ]
    return random.choice(user_agent_list)


def clean_result_ukr(string: str):
    start_index = string.find('t="')
    end_index = string.rfind('" data-url=')
    new_string = string[start_index:end_index]
    result_string = new_string.replace('t="', '').replace('&lt;em&gt;', '').replace('&lt;/em&gt;', '')
    return result_string


try:
    def get_word_and_context():
        word = random_word()
        url = "https://context.reverso.net/translation/english-ukrainian/" + word
        response = requests.get(
            url, headers={'User-Agent': random_user_agent()})

        html_content = response.text.encode("utf-8")
        soup = BeautifulSoup(html_content, 'html.parser')
        result_eng = soup.find(class_="src ltr").find('span').text.replace(word, word.upper()).strip()
        result_ukr = clean_result_ukr(str(soup.find(class_="add icon addentry")))
        
        return f"{word.upper()}\n🇬🇧: {result_eng}\n🇺🇦: {result_ukr}"
except:
    print("Failed to fetch the webpage: ", response.status_code)
    html_content = None

if __name__ == '__main__':
    get_word_and_context()
