import requests
from bs4 import BeautifulSoup as BS
link = "https://en.wikipedia.org/wiki/Fiber"
f = requests.get(link)
soup = BS(f.text,"html")
for text in soup.find_all('div', class_='article-additional-info'):
        for links in text.find_all('a'):
                    print links.get('href')



