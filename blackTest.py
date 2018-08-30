#!/usr/bin/python3
# -*- coding:utf-8 -*-
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
from pymongo import MongoClient


valid_corp = ['圣安', '赫品迈', '茗博']
invalid_corp = ['天闻角川', '统一', '大世界']
valid_area = ['北京', '南宁', '北海']
invalid_area = ['西乡塘', '咸宁', '北海道']
valid_person = ['史贝', '余利吉', '陶雷']
invalid_person = ['潘晓', '郭芷柔', '李振成']


# def driver_open():
#
#     new_driver = webdriver.Chrome()
#     return new_driver


def get_page(driver):

    for corp in valid_corp:
        a_file = open("valid_corp_sql.txt", "a")
        query_list = db.corp.find({'name': {'$regex': corp}})
        if query_list is None:
            a_file.write('-------暂无数据-------')
        for query in query_list:
            a_file.write(query['name'])
            a_file.write('\n')
        a_file.close()

        # driver.get('localhost:8080')
        # soup = click_to_search(driver, corp)
        # file = open('valid_corp_web.txt', 'a')
        # test_corp(soup, file)

    for corp in invalid_corp:
        a_file = open("invalid_corp_sql.txt", "a")
        query_list = db.corp.find({'name': {'$regex': corp}})
        if query_list is None:
            a_file.write('-------暂无数据-------')
        for query in query_list:
            a_file.write(query['name'])
            a_file.write('\n')
        a_file.close()

        # driver.get('localhost:8080')
        # soup = click_to_search(driver, corp)
        # file = open('invalid_corp_web.txt', 'a')
        # test_corp(soup, file)

    for area in valid_area:
        a_file = open("valid_area_sql.txt", "a")
        query_list = db.corp.find({'area': {'$regex': area}})
        if query_list is None:
            a_file.write('-------暂无数据-------')
        for query in query_list:
            a_file.write(query['name'] + '>地区：' + query['area'])
            a_file.write('\n')
        a_file.close()

        # driver.get('localhost:8080')
        # driver.find_element_by_class_name('findCity').click()
        # soup = click_to_search(driver, area)
        # file = open('valid_area_web.txt', 'a')
        # test_area(soup, file)

    for area in invalid_area:
        a_file = open("invalid_area_sql.txt", "a")
        query_list = db.corp.find({'area': {'$regex': area}})
        if query_list is None:
            a_file.write('-------暂无数据-------')
        for query in query_list:
            a_file.write(query['name'] + '>地区：' + query['area'])
            a_file.write('\n')
        a_file.close()

        # driver.get('localhost:8080')
        # driver.find_element_by_class_name('findCity').click()
        # soup = click_to_search(driver, area)
        # file = open('invalid_area_web.txt', 'a')
        # test_area(soup, file)

    for person in valid_person:
        a_file = open("valid_person_sql.txt", "a")
        query_list = db.corp.find({"person": {"$regex": person}})
        if query_list is None:
            a_file.write('-------暂无数据-------')
        for query in query_list:
            a_file.write(query['name'] + '>法定代表人：' + query['person'])
            a_file.write('\n')
        a_file.close()

        # driver.get('localhost:8080')
        # driver.find_element_by_class_name('findName').click()
        # soup = click_to_search(driver, person)
        # file = open('valid_person_web.txt', 'a')
        # test_person(soup, file)

    for person in invalid_person:
        a_file = open("invalid_person_sql.txt", "a")
        query_list = db.corp.find({'person': {'$regex': person}})
        if query_list is None:
            a_file.write('-------暂无数据-------')
        for query in query_list:
            a_file.write(query['name'] + '>法定代表人：' + query['person'])
            a_file.write('\n')
        a_file.close()

        # driver.get('localhost:8080')
        # driver.find_element_by_class_name('findName').click()
        # soup = click_to_search(driver, person)
        # file = open('invalid_person_web.txt', 'a')
        # test_person(soup, file)


# def click_to_search(driver, key):
#
#     driver.find_element_by_class_name('findParam').send_keys(key)
#     driver.find_element_by_class_name('findOkBtn').click()
#     driver.switch_to_window(driver.window_handles[1])
#     content = driver.page_source.encode('utf-8')
#     soup = BeautifulSoup(content, 'lxml')
#     return soup


# def test_corp(soup, file):
#
#     try:
#         basics = soup.find(name='div', attrs={'class': 'list-group'}).findAll('a')
#         for basic in basics:
#             print('aaa', basic)
#             data = str(basic.get_text())
#             file.write(data)
#             file.write('\n')
#     except:
#         file.write('--------暂无数据---------')
#     file.close()
#
#
# def test_person(soup, file):
#
#     try:
#         basics = soup.find(name='div', attrs={'class': 'list-group'}).findAll('a')
#         for basic in basics:
#             data = str(basic.get_text())
#             file.write(data)
#             file.write('\n')
#     except:
#         file.write('--------暂无数据---------')
#     file.close()
#
#
# def test_area(soup, file):
#
#     try:
#         basics = soup.find(name='div', attrs={'class': 'list-group'}).findAll('a')
#         for basic in basics:
#             data = str(basic.get_text())
#             file.write(data)
#             file.write('\n')
#     except:
#         file.write('--------暂无数据---------')
#     file.close()

if __name__ == '__main__':

    conn = MongoClient('47.104.225.166', 27017)
    db = conn.qiyexinxi  # 连接mydb数据库，没有则自动创建
    # driver = driver_open()
    # get_page(driver)
    # driver.close()
