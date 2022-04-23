# bookmark
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
        print(email)
        data = bookmarkdao.selectall(email)
        print(data)

        li = []
        num = 0
        for u in data:
            a = bookmarkVO.pr(u)
            li.append(a);
            print('li',li)
            print(li[num][1])
            url = li[num][2]
            print(url)
            crowling = detail_crowling(url)
            data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                                  crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12], crowling[13],
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

def bookmark_insert(request):
    # bookmarkdao.alldelete()
    print('확인해보자')
    url = request.POST["bookmarkurl"]
    stockname = request.POST["bookmarkstockname"]
    email = request.session['sessionemail']
    total_num = len(bookmarkdao.selectall(email))

    # 중복 종목 포함 여부 체크
    namelist = []
    stocknames = bookmarkdao.selectall(email)
    for i in range(len(stocknames)):
        a = bookmarkVO.pr(stocknames[i])
        namelist.append(a[1])
    print(namelist)

    if stockname not in namelist:
        print('불포함, 중복 아님')
        for i in range(1):
            data = bookmarkVO(email+str(total_num+len(stocknames)),stockname,url)
            try:
                bookmarkdao.insert(data);
                print('OK');
            except Exception as e:
                print('error',e);

        data = bookmarkdao.selectall(email)
        print('data',data)
        li = []
        for u in data:
            a = bookmarkVO.pr(u)
            li.append(a);
        print('li',li)

        # 화면 유지
        last = []
        ## 주식 정보 크롤링 ##
        print("url 확인", url)
        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12], crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        ### 주식 뉴스 ###
        name = crowling[2]

        newsdao = NewsDAO('shop');
        news = newsdao.select(name);

        context = {
            'center': 'detail/detail.html',
            'detailm': 'detail/bookmark_insertok.html',
            'items': last,
            'itemlist': news
        }
        return render(request, 'index.html', context)
    else:
        print('중복 종목')
        url = request.POST["bookmarkurl"]
        stockname = request.POST["bookmarkstockname"]
        email = request.session['sessionemail']
        data = bookmarkVO(email, stockname, url)
        print('한번 확인2 : ', data)

        # 화면 유지
        last = []
        ## 주식 정보 크롤링 ##
        print("url 확인", url)
        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5],
                              crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12],
                              crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        ### 주식 뉴스 ###
        name = crowling[2]

        newsdao = NewsDAO('shop');
        news = newsdao.select(name);

        context = {
            'center': 'detail/detail.html',
            'detailm': 'detail/bookmark_insertfail2.html',
            'items': last,
            'itemlist': news
        }

        return render(request, 'index.html', context)


def bookmark_delete(request):

    url = request.POST["bookmarkstockurl"]
    name = request.POST["bookmarkname"]
    email = request.session['sessionemail']

    value = bookmarkVO(email,name,url)
    data = bookmarkdao.select(value)
    print('확인1')
    print(data)

    if data == []:
        print('데이터 없다 넘어감1')
        # 화면 유지
        last = []
        ## 주식 정보 크롤링 ##
        print("url 확인", url)
        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12],
                              crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        ### 주식 뉴스 ###
        name = crowling[2]

        newsdao = NewsDAO('shop');
        news = newsdao.select(name);

        context = {
            'center': 'detail/detail.html',
            'detailm': 'detail/bookmark_delfail.html',
            'items': last,
            'itemlist': news
        }

        return render(request, 'index.html', context)

    else:
        print('데이터 있다 넘어감2')
        delvalue = bookmarkVO(email, name, url)
        bookmarkdao.delete(delvalue)
        # 화면 유지
        last = []
        ## 주식 정보 크롤링 ##

        print("url 확인", url)
        crowling = detail_crowling(url)
        data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                              crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12],
                              crowling[13],
                              crowling[14], crowling[15])
        last.append(data)
        ### 주식 뉴스 ###
        name = crowling[2]

        newsdao = NewsDAO('shop');
        news = newsdao.select(name);

        context = {
            'center': 'detail/detail.html',
            'detailm': 'detail/bookmark_delok.html',
            'items': last,
            'itemlist': news
        }

        return render(request, 'index.html', context)

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