import bs4
import requests

from View.home.homestocksvo import homestocksvo

def homestocks():

    req = requests.get('https://finance.naver.com/')
    main_web_page = req.content.decode('euc-kr', 'replace')
    main_result = bs4.BeautifulSoup(main_web_page, 'html.parser')
    main_find_news = main_result.find(id="_topItems1")
    main_news_list = main_find_news.find_all('th', scope="row")

    main_find_news2 = main_result.find_all(id="_topItems1")

    url = []
    list = []

    for idx in range(15):
        result = "https://finance.naver.com/" + main_news_list[idx].a.attrs.get('href')
        url.append(result)

    for idx in range(1):
        result = main_find_news2[idx].text
        result2 = result.split('\n')
        list.append(result2)

    items = [];  # 리스트
    items2 = [];  # 오브젝트

    n = 0
    for i in range(10):
        name = list[0][n + 2].strip()
        price = list[0][n + 3].strip()
        udprice1 = list[0][n + 4].strip()
        rate = list[0][n + 5].strip()
        udprice2 = rate[0] + udprice1[3:]
        sign = rate[0]
        num = i + 1

        data = homestocksvo(num, url[i], name, price, udprice2, rate, sign)
        # data2 = num, url[i], name, price, udprice2, rate, sign

        n += 6

        items.append(data)
        # items2.append(data2)

    # print(items)
    # print(items)
    # print(items2)

    return items

# print(home())