import json
import urllib.request, bs4
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
import requests
from Model.news.newsdao.newsdao import NewsDAO
from Model.news.newsvo.newsvo import NewsVO
from Model.sqlitedao import SqliteDao

def allnews_crowling():
####### 크롤링 시작 #######
    last = []
    print('DB에 뉴스 담기 시작')
    sqlitedao = SqliteDao('shop');
    sqlitedao.makeTable();
    newsdao = NewsDAO('shop');

    # 뉴스 계속 업로드 시키려면 아래 구문 삭제
    # newsdao.delete();  # 이전 DB 기록된 뉴스 삭제

    # 당일 날짜 url :
    # https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258
    # 날짜, 페이지 양식
    # https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258&date=???&page=???

    ## 날짜 추출 : &date=
    time = datetime.now()
    # 뉴스 자료가 방대하므로 위해 10일 뉴스 분량만 DB에 기록해놓음
    # for i in range(10):  # 범위 숫자를 1000으로 바꾸면 '코드 실행일 ~ 1000일' 까지 크롤링 가능
    for i in range(0):
        day1 = time - timedelta(days=i)
        day2 = day1.isoformat()
        day_y = day2[:4]
        day_m = day2[5:7]
        day_d = day2[8:10]
        day = day_y + day_m + day_d
        print(day)

        url = 'https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258&date=' + str(
            day)
        ## 마지막 페이지 추출 : &page=
        req = requests.get(url)
        web_page = req.content.decode('euc-kr', 'replace')
        result = bs4.BeautifulSoup(web_page, 'html.parser')
        result.find(class_="realtimeNewsList")

        try:
            lastpageurl = result.find(class_="pgRR").a.attrs.get('href')
            # print(lastpageurl)
            lastpagenum = lastpageurl[83:]
            print(lastpagenum)
        except:
            lastpagenum = 1

        #### 본 크롤링

        for page in range(1, int(lastpagenum) + 1):  # int(lastpagenum) + 1
            req = requests.get(
                'https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258&date=' + str(
                    day) + '&page=' + str(page))
            web_page = req.content.decode('euc-kr', 'replace')
            result = bs4.BeautifulSoup(web_page, 'html.parser')
            find_news = result.find(class_="realtimeNewsList")
            news_list = find_news.find_all(class_="articleSubject")
            news_list2 = find_news.find_all(class_="articleSummary")
            print('크롤링 중 날짜:', day, '/ 총 페이지 수:',lastpagenum, '현재 페이지:', page)

            for idx in range(len(news_list)):
                title = news_list[idx].find('a').text
                url = "https://finance.naver.com" + news_list[idx].a.attrs.get('href')
                press = news_list2[idx].find('span', class_="press").text
                dtime = news_list2[idx].find('span', class_="wdate").text
                # DB 저장
                rlist = NewsVO(title, url, press, dtime)
                newsdao.insert(rlist)
                # 실시간 출력
                last.append(NewsVO(title, url, press, dtime))

                ####### 크롤링 완료 #######
    print('뉴스 수량 : ',len(newsdao.selectall()))
    # print('뉴스 수량 : ',len(last))
    print('DB에 뉴스 담기 종료')
    return last

## [미구현]기존 받은 데이터에서 중복 데이터 삽입시 BREAK되도록(newsdao.delete(); 이전 내용 삭제 지우고) ##
allnews_crowling()