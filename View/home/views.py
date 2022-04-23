import json

import bs4
import requests
from django.http import HttpResponse
from django.shortcuts import render

from home.main import key_search
from View.all_stock import all_stock_crowling, up_stock_crowling, down_stock_crowling
from home.main.kos_crowling import crowlpi_toss, crowldaq_toss
from View.all_stock.top_search_stocks_crowling import top_search_stocks_crowling
from View.detail.detail_crowling import detail_crowling
from View.detail.predict import stock_predict
from View.home import homestocks
from View.detail.detailstocksvo import detailstocksvo
from Model.news.newsdao.newsdao import NewsDAO

############ 메뉴 구성 ############

def home(request):

    data = homestocks.homestocks()
    context = {
        'items': data
    }
    return render(request, 'index.html', context)

def kospigraph(request):
    data = crowlpi_toss()
    print('kospigraph 실행')
    return HttpResponse(json.dumps(data), content_type='application/json');

def kosdaqgraph(request):
    data = crowldaq_toss()
    print('kosdaqgraph 실행')
    return HttpResponse(json.dumps(data), content_type='application/json');

def all_stocks(r):
    data = all_stock_crowling.stock_call()[0]
    # print('올스톡데이텁니다.', data)
    context = {
        'center':'sidemenu/all_stocks.html',
        'data': data
    }
    # context['center'] = 'sidemenu/all_stocks.html'
    return render(r, 'index.html', context)

def kosdaq_all_stocks(r):
    data = all_stock_crowling.stock_call(is_kospi=False)[0]
    # print('올스톡데이텁니다.', data)
    context = {
        'center':'sidemenu/all_stocks.html',
        'data': data
    }
    # context['center'] = 'sidemenu/all_stocks.html'
    return render(r, 'index.html', context)

def up_stocks(r):
    data = up_stock_crowling.stock_call_up()[0]
    # print('up 데이텁니다.', data)
    context = {
        'center':'sidemenu/up.html',
        'data': data
    }
    # context['center'] = 'sidemenu/up.html'
    return render(r, 'index.html', context)

def kosdaq_up_stocks(r):
    data = up_stock_crowling.stock_call_up(is_kospi=False)[0]
    # print('up 데이텁니다.', data)
    context = {
        'center':'sidemenu/up.html',
        'data': data
    }
    # context['center'] = 'sidemenu/up.html'
    return render(r, 'index.html', context)

def down_stocks(r):
    data = down_stock_crowling.stock_call_down()[0]
    # print('down 데이텁니다.', data)
    context = {
        'center':'sidemenu/down.html',
        'data': data
    }
    # context['center'] = 'sidemenu/down.html'
    return render(r, 'index.html', context)

def kosdaq_down_stocks(r):
    data = down_stock_crowling.stock_call_down(is_kospi=False)[0]
    # print('down 데이텁니다.', data)
    context = {
        'center':'sidemenu/down.html',
        'data': data
    }
    # context['center'] = 'sidemenu/down.html'
    return render(r, 'index.html', context)

def top_search(r):
    keyword = r.POST['search']
    data = key_search.search(keyword)
    try:
        if type(data) == str:
            last = []
            ## 주식 정보 크롤링 ##
            print("url 확인", data)
            crowling = detail_crowling(data)
            data = detailstocksvo(crowling[0], crowling[1], crowling[2], crowling[3], crowling[4], crowling[5], crowling[6],
                                  crowling[7], crowling[8], crowling[9], crowling[10], crowling[11], crowling[12],
                                  crowling[13], crowling[14], crowling[15])
            last.append(data)
            ### 주식 뉴스 ###
            name = crowling[2]

            newsdao = NewsDAO('shop');
            news = newsdao.select(name);

            context = {
                'center': 'detail/detail.html',
                'items': last,
                'itemlist': news,
                'url': data
            }

            return render(r, 'index.html', context)
        else:
            context = {
                'center': 'top_search.html',
                'data': data
            }
            return render(r, 'index.html', context)
    except:
        context = {
            'center': 'top_search.html',
            'center2': 'search_error.html',
        }
        return render(r, 'index.html', context)


def top_search_stocks(request):
    data = top_search_stocks_crowling()
    context = {
        'center': 'sidemenu/top_search_stocks.html',
        'items': data
    };
    return render(request, 'index.html', context)


def detail(request):
    last = []
    ## 주식 정보 크롤링 ##
    url = request.POST["inputurl"];
    print("url 확인",url)
    crowling = detail_crowling(url)
    data = detailstocksvo(crowling[0],crowling[1],crowling[2],crowling[3],crowling[4],crowling[5],crowling[6],crowling[7],crowling[8],crowling[9],crowling[10],crowling[11],crowling[12],crowling[13],crowling[14],crowling[15])
    last.append(data)
    ### 주식 뉴스 ###
    name = crowling[2]

    newsdao = NewsDAO('shop');
    news = newsdao.select(name);

    context = {
        'center': 'detail/detail.html',
        'items': last,
        'itemlist': news,
        'url': url,
        'name': name
    }

    return render(request, 'index.html', context)

def detail_daygraph(request):
    last = []
    ## 주식 정보 크롤링 ##
    url = request.POST["detail_url_day"];
    print("url 확인",url)
    crowling = detail_crowling(url)
    data = detailstocksvo(crowling[0],crowling[1],crowling[2],crowling[3],crowling[4],crowling[5],crowling[6],crowling[7],crowling[8],crowling[9],crowling[10],crowling[11],crowling[12],crowling[13],crowling[14],crowling[15])
    last.append(data)
    ### 주식 뉴스 ###
    name = crowling[2]

    newsdao = NewsDAO('shop');
    news = newsdao.select(name);

    context = {
        'center': 'detail/detail.html',
        'center2': 'detail/detail_daygraph.html',
        'items': last,
        'itemlist': news,
        'url': url
    }

    return render(request, 'index.html', context)

def detail_weekgraph(request):
    last = []
    ## 주식 정보 크롤링 ##
    url = request.POST["detail_url_week"];
    print("url 확인",url)
    crowling = detail_crowling(url)
    data = detailstocksvo(crowling[0],crowling[1],crowling[2],crowling[3],crowling[4],crowling[5],crowling[6],crowling[7],crowling[8],crowling[9],crowling[10],crowling[11],crowling[12],crowling[13],crowling[14],crowling[15])
    last.append(data)
    ### 주식 뉴스 ###
    name = crowling[2]

    newsdao = NewsDAO('shop');
    news = newsdao.select(name);

    context = {
        'center': 'detail/detail.html',
        'center2': 'detail/detail_weekgraph.html',
        'items': last,
        'itemlist': news,
        'url': url
    }

    return render(request, 'index.html', context)

def detail_monthgraph(request):
    last = []
    ## 주식 정보 크롤링 ##
    url = request.POST["detail_url_month"];
    print("url 확인",url)
    crowling = detail_crowling(url)
    data = detailstocksvo(crowling[0],crowling[1],crowling[2],crowling[3],crowling[4],crowling[5],crowling[6],crowling[7],crowling[8],crowling[9],crowling[10],crowling[11],crowling[12],crowling[13],crowling[14],crowling[15])
    last.append(data)
    ### 주식 뉴스 ###
    name = crowling[2]

    newsdao = NewsDAO('shop');
    news = newsdao.select(name);

    context = {
        'center': 'detail/detail.html',
        'center2': 'detail/detail_monthgraph.html',
        'items': last,
        'itemlist': news,
        'url': url
    }

    return render(request, 'index.html', context)

def predict_page(r):
    name = r.POST['stock-name']
    data = stock_predict(name)
    global predict_data
    try:
        predict_data = data[0]
        runtime = round(data[1], 1)
        if predict_data != None:
            context = {
                'center': 'detail/predict.html',
                'name': name,
                'runtime': runtime
            }
            return render(r, 'index.html', context)
    except:
        context = {
            'center': 'detail/predict_error.html',
            'name': name,
        }
        return render(r, 'index.html', context)

def predict_graph(r):
    # name = r.GET['name']
    # predict_data = stock_predict(name)
    print(predict_data)
    return HttpResponse(json.dumps(predict_data), content_type='application/json');
