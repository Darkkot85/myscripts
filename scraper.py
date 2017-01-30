#http://baguzin.ru/wp/?p=14420
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup



try:
    html = urlopen("https://www.python.org")
except HTTPError as e:
    print(e)
try:
    bsObj = BeautifulSoup(html, "html.parser")
    news = bsObj.find('div', {"class": "event-widget"}).ul.findAll("li")
    if news:
        for li in news:
            print('{0:10} ==> {1:10}'.format(li.time.get_text(), li.a.get_text()))
    else:
        print("Блок с событиями не найден, либо изменилась разметка страницы")
except AttributeError as e:
    print("Произошла ошибка парсинга")



