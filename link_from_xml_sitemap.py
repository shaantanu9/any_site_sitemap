import requests
from bs4 import BeautifulSoup

i = 0
o = 0
fl = []
while i <62:
    i = i+1
    url = f'https://shodkk.com/sitemap{i}.xml'
    document = requests.get(url)
    soup= BeautifulSoup(document.content,"lxml-xml")
    titles = soup.find_all("loc")

    for data in titles:
        links = data.get_text()
        with open(f"oevenwhole.csv",'a') as f:
            f.write(links,"\n")