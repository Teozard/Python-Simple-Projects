from bs4 import BeautifulSoup
import requests


def get_article_heads(link):
    soup = BeautifulSoup(requests.get(link).text, "html.parser")
    article_heads = [elem.text for elem in soup.find_all('h2', 'story-heading')]
    return article_heads


url = 'http://www.nytimes.com/'
print(get_article_heads(url))
