import json
import os

from django.shortcuts import render

os.environ.get("DJANGO_SETTINGS_MODULE")
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

from django.http import HttpResponse

url = "https://finance.naver.com/sise/sise_rise.naver?sosok=0"
response = requests.get(url).text.encode('utf-8')
response = bs4.BeautifulSoup(response, 'html.parser')
kospi_data = response.find('table',{'class':'type_2'})

url2 = "https://finance.naver.com/sise/sise_rise.naver?sosok=1"
response2 = requests.get(url2).text.encode('utf-8')
response2 = bs4.BeautifulSoup(response2, 'html.parser')
kosdaq_data = response2.find('table',{'class':'type_2'})

def stock_call_up(is_kospi=True):
    global kospi_data, kosdaq_data
    if is_kospi:
        target = kospi_data
    else:
        target = kosdaq_data
    thead = target.find_all('th')  # [<th>순위</th>, <th>종목명</th>, ... , <th>PER</th>, <th>ROE</th>]
    trank = target.select('td.no')  # [<td class="no">1</td>, <td class="no">2</td>, ... , <td class="no">29</td>, <td class="no">30</td>]
    ttitle = target.select('td > a.tltle')  # [<a class="tltle" href="/item/main.naver?code=005930">삼성전자</a>, ... </a>]
    td = target.select('td.number')  # [<td class="number">1.13%</td>, ... , <td class="number">23.07</td>]
    ttd = []  # td 데이터 가공해서 넣을 리스트 선언
    lasthreflist = []  # 종목 url 넣을 리스트 선언

    for i in range(0, len(td)):  # td의 text만 ttd 리스트에 추가
        ttd.append(td[i].text.strip())
    for i in range(len(ttitle)):  # 종목 url 크롤링
        if str(ttitle[i]).find('href') != -1:  # href 가지고 있으면 href 크롤링하기
            href = str(ttitle[i])[23:51]
            lasthreflist.append("https://finance.naver.com" + href)

    def list_chunk(lst, n):  # 리스트 쪼개서 리스트안에 쪼갠 리스트 넣는 함수
        return [lst[i:i + n] for i in range(0, len(lst), n)]

    ttd = list_chunk(ttd, 10)  # tdd 리스트 검색비율~ROE까지 10개씩 리스트로 쪼개서 큰 리스트에 다시 넣기

    dic = {}  # 완성된 데이터 넣을 딕셔너리 선언

    for r in range(len(trank)):  # {순위: {'순위':'', '종목명':''} 까지 만드는 for 문
        dic[r+1] = {thead[0].text: trank[r].text,
                    thead[1].text: ttitle[r].text,
                   }
        for k in range(10):  # {순위: {'순위': '', '종목명': '', ..., 'ROE': ''}} 까지 만드는 for 문
            dic[r + 1][thead[k+2].text] = ttd[r][k]

        dic[r + 1]['링크'] = lasthreflist[r]  # {순위: {'순위': '', '종목명': '', ..., 'ROE': '', '링크': ''}} 까지 만듬

    last_json = []  # json 형식으로 담을 리스트 선언 [{},{},..,{}]

    # for key, item in dic.items():  # 키, 값 모두 가져오기 -> [{1: {'순위': '1', '종목명': '삼성전자', ..., {30: {'순위': '30', '종목명': '', ...}}] 형태
    #     last_json.append({key:item})

    for value in dic.values():  # 값만 가져오기 -> [{'순위': '1', '종목명': '삼성전자', ..., {'순위': '30', '종목명': ''}] 의 json 형태
        last_json.append(value)
        if len(last_json) == 100:
            break

    # print(last_json)

    return last_json, lasthreflist

if __name__ == '__main__':
    stock_call_up()


