# 일일 갱신 뉴스
import json
import urllib.request, bs4
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
import requests

from View.news.newscrowling import allnews_crowling
from Model.news.newsdao.newsdao import NewsDAO
from Model.news.newsvo.newsvo import NewsVO
from Model.sqlitedao import SqliteDao


# 1. 홈페이지 출력 : 오늘의 주요 뉴스
####### 크롤링 시작 #######
# js로 하기

def main_news_crowling(request):
    req = requests.get('https://finance.naver.com/news/mainnews.naver')
    main_web_page = req.content.decode('euc-kr', 'replace')
    main_result = bs4.BeautifulSoup(main_web_page, 'html.parser')
    main_find_news = main_result.find(class_="mainNewsList")
    main_news_list = main_find_news.find_all('li', class_="block1")

    data = []
    for idx in range(len(main_news_list)):
        title = main_news_list[idx].find(class_="articleSubject").find('a').text
        url = "https://finance.naver.com/" + main_news_list[idx].a.attrs.get('href')

        obj = {}
        obj['title'] = title
        obj['url'] = url
        data.append(obj)

    # print(len(data), data)

    return HttpResponse(json.dumps(data), content_type='application/json')

#-------------------------------주요 뉴스 크롤링 데이터 완성------------------------------------


### 2. 메뉴 실시간 속보 뉴스 하루치 ###
####### 크롤링 시작 #######
def newsmenu(request):
    newsdao = NewsDAO('shop');
    data = newsdao.selectall()

    # data = allnews_crowling() # 실시간으로 크롤링 출력

    context = {
        'center': 'news/news_script.html',
        'itemlist': data
    };
    return render(request, 'index.html', context);


### 2. 메뉴 실시간 속보 뉴스 홈화면 검색 ###

def search(request):
    newsdao = NewsDAO('shop');

    # 입력 받기
    search = request.POST['search'];
    data = newsdao.select(search);
    print('표시')

    context = {
        'center': 'news/news_script.html',
        'itemlist': data
    };
    return render(request, 'index.html', context);
