from urllib.request import urlopen
from bs4 import BeautifulSoup


html =urlopen("http://csn.irk.ru")
bsObj = BeautifulSoup(html.read())
print(bsObj.p)