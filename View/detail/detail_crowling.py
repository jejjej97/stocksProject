import bs4
import requests



def detail_crowling(url):
    # for i in url():
    # 상세 페이지 크롤링 시작
    req = requests.get(url)
    detailstocks1 = req.content.decode('euc-kr', 'replace')
    detailstocks2 = bs4.BeautifulSoup(detailstocks1, 'html.parser')
    detailstocks3 = detailstocks2.find('div', class_="new_totalinfo")
    detailstocks4 = detailstocks3.find_all('dd')

    data = []
    for i in range(12):
        result = detailstocks4[i].text
        data.append(result)
    # print(data)

    sign = ''  # 기호
    if data[3][4:].split(' ')[2] == '하락':
        sign = '-'
    elif data[3][4:].split(' ')[2] == '상승':
        sign = '+'
    else:
        sign = ''
    name = data[1][4:]  # 종목명
    code = data[2][5:][:-4]  # 종목 코드
    price = data[3][4:].split(' ')[0]  # 현재가
    p_eve_price = sign + data[3][4:].split(' ')[3]  # 전일 대비
    eve_price_rate = sign + data[3][4:].split(' ')[5] + '%'  # 등락률
    eve_price = data[4][4:]  # 전일가
    m_price = data[5][3:]  # 시가
    h_price = data[6][3:]  # 고가
    l_price = data[8][3:]  # 저가
    trace = data[10][4:]  # 거래량
    trace_price = data[11][5:]  # 거래대금
    day_graph = 'https://ssl.pstatic.net/imgfinance/chart/item/candle/day/' + str(code) + '.png?sidcode=1643450737002'
    week_graph = 'https://ssl.pstatic.net/imgfinance/chart/item/candle/week/' + str(code) + '.png?sidcode=1643450737002'
    month_graph = 'https://ssl.pstatic.net/imgfinance/chart/item/candle/month/' + str(
        code) + '.png?sidcode=1643450737002'

    return url, sign, name, code, price, p_eve_price, eve_price_rate, eve_price, m_price, h_price,l_price, trace, trace_price, day_graph, week_graph, month_graph

# print(detail_crowling(url))