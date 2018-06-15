import requests
from bs4 import BeautifulSoup

URL_OBJ_INFO = 'http://www.zakupki.gov.ru/epz/contract/contractCard/payment-info-and-target-of-order.html?reestrNumber='


def get_nums_of_orders(page) :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    #print(soup)
    nums = {}
    soup = soup.findAll('td', attrs= {'class': 'descriptTenderTd'})
    for i in range(soup.__len__()) :
        nums[i] = soup[i].find('dt').find('a').text[2:]
        get_info_of_order(URL_OBJ_INFO + nums[i])
    return nums

def get_info_of_order(page) :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    description = soup.find('div', attrs= {'class':'padBtm5'}).text.strip()
    money = soup.find('tr', attrs= {'class':'tdTotal'}).find('td', attrs={'align':'alignLeft'}).text.strip()
    print(description,money)

def get_orders_names(page) :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    soup = soup.find('table', attrs={'class', 'table table_1'})
    buff = soup.findAll('a')
    titles = []
    for i in range(buff.__len__()):
        titles.append(buff[i].__str__().split('">',1)[1].split('</a',1)[0])
    return titles

def get_links_of_table(page) :
    r = requests.get(page)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    tenders_type_name = soup.findAll('div', attrs={'class':'tenders_caption'})
    tenders_type_content = soup.findAll('ul', attrs={'class':'list tenders_4'})
    tenders_links = {}
    for i in range(tenders_type_name.__len__()):
        name = tenders_type_name[i].find('a').text.strip()
        buff = tenders_type_content[i].findAll('a')
        links = []
        names = []
        count = []
        for k in range(buff.__len__()) :
            link = buff[k].__str__().split('"', 4)[3]
            title = buff[k].__str__().split('"text">', 1)[1].split('</span',1)[0]
            num = buff[k].__str__().split('"number">(', 1)[1].split(')</span',1)[0]
            links.append(link)
            names.append(title)
            count.append(num)
        tenders_links[name] = links, names, count
    return tenders_links
