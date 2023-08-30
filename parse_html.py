import requests
import random


def random_user_agent():
    user_agent_list = [
        'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    ]
    return random.choice(user_agent_list)


def parse_html(url: str):
    response = requests.get(
        url, headers={'User-Agent': random_user_agent()})

    if response.status_code == 200:
        html_content = response.text
        return html_content
    else:
        print("Failed to fetch the webpage: ", response.status_code)
        html_content = None
