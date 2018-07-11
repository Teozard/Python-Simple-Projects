from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
h2 = soup.find_all('h2', 'story-heading')

article_heads = []

for elem in len(h2):
    title = soup.find('h2', 'story-heading').string[elem]
    article_heads.append(title)
'
print(len(h2))
