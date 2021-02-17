# Coded by https://github.com/Ashish0804
# Coded by : @wfjpwf on tg
import requests
import sys
headers = {
}

baseurl = str(sys.argv[1])


def getepisodes(seasonid):
    print("Getting episodes for season with id: "+str(seasonid))
    url = 'https://apiv2.sonyliv.com/AGL/1.4/R/ENG/WEB/IN/CONTENT/DETAIL/BUNDLE/{}?from=0&to=1000&orderBy=episodeNumber&sortOrder=asc'.format(
        seasonid)
    req = requests.get(url, headers=headers).json()[
        'resultObj']['containers'][0]['containers']
    episodes = []
    for r in req:
        episodes.append(baseurl+str(r['metadata']['episodeTitle'].replace(
            ' ', '-').replace('/', '-').replace('?', '-').replace('---', '-').replace('--', '-').lower())+'-'+str(r['metadata']['contentId']))
    return(episodes)


showid = baseurl.split('-')[-1].strip('/')
seasonids = []
episodes = []
print("Getting Season Ids for show with id: "+str(showid))
showapiurl = 'https://apiv2.sonyliv.com/AGL/1.9/R/ENG/WEB/IN/DL/DETAIL/{}?kids_safe=false&from=0&to=49'.format(
    showid)
showinfo = requests.get(showapiurl, headers=headers).json()[
    'resultObj']['containers'][0]['containers']
for season in showinfo:
    seasonids.append(season['id'])

with open(str(showid) + '.txt', 'w') as f:
    for seasonid in seasonids:
        episodes = (getepisodes(seasonid))
        for episode in episodes:
            f.write(episode + '\n')
        print("Scraped " + str(len(episodes))+" Episodes")
