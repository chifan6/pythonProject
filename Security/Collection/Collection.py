import socket, os, sys
import whois


# 查询ip
def ip_check(url):
    ip = socket.gethostbyname_ex(url)
    print(ip)


# 查询whois
def whois_check(url):
    data = whois.whois(url)
    print(data)


if __name__ == '__main__':
    whois_check('qedgw.com')
