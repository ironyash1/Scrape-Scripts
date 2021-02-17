# Coded by https://github.com/Ashish0804
# Coded by : @wfjpwf on tg


import requests
from bs4 import BeautifulSoup
import time
headers = {

}

URLS = []


def scrape(url):
    print('scraping '+url)
    req = requests.get(
        url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    items = soup.findAll(class_="ATag zIZVd")
    for item in items:
        # showurl = url+item.find('a')['href']
        URLS.append('https://tubi.tv' + item['href'])
    print("sleeping for 5 sec....")
    time.sleep(5)


with open('tubicat.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    scrape(line.strip())

with open('TubiLinks.txt', 'w') as f:
    for URL in URLS:
        f.write(URL+'\n')
