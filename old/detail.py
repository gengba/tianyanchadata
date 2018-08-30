#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver

from old import conn_mysql


def driver_open():

    driver = webdriver.Chrome()
    return driver


def get_content(driver, url):

    driver.get(url)
    content = driver.page_source.encode('utf-8')
    driver.close()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    return soup


def get_basic_info(soup, row):

    company = soup.select('div.position-rel > h1')[0].get_text()
    print(u'公司名称：'+company)
    basics = soup.find(
        name='div', attrs={'class': 'company_header_interior'}).findAll(
        name='div', attrs={'class': 'sec-c2'})
    phone = str(basics[0].findAll('div')[0].findAll('span')[1].get_text())
    print(u'电话:' + phone)
    email = str(basics[0].findAll('div')[1].findAll('span')[1].get_text())
    print(u'邮箱:' + email)
    try:
        website = str(basics[1].find('a').get_text())
    except:
        website = ''
    print(u'网址:' + website)
    fddbr = str(row[4])
    print(u'法定代表人：'+fddbr)
    zczb = is_digital(row[5])
    print(u'注册资本：'+zczb + u'万元')
    zcrq = row[6]
    print(u'注册时间：'+zcrq)
    zt = str(row[2])
    print(u'公司状态：'+zt)
    table2 = soup.findAll('table')[1]
    rowst = table2.find('tbody').findAll('tr')
    qyzch = rowst[0].findAll('td')[1].get_text()
    print(u'工商注册号:' + qyzch)
    zzjgdm = rowst[0].findAll('td')[3].get_text()
    print(u'注册机构代码:' + zzjgdm)
    tyxydm = rowst[1].findAll('td')[1].get_text()
    print(u'统一信用代码:' + tyxydm)
    qylx = rowst[1].findAll('td')[3].get_text()
    print(u'企业类型:' + qylx)
    nsrsbh = rowst[2].findAll('td')[1].get_text()
    print(u'纳税人识别号:' + nsrsbh)
    hy = rowst[2].findAll('td')[3].get_text()
    print(u'行业:' + hy)
    yyqx = is_date(rowst[3].findAll('td')[1].find(text=True))
    print(u'经营期限（起）:' + yyqx[0])
    print(u'经营期限（止）:' + yyqx[1])
    hzrq = is_date(rowst[3].findAll('td')[3].find(text=True))
    print(u'核准日期:' + hzrq[1])
    djjg = rowst[4].findAll('td')[1].get_text()
    print(u'登记机构：'+djjg)
    ywmc = rowst[4].findAll('td')[3].get_text()
    print(u'英文名称:' + ywmc)
    zcdz = str(rowst[5].findAll('td')[1].find(text=True))
    print(u'注册地址：' + zcdz)
    jyfw = str(rowst[6].findAll('td')[1].find(text=True))
    print(u'经营范围：' + jyfw)
    record = (company, phone, email, website, row[3], fddbr, zczb, zcrq, zt, qyzch,
              zzjgdm, tyxydm, qylx, nsrsbh, hy, yyqx[0], yyqx[1], hzrq[1],
              djjg, ywmc, zcdz, jyfw)
    return conn_mysql.insert_detail(record)


def get_gg_info(soup, id):

    ggtable = soup.findAll('table')[2]
    gg_head = ggtable.find('thead').find('tr').findAll('th')[1].get_text()
    if gg_head != '主要人员':
        return
    person_rows = ggtable.find('tbody').findAll('tr')
    for person in person_rows:
        name = str(person.findAll('td')[1].find(text=True))
        position = ''
        positions = person.findAll('td')[2].findAll('span')
        for pos in positions:
            position += str(pos.get_text())
        print(name + ':' + position)
        record = (id, name, position)
        conn_mysql.insert_ggtable(record)


def get_gd_info(soup, id):

    gdtable = soup.findAll('table')[3]
    gd_head = gdtable.find('thead').find('tr').findAll('th')[1].get_text()
    if gd_head != '股东':
        return
    gd_rows = gdtable.find('tbody').findAll('tr')
    for gd in gd_rows:
        name = gd.findAll('td')[1].find(text=True)
        rate = is_digital(gd.findAll('td')[2].find(text=True))
        count = is_digital(gd.findAll('td')[3].find(text=True))
        date = gd.findAll('td')[4].find(text=True)
        print(name + ':' + rate + ':' + count + ':' + date)
        record = (id, name, rate, count, date)
        conn_mysql.insert_gdtable(record)


# def get_tz_info(soup, id):
#
#     tztable = soup.findAll('table')[4]
#     tz_rows = tztable.find('tbody').findAll('tr')
#     for tz in tz_rows:
#         corp = str(tz.findAll('td')[1].find(text=True))
#         person = str(tz.findAll('td')[2].find(text=True))
#         fund = str(is_digital(tz.findAll('td')[3].find(text=True)))
#         rate = str(is_digital(tz.findAll('td')[4].find(text=True)))
#         date = str(tz.findAll('td')[5].find(text=True))
#         status = str(tz.findAll('td')[6].find(text=True))
#         print(corp + '' + person + '' + fund + '' + rate + '' + date + '' + status)
        # record = (corp, person, fund, rate, date, status)
        # conn_mysql.insert_tztable(record)


def get_fz_info(soup, id):

    try:
        fztable = soup.findAll('table')[6]
    except:
        return
    print('111')
    fz_head = fztable.find('thead').find('tr').findAll('th')[1].get_text()
    if fz_head != '企业名称':
        return
    fz_rows = fztable.find('tbody').findAll('tr')
    for fz in fz_rows:
        name = str(fz.findAll('td')[1].find('a').find('span').get_text())
        person = str(fz.findAll('td')[2].find(text=True))
        date = str(fz.findAll('td')[3].find(text=True))
        status = str(fz.findAll('td')[4].find('span').get_text())
        print(name + '' + person + '' + date + '' + status)
        record = (id, name, person, date, status)
        conn_mysql.insert_fztable(record)


def is_digital(data):

    result = ''
    for s in data:
        if s.isdigit() or s == '.':
            result += s
    return result


def is_date(data):

    result = ''
    start_date = ''
    for s in data:
        if s == '至':
            start_date = result
            result = ''
        result += s
    return (start_date, result)

if __name__ == '__main__':

    conn_mysql.create_detail()
    conn_mysql.create_ggtable()
    conn_mysql.create_gdtable()
    conn_mysql.create_fztable()
    for row in conn_mysql.get_url():
        url = row[1]
        driver = driver_open()
        soup = get_content(driver, url)
        print('----获取基础信息----')
        last_id = get_basic_info(soup, row)
        print('----获取高管信息----')
        get_gg_info(soup, last_id)
        print('----获取股东信息----')
        get_gd_info(soup, last_id)
        # print('----获取对外投资信息----')
        # get_tz_info(soup, last_id)
        print('----获取分支机构信息----')
        get_fz_info(soup, last_id)
