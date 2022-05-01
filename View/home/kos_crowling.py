import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import datetime
from datetime import datetime, timedelta
from dateutil.parser import parse

def date_format(d):
    date = parse(d)  # 모든 날짜 형식을 알아서 인식해서 바꿔주는 함수. -> from dateutil.parser import parse 임포트할 것.
    date = time.mktime(date.timetuple())  # 타임스탬프 형식으로 바꾸기
    return int(date) * 1000

def daily_data(code='KOSPI',starttime='default',endtime='today',timeframe='day'):
    date_close_list = []

    if endtime == 'today':
        endtime = datetime.today().strftime('%Y%m%d')
    if starttime == 'default':
        date = datetime.strptime(endtime,'%Y%m%d')-timedelta(days=365*10)
        starttime = date.strftime('%Y%m%d')
    url = 'https://api.finance.naver.com/siseJson.naver?symbol='+str(code)+'&requestType=1&startTime='+str(starttime)+'&endTime='+str(endtime)+'&timeframe='+str(timeframe)
    res = urlopen(url, context=ssl.create_default_context())
    soup = BeautifulSoup(res.read(), 'html.parser', from_encoding='utf-8')
    # print('soup????', soup)
    data = str(soup).split('],')
    # print('가공 전 data: ', data)
    for i in range(1,len(data)):
        date = data[i].split(', ')[0].split('["')[1].split('"')[0]
        open = data[i].split(', ')[1]
        high = data[i].split(', ')[2]
        close = data[i].split(', ')[3]
        low = data[i].split(', ')[4]
        volume = data[i].split(', ')[5]
        list = [date, open, high, low, close, volume]
        date = date_format(date)
        date_close = [date, float(close)]
        # print(date_close)
        date_close_list.append(date_close)

    date_close_list.reverse()
    # print(date_close_list)
    return date_close_list

# if __name__ == '__main__':
#     print(daily_data(code='KOSPI',endtime='today', timeframe='day'))
daily_data(code='KOSPI',endtime='today', timeframe='day')
def crowlpi_toss():
    print('코스피 크롤링, 데이터 전송 완료.')
    return daily_data(code='KOSPI',endtime='today', timeframe='day')

def crowldaq_toss():
    print('코스닥 크롤링, 데이터 전송 완료.')
    return daily_data(code='KOSDAQ',endtime='today', timeframe='day')