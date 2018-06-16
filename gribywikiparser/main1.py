import requests
from bs4 import BeautifulSoup
import codecs

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

FILENAME_MUSH_INFO = "mushroom_all_spieces.txt"

mush_info = {}

def scrap_chapter(url, page_num, title) :
    page = url
    i = 2
    while True:
        r = requests.get(page)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        content_list = soup.findAll('div', attrs={'class': 'catcont-list__info'})
        for content in content_list:
            title_ru = content.find('a', attrs={'class': 'catcont-list__title'}).text
            title_lat = content.find('span').text
            link = content.find('a', attrs={'class': 'catcont-list__title'})['href']
            mush_info[title_ru] = title , title_lat, link
        if i > page_num: break
        page = url + URLPART_PAGE_NUMBER + i.__str__() + "/"
        i += 1

scrap_chapter(URL_BAD, PAGES_OF_BAD, "NTRL")
scrap_chapter(URL_PSYCHOACTIVE, PAGES_OF_PSYCHO, "PSCH")
scrap_chapter(URL_POISONOUS, PAGES_OF_POISONOUS, "PSNS")
scrap_chapter(URL_GOOD, PAGES_OF_GOOD, "ACPT")
scrap_chapter(URL_CONDITIONAL, PAGES_OF_CONDITIONAL, "CNDT")


i = 1
f = open(FILENAME_MUSH_INFO, 'wb')
for key in mush_info :
    grib = i.__str__()+ "#" + mush_info[key][0] + "#" + key + "#" + mush_info[key][1]+ "#" +  mush_info[key][2] +'\n'
    print(grib)
    f.write(grib.encode('UTF-8'))
    i += 1
f.close()

#<span lang="la" xml:lang="la">Albatrellus confluens</span>
#<div class="catcont-list__info">
#<a class="catcont-list__title" href="http://wikigrib.ru/albatrellus-slivayushhijsya/" rel="bookmark">Альбатреллус сливающийся (Альбатреллус сросшийся)</a>
