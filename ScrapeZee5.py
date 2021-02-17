# Coded by https://github.com/Ashish0804
# Coded by : @wfjpwf on tg
import requests
import time
import sys

headers = {
}


def scrape(url, f):
    id = url.split('/')[-1]
    showurl = 'https://gwapi.zee5.com/content/tvshow/{}?translation=en&country=IN'.format(
        id)

    seasonid = requests.get(
        showurl, headers=headers).json()['season']['id']
    print("Scraping season with id : "+seasonid)
    nexturl = 'https://gwapi.zee5.com/content/tvshow/?season_id={}&type=episode&translation=en&country=IN&on_air=false&asset_subtype=tvshow&page=1&limit=10'.format(
        seasonid)

    while nexturl is not '':
        nexturl = getepisodes(nexturl, f)
        time.sleep(5)


def getepisodes(url, f):
    episodesjson = requests.get(url, headers=headers).json()
    episodes = episodesjson['episode']
    for episode in episodes:
        f.write('https://zee5.com/'+episode['slug']+'\n')
    try:
        nexturl = episodesjson['next_episode_api']
    except:
        nexturl = ''
    return nexturl


with open('Zee5Links.txt', 'w') as f:
    scrape(str(sys.argv[1]).strip(), f)
