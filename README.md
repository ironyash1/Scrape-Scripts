# Scrape-Scripts

Scripts to scrape episode links from various streaming sites

Currently Supported SonyLiv, TubiTv, Voot, Zee5, Hotstar, MxPlayer

## Requesting for a site

Open a new issue with site name

## Instatting the requirements

`pip install -r requirements.txt`

## Getting Headers

0. Open new tab
1. Open Dev tools by pressing F12
2. Switch to **Network** tab
3. Go to the streaming site (example : https://mxplayer.in)
4. Right click on the first packet in the **Network** tab (should be the website url)
5. navigate to Copy -> Copy as cURL
6. Go to https://curl.trillworks.com/
7. Paste the curl command
8. Copy just the headers from output to the python file

## Usage

### Sonyliv

`python ScrapeSonyLiv.py URL`

Example

`python ScrapeSonyLiv.py https://www.sonyliv.com/shows/suryaputra-karn-1700000150`

### TubiTv

Paste all the links in **tubicat.txt**

`python ScrapeTubi.py`

### Voot

`python ScrapeVoot.py id`

**id** is the id of the first episode of the series

Example

For https://www.voot.com/shows/mahavir-hanuman/100616

**id** is **429460** from https://www.voot.com/shows/mahavir-hanuman/1/429460/mahavir-hanuman-is-born/424498

`python ScrapeVoot.py 429460`

### Zee5

`python ScrapeZee5.py URL`

Example

`python ScrapeZee5.py https://www.zee5.com/kids/kids-shows/krishna-balram/0-6-1871`

### Hotstar

`python ScrapeHotstar.py URL`

### MxPlayer

`python ScrapeMXPlayer.py URL`

Example

`python ScrapeMXPlayer.py https://www.mxplayer.in/show/watch-crash-hindi-dubbed-series-online-36786766623a07382dc3d2f99d036e5d`
