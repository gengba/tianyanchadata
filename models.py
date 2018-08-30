#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Corp:

    def __init__(self, name, pid, person, person_id, status, xydm, addr, reg_org, area, industry, kind,
                 est_date, check_date, reg_capi, reg_id, fare_start, fare_end, fare_scope,
                 tel, website, email, org_inst_id, taxpay_id, staff, eng_name):
        self.name = name
        self.pid = pid  # 指向父公司的id
        self.person = person    # 法定代表人
        self.person_id = person_id    # 法定代表人证件编号
        self.status = status
        self.xydm = xydm
        self.addr = addr
        self.reg_org = reg_org    # 登记机关
        self.area = area
        self.industry = industry
        self.kind = kind
        self.est_date = est_date    # 成立日期
        self.check_date = check_date    # 核准日期
        self.reg_capi = reg_capi    # 注册资本
        self.reg_id = reg_id    # 注册号
        self.fare_start = fare_start
        self.fare_end = fare_end
        self.fare_scope = fare_scope
        self.tel = tel
        self.website = website
        self.email = email
        self.org_inst_id = org_inst_id    # 注册机构代码
        self.taxpay_id = taxpay_id    # 纳税号
        self.staff = staff    # 员工规模
        self.eng_name = eng_name


class Manager:

    def __init__(self, corp_id, name, position, age, gender, start_date, end_date):
        self.corp_id = corp_id
        self.name = name
        self.position = position
        self.age = age
        self.gender = gender
        self.start_date = start_date
        self.end_date = end_date


class Stock:

    def __init__(self, name, corp_id, category, ratio, amount, date):
        self.name = name
        self.corp_id = corp_id
        self.category = category
        self.ratio = ratio
        self.amount = amount
        self.date = date


class Investment:

    def __init__(self, corp_id, corp_name, corp_person, fund, ratio, date, status):
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.corp_person = corp_person
        self.fund = fund
        self.ratio = ratio
        self.date = date
        self.status = status
