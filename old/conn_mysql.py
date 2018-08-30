import pymysql


def create():

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """CREATE TABLE if not exists `corp_basics` (
            `id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
            `website` VARCHAR(255) DEFAULT NULL,
            `status` VARCHAR(10) DEFAULT NULL,
            `location` VARCHAR(20) DEFAULT NULL,
            `legal_person` VARCHAR(50) NOT NULL,
            `regist_fund` VARCHAR(50) DEFAULT NULL,
            `regist_time` VARCHAR(50) DEFAULT NULL,
            `phone` VARCHAR(20) DEFAULT NULL,
            PRIMARY KEY (`id`),
            CONSTRAINT MY_CONST UNIQUE (`website`)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8
            """
    cur.execute(sql)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def insert_basics(table):

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """INSERT INTO corp_basics (
          `website`, `status`, `location`, `legal_person`,
          `regist_fund`, `regist_time`, `phone`)VALUES (
          '%s', '%s', '%s', '%s','%s', '%s', '%s')"""
    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def get_url():

    # 注意数据表设计的时候id是整数还是字符串，其他字段的字符串类型需要选择utf8
    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "select * from corp_basics"
    cur.execute(sql)
    results = cur.fetchall()
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    return results


def create_detail():

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """CREATE TABLE if not exists `Corp` (
            `id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
            `corpName` VARCHAR(255) NOT NULL,
            `tel` VARCHAR(50) DEFAULT NULL,
            `email` VARCHAR(50) DEFAULT NULL,
            `webUrl` VARCHAR(50) DEFAULT NULL,
            `belongDistOrg` VARCHAR(255) NOT NULL,
            `openManName` VARCHAR(50) NOT NULL,
            `regCapi` VARCHAR(20) DEFAULT NULL,
            `startDate` VARCHAR(20) DEFAULT NULL,
            `corpStatus` VARCHAR(10) DEFAULT NULL,
            `uniScid` VARCHAR(50) DEFAULT NULL,
            `orgInstCode` VARCHAR(50) DEFAULT NULL,
            `regNo` VARCHAR(50) DEFAULT NULL,
            `econKind` VARCHAR(50) DEFAULT NULL,
            `taxpayNum` VARCHAR(50) DEFAULT NULL,
            `belongTrade` VARCHAR(50) DEFAULT NULL,
            `fareTermStart` VARCHAR(20) DEFAULT NULL,
            `fareTermEnd` VARCHAR(20) DEFAULT NULL,
            `checkDate` VARCHAR(20) DEFAULT NULL,
            `belongOrg` VARCHAR(50) DEFAULT NULL,
            `englishName` VARCHAR(255) NOT NULL,
            `addr` VARCHAR(255) NOT NULL,
            `fareScope` VARCHAR(1000) NOT NULL,
            PRIMARY KEY (`id`)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8
            """
    cur.execute(sql)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()


def insert_detail(table):

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """INSERT INTO Corp (
          `corpName`, `tel`, `email`, `webUrl`, `belongDistOrg`, `openManName`, `regCapi`, `startDate`,
          `corpStatus`, `uniScid`, `orgInstCode`, `regNo`, `econKind`, `taxpayNum`, `belongTrade`, `fareTermStart`,
          `fareTermEnd`, `checkDate`, `belongOrg`, `englishName`, `addr`, `fareScope`)VALUES (
          '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s','%s', '%s',
          '%s', '%s', '%s', '%s')"""
    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    last_id = cur.lastrowid
    return last_id


def create_fztable():

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """CREATE TABLE if not exists `CorpDist` (
            `id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
            `corp_id` INT(10) unsigned NOT NULL,
            `legal_person` VARCHAR(50) NOT NULL,
            `status` VARCHAR(10) DEFAULT NULL,
            `startDate` VARCHAR(20) DEFAULT NULL,
            PRIMARY KEY (`id`)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8
            """

    cur.execute(sql)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def insert_fztable(table):

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """INSERT INTO CorpDist (
          `corp_id`, `legal_person`, `status`, `startDate`)VALUES ('%s', '%s', '%s', '%s')"""
    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    last_id = cur.lastrowid
    return last_id


def create_gdtable():

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """CREATE TABLE if not exists `CorpStock` (
            `id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
            `corp_id` INT(10) unsigned NOT NULL,
            `rate` VARCHAR(10) NOT NULL,
            `stockCapi` VARCHAR(20) DEFAULT NULL,
            `stockDate` VARCHAR(20) DEFAULT NULL,
            PRIMARY KEY (`id`)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8
            """

    cur.execute(sql)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def insert_gdtable(table):

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    print(table)
    sql = """INSERT INTO CorpStock (
          `corp_id`, `rate`, `stockCapi`, `stockDate`)VALUES ('%s', '%s', '%s', '%s')"""
    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    last_id = cur.lastrowid
    return last_id


def create_ggtable():

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """CREATE TABLE if not exists `CorpPertains` (
            `id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
            `corp_id` INT(10) unsigned NOT NULL,
            `personName` VARCHAR(50) NOT NULL,
            `personType` VARCHAR(50) DEFAULT NULL,
            PRIMARY KEY (`id`)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8
            """

    cur.execute(sql)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def insert_ggtable(table):

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """INSERT INTO CorpPertains (
          `corp_id`, `personName`, `personType`)VALUES ('%s', '%s', '%s')"""

    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    last_id = cur.lastrowid
    return last_id


def create_tztable():

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """CREATE TABLE if not exists `CorpPertains` (
            `id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
            `corp_id` INT(10) unsigned NOT NULL,
            `personName` VARCHAR(50) NOT NULL,
            `personType` VARCHAR(50) DEFAULT NULL,
            PRIMARY KEY (`id`)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8
            """

    cur.execute(sql)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def insert_tztable(table):

    conn = pymysql.connect(host='47.95.115.25',
                           user='root',
                           passwd='lzc@lzc15295909065',
                           db='tianyancha',
                           port=3306,
                           charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = """INSERT INTO CorpPertains (
          `corp_id`, `personName`, `personType`)VALUES ('%s', '%s', '%s')"""

    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    last_id = cur.lastrowid
    return last_id
