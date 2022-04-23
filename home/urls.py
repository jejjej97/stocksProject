"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from View.home import views
from View.bookmark import bookmark
from View.sidemenu import sidemenu
from View.user import user
from View.news import news

urlpatterns = [
    # 홈 메뉴
    path('', views.home, name='index'),
    path('index', views.home, name='index'),
    path('search', news.search, name='search'),
    path('top_search', views.top_search, name='top_search'),

    # 사이드메뉴
    path('my', sidemenu.my, name='my'),
    path('all_stocks', views.all_stocks, name='all_stocks'),
    path('kosdaq_all_stocks', views.kosdaq_all_stocks, name='kosdaq_all_stocks'),
    path('up_stocks', views.up_stocks, name='up_stocks'),
    path('kosdaq_up_stocks', views.kosdaq_up_stocks, name='kosdaq_up_stocks'),
    path('down_stocks', views.down_stocks, name='down_stocks'),
    path('kosdaq_down_stocks', views.kosdaq_down_stocks, name='kosdaq_down_stocks'),
    path('top_search_stocks', views.top_search_stocks, name='top_search_stocks'),

    # 유저
    path('register', user.register, name='register'),
    path('registerok', user.registerok, name='registerok'),
    path('registerimpl', user.registerimpl, name='registerimpl'),
    path('registerdel', user.registerdel, name='registerdel'),
    path('registerdelimpl', user.registerdelimpl, name='registerdelimpl'),

    path('login', user.login, name='login'),
    path('logout', user.logout, name='logout'),
    path('loginimpl', user.loginimpl, name='loginimpl'),

    path('update', user.update, name='update'),
    path('updateimpl', user.updateimpl, name='updateimpl'),

    path('password', user.password, name='password'),
    path('passwordimpl', user.passwordimpl, name='passwordimpl'),
    path('changepasswordimpl', user.changepasswordimpl, name='changepasswordimpl'),

    # 뉴스
    path('newsmenu', news.newsmenu, name='newsmenu'),
    path('main_news_crowling', news.main_news_crowling, name='main_news_crowling'),

    # 코스피, 코스닥 그래프
    path('kospigraph', views.kospigraph, name='kospigraph'),
    path('kosdaqgraph', views.kosdaqgraph, name='kosdaqgraph'),

    # 상세 보기
    path('detail', views.detail, name='detail'),
    path('detail_daygraph', views.detail_daygraph, name='detail_daygraph'),
    path('detail_weekgraph', views.detail_weekgraph, name='detail_weekgraph'),
    path('detail_monthgraph', views.detail_monthgraph, name='detail_monthgraph'),
    path('predict_graph', views.predict_graph, name='predict_graph'),
    path('predict_page', views.predict_page, name='predict_page'),

    # 관심 종목 담기
    path('bookmark_insert', bookmark.bookmark_insert, name='bookmark_insert'),
    path('bookmark_selectall', bookmark.bookmark_selectall, name='bookmark_selectall'),
    path('bookmark_delete', bookmark.bookmark_delete, name='bookmark_delete'),
    path('bookmark_alldelete', bookmark.bookmark_alldelete, name='bookmark_alldelete'),
]