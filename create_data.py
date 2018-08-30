#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random
from models import *
from pymongo import MongoClient
from decimal import Decimal


status_list = ['续存', '在业', '吊销', '注销', '迁出', '迁入'  '停业', '清算']
surnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱',
            '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢',
            '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌',
            '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛',
            '雷', '贺', '倪', '汤', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞',
            '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '姚', '邵', '湛', '汪',
            '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '成', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项',
            '祝', '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '贾', '路', '娄', '危', '江', '颜', '郭',
            '梅', '盛', '林', '刁', '钟', '徐', '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞',
            '万', '支', '柯', '管', '卢', '莫', '经', '房', '裘', '关', '蒯', '相', '查', '後', '荆', '红', '游',
            '竺', '权', '逯', '盖', '公', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方']
industry_list = ['保险业', '采矿', '能源', '餐饮', '宾馆', '电讯业', '房地产', '服务', '服装业', '公益组织', '广告业',
                 '航空航天', '化学', '健康', '保健', '建筑业', '教育', '培训', '计算机', '金属冶炼', '警察', '消防',
                 '会计', '美容', '媒体', '出版', '木材', '造纸', '零售', '批发', '农业', '旅游业', '司法', '律师',
                 '司机', '体育运动', '演艺', '医疗服务', '艺术', '设计', '银行', '金融', '因特网', '音乐舞蹈', '邮政快递',
                 '运输业', '政府机关', '机械制造', '咨询']
kind_list = ['国有', '私营', '股份制', '有限责任']
position_list = ['董事', '副总经理', '总工程师', '总监', '总经济师', '财务总监']


def corp_name():

    province_list = []
    chars = open('cities.txt', encoding='utf8')
    for line in chars:
        province_list.append(line.strip('\n'))
    random_province = random.sample(province_list, 1)[0]
    province = random_province[0:random_province.find(':')]

    name = create_name()
    pid = '0'
    person = create_person_name()

    person_id = ''
    for i in range(9):
        person_id += str(random.randint(0, 9))

    status = random.sample(status_list, 1)[0]

    char_list = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
    num_list = [str(i) for i in range(10)]
    xydm = ''.join(random.sample(num_list, 8) + random.sample(char_list, 7) + random.sample(num_list, 3))
    addr = province + '中华路财富大厦c栋1101'
    reg_org = province + '工商局'
    area = province
    industry = random.sample(industry_list, 1)[0]
    kind = random.sample(kind_list, 1)[0]
    est_date = '1999-08-10'
    check_date = '1999-10-08'
    reg_capi = str(random.randint(10, 99999))
    reg_id = xydm
    fare_start = '1999-10-10'
    fare_end = '2056-10-10'
    fare_scope = '经营范围经营范围经营范围'
    tel = '020-3854226'
    website = 'www$web$com'
    email = 'email@corp$com'
    org_inst_id = xydm
    taxpay_id = xydm
    staff = str(random.randint(10, 2000))
    eng_name = 'corpEnglishName'

    corp = Corp(name, pid, person, person_id, status, xydm, addr, reg_org, area, industry, kind,
                est_date, check_date, reg_capi, reg_id, fare_start, fare_end, fare_scope,
                tel, website, email, org_inst_id, taxpay_id, staff, eng_name)

    cid = db.corp.insert({
        "name": province + corp.name,
        "pid": corp.pid,
        "person": corp.person,
        "status": corp.status,
        "xydm": corp.xydm,
        "addr": corp.addr,
        "reg_org": corp.reg_org,
        "area": corp.area,
        "industry": corp.industry,
        "kind": corp.kind,
        "est_date": corp.est_date,
        "check_date": corp.check_date,
        "reg_capi": corp.reg_capi,
        "reg_id": corp.reg_id,
        "fare_start": corp.fare_start,
        "fare_end": corp.fare_end,
        "fare_scope": corp.fare_scope,
        "tel": corp.tel,
        "website": corp.website,
        "email": corp.email,
        "org_inst_id": corp.org_inst_id,
        "taxpay_id": corp.taxpay_id,
        "staff": corp.staff,
        "eng_name": corp.eng_name
    })
    print("------corpOK-------")

    create_manager(corp, cid)
    create_stock(corp, cid)

    cities = random_province[random_province.find(':') + 1:]
    if cities:
        city_list = cities.split(',')
        create_dist(city_list, corp, cid)


def create_dist(city_list, pcorp, pid):

    dist_num = random.randint(0, 5)
    cities = random.sample(city_list, dist_num)
    for city in cities:
        name = pcorp.name
        pid = pid
        person = pcorp.person
        person_id = pcorp.person_id
        status = random.sample(status_list, 1)[0]

        char_list = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
        num_list = [str(i) for i in range(10)]
        xydm = ''.join(random.sample(num_list, 8) + random.sample(char_list, 7) + random.sample(num_list, 3))

        addr = city + '中华路财富大厦c栋1101'
        reg_org = city + '工商局'
        area = pcorp.area
        industry = random.sample(industry_list, 1)[0]
        kind = random.sample(kind_list, 1)[0]
        est_date = '1999-08-10'
        check_date = '1999-10-08'
        reg_capi = str(random.randint(10, 29999))
        reg_id = xydm
        fare_start = '1999-10-10'
        fare_end = '2056-10-10'
        fare_scope = '经营范围经营范围经营范围'
        tel = '020-3854226'
        website = 'www$web$com'
        email = 'email@corp$com'
        org_inst_id = xydm
        taxpay_id = xydm
        staff = str(random.randint(10, 2000))
        eng_name = 'corpEnglishName'

        corp = Corp(name, pid, person, person_id, status, xydm, addr, reg_org, area, industry, kind,
                    est_date, check_date, reg_capi, reg_id, fare_start, fare_end, fare_scope,
                    tel, website, email, org_inst_id, taxpay_id, staff, eng_name)

        cid = db.corp.insert({
            "name": city + corp.name,
            "pid": corp.pid,
            "person": corp.person,
            "status": corp.status,
            "xydm": corp.xydm,
            "addr": corp.addr,
            "reg_org": corp.reg_org,
            "area": corp.area,
            "industry": corp.industry,
            "kind": corp.kind,
            "est_date": corp.est_date,
            "check_date": corp.check_date,
            "reg_capi": corp.reg_capi,
            "reg_id": corp.reg_id,
            "fare_start": corp.fare_start,
            "fare_end": corp.fare_end,
            "fare_scope": corp.fare_scope,
            "tel": corp.tel,
            "website": corp.website,
            "email": corp.email,
            "org_inst_id": corp.org_inst_id,
            "taxpay_id": corp.taxpay_id,
            "staff": corp.staff,
            "eng_name": corp.eng_name
        })
        print("------distOK-------")
        create_manager(corp, cid)
        create_stock(corp, cid)


def create_manager(corp, pid):

    manager_list = []
    legal_person = Manager(
        pid, corp.person, '总经理', str(random.randint(25, 56)), random.sample(['男', '女'], 1)[0], corp.fare_start, '')
    manager_list.append(legal_person)
    for i in range(random.randint(0, 5)):
        corp_id = pid   # 存入db后取最新记录ID
        position = random.sample(position_list, 1)[0]
        age = str(random.randint(25, 65))
        gender = random.sample(['男', '女'], 1)[0]
        manager_list.append(Manager(corp_id, create_person_name(), position, age, gender, corp.fare_start, ''))
    for manager in manager_list:
        db.corpManager.insert_one({
            "corp_id": manager.corp_id,
            "name": manager.name,
            "position": manager.position,
            "age": manager.age,
            "gender": manager.gender,
            "start_date": manager.start_date,
            "end_date": manager.end_date
        })
    print("------managerOK-------")


def create_stock(corp, corp_id):

    stock_list = []
    if corp.pid == '0':
        stock_list.append(
            Stock(create_person_name(), corp_id, '0', '55.00', str(int(corp.reg_capi)*0.55), corp.est_date))
    else:
        pcorp = db.corp.find_one({"_id": corp.pid})
        stock_list.append(Stock(pcorp['name'], corp_id, '1', '55.00', str(int(corp.reg_capi)*0.55), corp.est_date))
    stock_num = random.randint(1, 5)
    stock_sum = Decimal(str(45/stock_num)).quantize(Decimal('0.00'))
    for i in range(stock_num):
        stock_list.append(
            Stock(
                create_person_name(),
                corp_id,
                '0',
                str(stock_sum),
                str(int(corp.reg_capi)*stock_sum/100),
                corp.est_date
            )
        )
    for stock in stock_list:
        db.corpStock.insert({
            "name": stock.name,
            "corp_id": stock.corp_id,
            "category": stock.category,
            "ratio": stock.ratio,
            "amount": stock.amount,
            "date": stock.date
        })
        print("------stockOK-------")


def create_name():

    char_list = []
    chars = open('characters.txt', encoding='utf8')
    for line in chars:
        for char in line:
            if char == '':
                pass
            else:
                char_list.append(char)
    name_len = random.randint(2, 4)
    random_name = random.sample(char_list, name_len)
    value = ''
    for s in random_name:
        value += s
    names = value + '有限公司'

    return names


def create_person_name():

    word_list = []
    chars = open('characters.txt', encoding='utf8')
    for line in chars:
        for char in line:
            if char == '':
                pass
            else:
                word_list.append(char)
    random_name = random.sample(word_list, random.randint(1, 2))
    value = ''
    for s in random_name:
        value += s
    name = random.sample(surnames, 1)[0] + value

    return name


if __name__ == '__main__':

    conn = MongoClient('127.0.0.1', 27017)
    db = conn.qiyexinxi  # 连接mydb数据库，没有则自动创建
    corp_name()
