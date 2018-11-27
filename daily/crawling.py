import sys
from concurrent.futures import ThreadPoolExecutor
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
import pprint
import os
    
def total_url() -> tuple:
    """ Get total data / total url"""
    # 746ms
    total_url = db.data.find({}, {'_id':0, 'page':1})
    total_url = list(map(lambda i : i['page'], total_url))
    
    return total_url

def crawled_url() -> list:
    """ Get crawled url"""
    # 500ms
    crawled_url = db.uk_181124.find({}, {'_id':0, 'url':1})
    crawled_url = list(map(lambda one_url : one_url['url'], crawled_url))
    
    return crawled_url

def to_crawl_url(total_url, crawled_url) -> list:
    if crawled_url:
        to_crawl_url = set(total_url) - set(crawled_url)
        return to_crawl_url
    else:
        return total_url
    
    
def to_crawl_data() -> list:
    _total_url = total_url()
    _crawled_url = crawled_url() 
    _to_crawl_url = list(to_crawl_url(_total_url, _crawled_url))
    
    _to_crawl_data = db.data.find({"page": { "$in":_to_crawl_url}}, {'_id':0})
    _to_crawl_data = list(map(lambda one_data : tuple(one_data.values()), _to_crawl_data))
    return _to_crawl_data

def get_contents(data):
    (site, url, clicks, impressions, ctr, position, number) = data
    status_code = current_url = page_source = browser_logs = description = description_len = title = title_len = None

    ## headless options\n
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    caps = webdriver.DesiredCapabilities.CHROME
    caps['loggingPrefs'] = {'performance': 'ALL'}
    ## 
    # driver = webdriver.Chrome('C:/Users/ff/Downloads/chromedriver', desired_capabilities=caps, chrome_options=options)
    driver = webdriver.Chrome('/usr/bin/chromedriver', desired_capabilities=caps, chrome_options=options)

    driver.set_page_load_timeout(20)
    driver.set_script_timeout(20)

    print("수집중 URL : ", url)
    try:
        driver.get(url)
        trigger = "success"
    except Exception as e:
        trigger = "fail"

    if trigger == "success":
        try:
            r = requests.get(url)
            status_code = r.status_code
        except Exception as e :
            status_code = 999

        try:
            current_url = driver.current_url
        except Exception as e :
            print("current_url 에러 : ", e)

        try :
            browser_logs = driver.get_log("browser")
        except Exception as e :
            print("browser_logs 에러 : ", e)

        try :
            page_source = driver.page_source
        except Exception as e :
            print("soup 에러 : ", e)

        try:
            soup = BeautifulSoup(page_source , 'html.parser')
            description = soup.find("meta", {"name":"description"})['content']
            description_len = len(description)
        except Exception as e :
            print("description 에러 : ", e)            

        try:
            title = driver.title
            title_len = len(title)
        except Exception as e:
            print("title 에러 : ", e)            

    data = {
        'url' : url ,
        'redirect' : current_url ,
        'time': time.strftime('%D %H:%M:%S') ,
        'page_source':page_source,
        'browser_log': browser_logs ,
        'status_code': status_code ,
        'description': description ,
        'description_len':description_len,
        'title': title,
        'title_len':title_len,
        "site" : site,
        "clicks" : clicks,
        "impressions" : impressions,
        "ctr" : ctr,
        "position" : position,
        "index" : number,
        "trigger" : trigger
    }

    driver.close()
    try:
        driver.quit()
    except Exception as e:
        print("driver 에러 : ", e)        

    db.uk_181124.insert_one(data)


if __name__=='__main__':
    client = MongoClient('112.222.29.147', 27017)
    db = client.get_database('samsung')
    
    data = to_crawl_data()
    print("크롤링할 데이터 : ", len(data))
    print("크롤링할 데이터 : ", type(data))
    print(data[0])
    pool = Pool(processes=96)
    pool.map(get_contents, data) 

       
