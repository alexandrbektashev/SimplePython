import scrapping
import string
#50 пунктов на странице
#между первой и второй частью разделитель - это номер страницы
URL_GOS_USLUGI_REESTR1 = "http://www.zakupki.gov.ru/epz/contract/quicksearch/search.html?morphology=on&pageNumber="
URL_GOS_USLUGI_REESTR2 ="&sortDirection=true&recordsPerPage=_50&sortBy=PO_DATE_OBNOVLENIJA&fz44=on&priceFrom=0&priceTo=200000000000&contractStageList_0=on&contractStageList_3=on&contractStageList=0%2C3&regionDeleted=true"

#в конце ставится номер заказа
URL_COMMON_INFO = 'http://www.zakupki.gov.ru/epz/contract/contractCard/common-info.html?reestrNumber='
URL_OBJ_INFO = 'http://www.zakupki.gov.ru/epz/contract/contractCard/payment-info-and-target-of-order.html?reestrNumber='
URL_TABLE = 'http://goszakaz.ru/tenders'

#количесвто обрабатываемых страниц
n_pages = 33

#получаем номера заказов
#for i in range(n_pages) :
 #   page_url = URL_GOS_USLUGI_REESTR1 + i.__str__() + URL_GOS_USLUGI_REESTR2
  #  nums_of_orders = []
   # nums_of_orders.append(scrapping.get_nums_of_orders(page_url))

URL_LIST_1part = 'http://goszakaz.ru'
URL_LIST_2part ='/page'
URL_LIST_3part = '/?order=startdate'

dictionary = {}

dictionary = scrapping.get_links_of_table(URL_TABLE)

orders = []
for val in dictionary :
    links = dictionary[val][0]
    nums = dictionary[val][2]
    for k in range(links.__len__()) :

        if (int(nums[k]) > 30):
            border = int(nums[k])
            pages = border//30

            i = 2
            while (i < pages ) and ( i < 33) :
                str = URL_LIST_1part + links[k] + URL_LIST_2part + i.__str__() + URL_LIST_3part
                orders = scrapping.get_orders_names(str)
                i +=1
        else:
            str = URL_LIST_1part + links[k]
            orders = scrapping.get_orders_names(str)
        f = open(val + '.txt', 'a')
        f.write(orders.__str__() + '\n')
        f.close()