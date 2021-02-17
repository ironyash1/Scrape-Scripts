# Coded by https://github.com/Ashish0804
# Coded by : @wfjpwf on tg


import requests
import math
import sys

Id = str(sys.argv[1])
url = "https://psapi.voot.com/media/voot/v1/voot-web/content/generic/series-wise-episode?sort=episode%3Aasc&id={}&responseType=common&page=".format(
    Id)
showName = requests.get("https://psapi.voot.com/media/voot/v1/voot-web/content/generic/series-wise-episode?sort=episode%3Aasc&id={}&responseType=common".format(Id)
                        ).json()['result'][0]['showName']+'.txt'

NumberofPages = (math.ceil(int(requests.get(
    "https://psapi.voot.com/media/voot/v1/voot-web/content/generic/series-wise-episode?sort=episode%3Aasc&id={}&responseType=common".format(Id)).json()['totalAsset'])/10))

with open(showName, 'w') as f:
    for i in range(1, NumberofPages+1):
        response = requests.get(url+str(i)).json()['result']
        for ep in response:
            f.write(ep['slug']+'\n')
