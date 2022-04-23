# bookmark
import json

from django.http import HttpResponse
from django.shortcuts import render

from home.main import key_search
from View.detail.detail_crowling import detail_crowling
from View.detail.detailstocksvo import detailstocksvo
from Model.bookmark.bookmarkdao.bookmarkdao import bookmarkDAO
from Model.bookmark.bookmarksql.bookmarksql import bookmarkSql
from Model.bookmark.bookmarkvo.bookmarkvo import bookmarkVO
from Model.news.newsdao.newsdao import NewsDAO
from Model.sqlitedao import SqliteDao

sqlitedao = SqliteDao('shop');
sqlitedao.makeTable();
bookmarkdao = bookmarkDAO('shop');

def bookmark_selectall(request):
    try:
        last = []

        email = request.session['sessionemail']
        # print(email)
        data = bookmarkdao.selectall(email)
        # print(data)

        li = []
        num = 0
        for u in data:
            a = bookmarkVO.pr(u)
            li.append(a);
            # print('li',li)
            # print(li[num][1])
            url = li[num][2]
            # print(url)
            crowling = detail_crowling(url)
            data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                                  crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12], crowling[13],
                                  crowling[14], crowling[15])
            last.append(data)
            num += 1
        # print(last)
        context = {
            'center': 'sidemenu/my.html',
            'data': last
        }
        return render(request, 'index.html', context)

    except:
        context = {
            'center': 'sidemenu/my.html',
        }
        return render(request, 'index.html', context)

def bookmark_insert(request):
    # bookmarkdao.alldelete()
    url = request.POST["bookmarkurl_insert"]
    stockname = request.POST["bookmarkstockname_insert"]
    email = request.session['sessionemail']

    print("확인:",url,stockname,email)
    # 중복 종목 포함 여부 체크
    namelist = []
    stocknames = bookmarkdao.selectall(email)
    for i in range(len(stocknames)):
        a = bookmarkVO.pr(stocknames[i])
        namelist.append(a[1])
    print(namelist)

    # data = []
    if stockname not in namelist:
        print('불포함, 중복 아님')
        data = bookmarkVO(email+stockname, stockname, url)
        try:
            bookmarkdao.insert(data);
            print('OK');
        except Exception as e:
            print('error',e);
        value='ok'
        return HttpResponse(json.dumps(value), content_type='application/json');

    else:
        value = 'no'
        return HttpResponse(json.dumps(value), content_type='application/json');

def bookmark_delete(request):

    url = request.POST["bookmarkurl_delete"]
    stockname = request.POST["bookmarkstockname_delete"]
    email = request.session['sessionemail']
    print("확인:", url, stockname, email)
    value = bookmarkVO(email,stockname,url)
    data = bookmarkdao.select(value)

    if data == []:
        value = 'no'
        return HttpResponse(json.dumps(value), content_type='application/json');
    else:
        bookmarkdao.delete(value)
        value = 'ok'
        return HttpResponse(json.dumps(value), content_type='application/json');


def bookmark_alldelete(request):

    bookmarkdao.alldelete()

    try:
        last = []

        email = request.session['sessionemail']
        print(email)
        data = bookmarkdao.selectall(email)
        print(data)

        li = []
        num = 0
        for u in data:
            a = bookmarkVO.pr(u)
            li.append(a);
            print('li', li)
            print(li[num][1])
            url = li[num][2]
            print(url)
            crowling = detail_crowling(url)
            data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5],
                                  crowling[6],
                                  crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12],
                                  crowling[13],
                                  crowling[14], crowling[15])
            last.append(data)
            num += 1
        print(last)
        context = {
            'center': 'sidemenu/my.html',
            'data': last
        }
        return render(request, 'index.html', context)

    except:
        context = {
            'center': 'sidemenu/my.html',
        }
        return render(request, 'index.html', context)