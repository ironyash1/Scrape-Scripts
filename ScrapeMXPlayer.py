# Coded by https://github.com/Ashish0804
# Coded by : @wfjpwf on tg

import requests
import time
import sys

headers = {
}


showid = sys.argv[1].split('-')[-1]
showurl = "https://api.mxplay.com/v1/web/detail/tab/tvshowseasons?type=tv_show&id={}&device-density=2&platform=com.mxplay.desktop&content-languages=hi,en".format(
    showid)
episodesurl = "https://api.mxplay.com/v1/web/detail/tab/tvshowepisodes?type=season&id={}&device-density=1&platform=com.mxplay.desktop&content-languages=hi,en&{}"

seasonids = []


def scrape(showurl, f):
    res = requests.get(showurl, headers=headers).json()
    seasons = res['items']
    for season in seasons:
        seasonids.append(season['id'])
    for seasonid in seasonids:
        next = ''
        while next is not None:
            res = requests.get(episodesurl.format(
                seasonid, next), headers=headers).json()
            next = res['next']
            episodes = res['items']
            try:
                for episode in episodes:
                    f.write('https://mxplayer.in/' + episode['webUrl']+'\n')
            except:
                pass


with open('MXPlayerLinks.txt', 'w') as f:
    scrape(showurl, f)
