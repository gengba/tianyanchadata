#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pymongo import MongoClient


valid_corp = ['圣安', '赫品迈', '茗博', '天闻角川']
valid_area = ['山西', '广西', '咸宁', '北海道']
valid_person = ['史贝', '余利吉', '陶雷', '潘晓', '郭芷柔', '李振成']


def get_data():

    # a_file = open("valid_corp_sql.txt", "a")
    # for corp in valid_corp:
    #     query_list = db.corp.find({'name': {'$regex': corp}})
    #     if query_list is None:
    #         a_file.write('-------暂无数据-------')
    #     for query in query_list:
    #         a_file.write(query['name'])
    #         a_file.write('\n')
    #         print('-----valid_corp_sql.txt write OK!\n')
    # a_file.close()

    a_file = open("valid_area_sql.txt", "a")
    for area in valid_area:
        query_list = db.corp.find({'area': {'$regex': area}})
        if query_list is None:
            a_file.write('-------暂无数据-------')
        for query in query_list:
            a_file.write(query['name'] + '>地区：' + query['area'])
            a_file.write('\n')
            print('-----valid_area_sql.txt write OK!\n')
    a_file.close()

    # a_file = open("valid_person_sql.txt", "a")
    # for person in valid_person:
    #     query_list = db.corp.find({"person": {"$regex": person}})
    #     if query_list is None:
    #         a_file.write('-------暂无数据-------')
    #     for query in query_list:
    #         a_file.write(query['name'] + '>法定代表人：' + query['person'])
    #         a_file.write('\n')
    #         print('-----valid_person_sql.txt write OK!\n')
    # a_file.close()

if __name__ == '__main__':

    conn = MongoClient('47.104.225.166', 27017)
    db = conn.qiyexinxi  # 连接mydb数据库，没有则自动创建
    get_data()
    print('-----All write OK!------')
    conn.close()
