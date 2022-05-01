import time

from django.shortcuts import render
from selenium import webdriver
import requests
import bs4
from webdriver_manager.chrome import ChromeDriverManager


def search(key):
    print("key:",key)
    if key == '':
        return None
    else :
        print('top.search.search() 실행 받은 데이터: ', key)

        # 크롤링 옵션 생성
        options = webdriver.ChromeOptions()
        # 백그라운드 실행 옵션 추가
        options.add_argument("headless")
        # 크롬 드라이버 실행
        # driver = webdriver.Chrome('chromedriver.exe', options=options)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        driver.get('https://finance.naver.com/')
        driver.find_element_by_id('stock_items').send_keys(key)
        driver.find_element_by_css_selector('button.snb_search_btn').click()
        time.sleep(1)
        print(driver.find_elements_by_css_selector('.paging > a'))
        if len(driver.find_elements_by_css_selector('.paging')) == 0:
            one_url = driver.current_url
            return one_url
        else:
            page = driver.find_elements_by_css_selector('.paging > a')
            print(len(page))
        td_list = []
        href_list = []
        for p in page:
            url = p.get_attribute('href')
            response = requests.get(url).text.encode('utf-8')
            response = bs4.BeautifulSoup(response, 'html.parser')
            target = response.find('table', {'class': 'tbl_search'})
            td = target.select('td')
            href = target.find_all('a')
            for d in td:
                td_list.append(d.text.strip())
            for h in href:
                link = 'https://finance.naver.com' + h['href']
                href_list.append(link)

        def list_chunk(lst, n):  # 리스트 쪼개서 리스트안에 쪼갠 리스트 넣는 함수
            return [lst[i:i + n] for i in range(0, len(lst), n)]

        td_list = list_chunk(td_list, 8)

        thead = target.find_all('span')
        # print('티해드', thead)
        # print('td리스트', td_list)

        dic = {}

        for r in range(len(td_list)):  # {1: {'종목명':'', '현재가':'', ...}} 까지 만드는 for 문
            dic[r+1] = {thead[0].text: td_list[r][0],
                        thead[1].text: td_list[r][1],
                        thead[2].text: td_list[r][2],
                        thead[3].text: td_list[r][3],
                        thead[4].text: td_list[r][4],
                        thead[5].text: td_list[r][5],
                        thead[6].text: td_list[r][6],
                        thead[7].text[:4]: td_list[r][7],
                       }
            dic[r + 1]['링크'] = href_list[r]  # {1: {'종목명': '', ..., '링크': ''}} 까지 만듬

        last_json = []  # json 형식으로 담을 리스트 선언 [{},{},..,{}]

        for value in dic.values():  # 값만 가져오기 -> [{'순위': '1', '종목명': '삼성전자', ..., {'순위': '30', '종목명': ''}] 의 json 형태
            last_json.append(value)


        driver.quit()
        print(last_json)
        return last_json



if __name__ == '__main__':
    search('i')
