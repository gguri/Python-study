import sys
from concurrent.futures import ThreadPoolExecutor
import feedparser
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from queue import Queue, Empty
import pandas as pd
import json
import re
import time
import json
from multiprocessing import Pool # Pool import하기
from pymongo import MongoClient

## headless options\n
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

def url_filter(links):
    global domain
    frame = pd.DataFrame({'href':links})

    if len(frame > 0):
        frame = frame.dropna()                                                # na 데이터 제거
        frame = frame[~frame['href'].str.startswith('#')]                     # '#'로 시작하는 데이터 제거
        frame = frame[~frame['href'].str.startswith('javascript')]            # 'javascript'로 시작하는 데이터 제거
        frame = frame['href'].replace(regex = ['^//'], value = 'https://')    # /~~~로 시작하는 href에 domain 추가
        frame = frame.str.replace('^/', domain)                               # /~~~로 시작하는 href에 domain 추가
        frame = frame.str.replace('\n|\t', '')                                # html문법기호 삭제
        frame = frame.str.replace('^http://', "https://")                     # http -> https
        frame = frame.loc[frame.str.contains('https://www.uplus.co.kr/')]      # domain : https://www.uplus.co.kr 가 존재하는 문자열만 추출
        frame = frame.loc[~frame.str.startswith('https://www.uplus.co.kr:')]
        frame = frame.loc[~frame.str.startswith('https://www.uplus.co.kr/hashtag')]
        frame = frame.drop_duplicates()                                       # 중복제거
        frame = frame.reset_index(drop = True)                                # index 초기화
        frame = frame.get_values().tolist()

        return frame

    else :
        return frame


def first_get_url_list(first_url):
    driver.get(first_url)
    soup = BeautifulSoup(driver.page_source , 'html.parser')
    links = [element.get('href') for element in soup.find_all('a')]
    driver.close()

    url_lists = url_filter(links)

    return url_lists


def get_contents(url):
        caps = webdriver.DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'performance': 'ALL'}
        driver = webdriver.Chrome('C:/Users/ff/Downloads/chromedriver', chrome_options=options)
        driver.implicitly_wait(3)
        time.sleep(1)
        print("URL : {} 수집중 *******************".format(url) )
        try:
            driver.get(url)
            r = requests.get(url)
            status_code = r.status_code
        except ConnectionError as timeout :
            print("Error발생 : Connection aborted")
            status_code = 598
        except Exception as e :
            print("Error발생 : {}".format(e))
            status_code = 999

        try :
            current_url = driver.current_url
        except Exception as e :
            current_url = 'error'

        try :
            browser_logs = driver.get_log("browser")
        except Exception as e :
            browser_log = ['error']

        try :
            network_logs = driver.get_log("performance")
        except Exception as e :
            network_logs = ['error']

        try :
            soup = BeautifulSoup(driver.page_source , 'html.parser')
            href = [element.get('href') for element in soup.find_all('a')]
        except Exception as e :
            href = ['error']

        try:
            cookies = driver.get_cookies()
        except Exception as e :
            cookies = ['error']

        data = {
            'url' : url ,
            'redirect_url' : current_url ,
            'time': time.strftime('%D %H:%M:%S') ,
            'browser_log': browser_logs ,
            'network_log': network_logs ,
            'status_code': status_code ,
            'cookies' : cookies,
            'href' : href
        }
        driver.close()

        return data



def export_date_excel(request):
    dataF = request
    filename = 'error_result_180808.xlsx'
    dataF.to_excel(filename,'Sheet1',index=False, engine='xlsxwriter')


if __name__=='__main__':
    start_time = time.time()
    domain = "https://www.uplus.co.kr/"
    crawled_url = set([])
    ## mongodb
    client = MongoClient('localhost', 27017)
    db = client.get_database('crawler')

    """
    driver = webdriver.Chrome('C:/Users/ff/Downloads/chromedriver', chrome_options=options)
    driver.implicitly_wait(3)
    first_url = domain + 'home/Index.hpi'

    url_lists = first_get_url_list(first_url)

    print(" Depth 1단계 시작 ")
    pool = Pool(processes=8) # 4개의 프로세스를 사용합니다.
    result = pool.map(get_contents, url_lists) # get_content 함수를 넣어줍시다.
    db.uplus_save.insert_many(result)
    """

    start_point = 0
    depth = 0
    while True:
        ''' depth 1에서 방문한 URL => set에 저장 '''
        for i in range(start_point, db.uplus_save.find().count()):
            url = db.uplus_save.find()[i].get('url')
            crawled_url.add(url)


        ''' depth 1에서 추출된 href에서 방문안한 URL 추출 '''

        print('not_crawl_url 처리 시작')
        not_crawl_url = []
        for i in range(start_point, db.uplus_save.find().count()):
            redirect_url = db.uplus_save.find()[i].get('redirect_url')
            if bool(re.match("^(https://www.uplus.co.kr/)", redirect_url)):
                target_url = db.uplus_save.find()[i].get('url')
                target_href_url = url_filter(db.uplus_save.find_one({'url' : target_url}).get('href'))
                for j in range(len(target_href_url)):
                    if target_href_url[j] not in crawled_url:
                        not_crawl_url.append(target_href_url[j])
        not_crawl_url = list(set(not_crawl_url))
        not_crawl_url.sort()


        if len(not_crawl_url) == 0:
            break


        start_point = db.uplus_save.find().count()

        ''' depth 시작 '''
        depth += 1
        print(" Depth {}단계 시작 ".format(depth))
        print(" URL 개수 : {}".format(len(not_crawl_url)))

        if len(not_crawl_url) != 0:
            pool2 = Pool(processes=8)
            result = pool2.map(get_contents, not_crawl_url) # 450~ success 850-900
            db.uplus_save.insert_many(result)


    print('**************************************************************************************')
    print("전체 크롤링 완료 : depth {}".format(depth))
    print("--- %s seconds ---" % (time.time() - start_time))
    print('**************************************************************************************')


# depth0 : 324개   1354 sec
# depth1 : 1267개
