import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href')

        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


def get_first_3_pages():
    for page_num in range(3):
        if page_num == 1:
            res = requests.get('https://news.ycombinator.com/news')

        else:
            res = requests.get(
                f'https://news.ycombinator.com/news?p={page_num}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titlelink')
        subtext = soup.select('.subtext')
        pprint.pprint(create_custom_hn(links, subtext))


get_first_3_pages()
