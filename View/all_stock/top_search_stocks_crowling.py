import bs4
import requests
from django.shortcuts import render

from Model.stocks.stocksvo.stocksvo import StockVO


def top_search_stocks_crowling():
    url = "https://finance.naver.com/sise/lastsearch2.naver"
    response = requests.get(url).text.encode('utf-8')
    response = bs4.BeautifulSoup(response, 'html.parser')
    target = response.find('table', {'class': 'type_5'})

    title = target.select('tr > td > a') # 종목명 a태그 크롤링
    ttitle = target.select('td > a.tltle')  # [<a class="tltle" href="/item/main.naver?code=005930">삼성전자</a>, ... </a>]
    td = target.select('td')  # [<td class="number">1.13%</td>, ... , <td class="number">23.07</td>]

    ttd = []  # td 데이터 가공해서 넣을 리스트 선언
    link = []  # 종목 url 넣을 리스트 선언
    sname = []  # 종목이름 닮을 리스트 선언

    for i in range(30):
        sname.append(title[i].text)  # 종목명 리스트
    # print(sname)
    for i in range(0, len(td)):  # td의 text만 ttd 리스트에 추가
        ttd.append(td[i].text.strip())
        ttd[i] = ttd[i].replace(" ", "")
    for i in range(len(ttitle)):  # 종목 url 크롤링
        if str(ttitle[i]).find('href') != -1:  # href 가지고 있으면 href 크롤링하기
            href = str(ttitle[i])[23:51]
            link.append("https://finance.naver.com" + href)

    # print(link)

    ttd = ' '.join(ttd).split()  # 리스트 값 내의 빈문자열 제거

    # print(ttd)
    items = []
    item2 = []
    n = 0

    for i in range(30):
        rank = ttd[n].strip()
        name = sname[i]
        srate = ttd[n + 2].strip()
        nprice = ttd[n + 3].strip()
        yrate = ttd[n + 4].strip()
        updownrate = ttd[n + 5].strip()
        tamount = ttd[n + 6].strip()
        mprice = ttd[n + 7].strip()
        high = ttd[n + 8].strip()
        low = ttd[n + 9].strip()
        per = ttd[n + 10].strip()
        roe = ttd[n + 11].strip()
        sign = updownrate[0]
        yrate = sign + yrate[:]
        n += 12

        data = StockVO(rank, name, srate, nprice, yrate, updownrate, tamount, mprice, high, low, per, roe, sign,
                       link[i])
        # data2 = rank,name,srate,nprice,yrate,updownrate,tamount,mprice,high,low,per,roe,link[i]

        items.append(data)
        # item2.append(data2)
    return items

# print(top_search_stocks_crowling())