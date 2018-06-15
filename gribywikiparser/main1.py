import requests
from bs4 import BeautifulSoup

URL_MAIN_PAGE = "http://wikigrib.ru/vidy/"
URL_GOOD = "http://wikigrib.ru/vidy/sedobnye-griby/"
PAGES_OF_GOOD = 25
URL_CONDITIONAL = "http://wikigrib.ru/vidy/uslovno-sedobnye/"
PAGES_OF_CONDITIONAL = 26
URL_BAD = "http://wikigrib.ru/vidy/nesedobnye-griby/"
PAGES_OF_BAD = 43
URL_PSYCHOACTIVE = "http://wikigrib.ru/vidy/nesedobnye-griby/gallyucinogennye-griby/"
PAGES_OF_PSYCHO = 2
URL_POISONOUS = "http://wikigrib.ru/vidy/nesedobnye-griby/yadovitye-griby/"
PAGES_OF_POISONOUS = 9

URLPART_PAGE_NUMBER = "page/"

mush_info = {}
print("bad")
page = URL_BAD
i = 2
while i < PAGES_OF_BAD :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    content_list = soup.findAll('div', attrs= {'class': 'catcont-list__info'})
    for content in content_list :
        title_ru = content.find('a', attrs= {'class': 'catcont-list__title'}).text
        title_lat = content.find('span').text
        link = content.find('a', attrs= {'class': 'catcont-list__title'})['href']
        mush_info[title_ru] = "NTRL", title_lat, link
    page = URL_BAD + URLPART_PAGE_NUMBER + i.__str__() + "/"
    i += 1
print("good")

page = URL_POISONOUS
i = 2
while i < PAGES_OF_POISONOUS :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    content_list = soup.findAll('div', attrs= {'class': 'catcont-list__info'})
    for content in content_list :
        title_ru = content.find('a', attrs= {'class': 'catcont-list__title'}).text
        title_lat = content.find('span').text
        link = content.find('a', attrs= {'class': 'catcont-list__title'})['href']
        mush_info[title_ru] = "PSNS", title_lat, link
    page = URL_POISONOUS + URLPART_PAGE_NUMBER + i.__str__() + "/"
    i += 1
print("psch")

page = URL_PSYCHOACTIVE
i = 2
while i < PAGES_OF_PSYCHO :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    content_list = soup.findAll('div', attrs= {'class': 'catcont-list__info'})
    for content in content_list :
        title_ru = content.find('a', attrs= {'class': 'catcont-list__title'}).text
        title_lat = content.find('span').text
        link = content.find('a', attrs= {'class': 'catcont-list__title'})['href']
        mush_info[title_ru] = "PSCH", title_lat, link
    page = URL_PSYCHOACTIVE + URLPART_PAGE_NUMBER + i.__str__() + "/"
    i += 1

page = URL_GOOD

i = 2
while i < PAGES_OF_GOOD :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    content_list = soup.findAll('div', attrs= {'class': 'catcont-list__info'})
    for content in content_list :
        title_ru = content.find('a', attrs= {'class': 'catcont-list__title'}).text
        title_lat = content.find('span').text
        link = content.find('a', attrs= {'class': 'catcont-list__title'})['href']
        mush_info[title_ru] = "ACPT", title_lat, link
    page = URL_GOOD + URLPART_PAGE_NUMBER + i.__str__() + "/"
    i += 1

page = URL_CONDITIONAL
i = 2
while i < PAGES_OF_CONDITIONAL :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    content_list = soup.findAll('div', attrs= {'class': 'catcont-list__info'})
    for content in content_list :
        title_ru = content.find('a', attrs= {'class': 'catcont-list__title'}).text
        title_lat = content.find('span').text
        link = content.find('a', attrs= {'class': 'catcont-list__title'})['href']
        mush_info[title_ru] = "CNDT", title_lat, link
    page = URL_CONDITIONAL + URLPART_PAGE_NUMBER + i.__str__() + "/"
    i += 1



for key in mush_info :
    print(key + " " + mush_info[key][0]+ " " + mush_info[key][1] + " " + mush_info[key][2])


#<span lang="la" xml:lang="la">Albatrellus confluens</span>
#<div class="catcont-list__info">
#<a class="catcont-list__title" href="http://wikigrib.ru/albatrellus-slivayushhijsya/" rel="bookmark">Альбатреллус сливающийся (Альбатреллус сросшийся)</a>
