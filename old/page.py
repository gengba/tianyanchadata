#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from old import conn_mysql


def driver_open():

    driver = webdriver.Chrome()
    return driver


def get_status(url):

    r = requests.get(url)
    if r.status_code == '200':
        print(r.status_code)
        return True
    return False


def get_content(driver, url):

    # driver.get('https://www.tianyancha.com')
    # for cookie in config.COOKIES:
        # driver.add_cookie(cookie)
    driver.get(url)
    content = driver.page_source.encode('utf-8')
    driver.close()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    return soup


def get_basic_info(soup):

    basics = soup.findAll(name='div', attrs={'class': 'search_right_item'})
    # print(basics)
    for basic in basics:
        website = str(basic.find('a').get('href'))
        print(u'网址：' + website)
        status = str(basic.findAll('div')[1].get_text())
        print(u'状态：' + status)
        location = str(basic.findAll('span')[1].get_text())
        print(u'地区: ' + location)
        try:
            fddbr = str(basic.findAll('div')[4].find('a').get_text())
        except:
            fddbr = str(basic.findAll('div')[4].find('span').get_text())
        print(u'法定代表人：' + fddbr)
        zczb = str(basic.findAll('div')[5].find('span').get_text())
        print(u'注册资本：'+zczb)
        zcrq = str(basic.findAll('div')[6].find('span').get_text())
        print(u'注册时间：' + zcrq)
        try:
            phone = str(basic.findAll('div')[9].findAll('span')[1].get_text())
        except:
            phone = ''
        print(u'电话:' + phone)
        print('---------next-----------')
        record = (website, status, location, fddbr, zczb, zcrq, phone)
        conn_mysql.insert_basics(record)


if __name__=='__main__':

    conn_mysql.create()
    # for i in range(2, 5):
    #     url = "https://www.tianyancha.com/search/p" + str(i) + ""
    url = "https://www.tianyancha.com/search/p5"
    driver = driver_open()
    # if get_status(url):
    soup = get_content(driver, url)
    print('----获取基础信息----')
    get_basic_info(soup)
    print('----基础信息结束----')
