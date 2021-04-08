import requests
from bs4 import BeautifulSoup


def parse(url,a,class_):
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")
    link = soup.find(a, {'class': class_})
    return link.text
print(parse('https://habr.com/ru/search/?q=python#h', 'a', 'post__title_link'))
print(parse('https://kloop.kg/blog/2021/04/08/tragicheskij-sluchaj-s-ajzadoj-kanatbekovoj-dolzhen-stat-poslednim-v-istorii-krazh-nevest-prezident-zhaparov/', 'h1', 'entry_title'))
print(parse('https://www.google.kg/imghp?hl=ru&tab=ri&ogbl', 'div', 'sfbgg'))
print(parse('https://habr.com/ru/search/?q=python#h', 'em', 'searched-item'))
