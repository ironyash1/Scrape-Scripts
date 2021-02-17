from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

import time

# connect chromedrive


def connect():
    #driver = webdriver.Chrome('chromedriver.exe')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

# scrape the webpage for links


def scrape(driver):
    contents = driver.find_elements_by_class_name('normal')
    links = []
    for content in contents:
        try:
            links.append(content.find_element_by_tag_name(
                'a').get_attribute('href'))
        except:
            pass
    return links

# save links to file


def save(links):
    with open('HotstarLinks.txt', 'w') as file:
        file.write('\n'.join(links))


def main():
    driver = connect()
    url = str(sys.argv[1])
    driver.get(url.strip())
    print("Scroll till end to load all episodes and press any key....")
    _ = input()
    print("scraping")
    links = scrape(driver)
    save(links)


if __name__ == '__main__':
    main()
