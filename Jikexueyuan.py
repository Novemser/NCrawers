# coding=utf-8

import urllib2
import urllib
import cookielib
__author__ = 'Novemser'

loginurl = 'http://www.renren.com'
logindomain = 'renren.com'

# url = 'http://www.jikexueyuan.com/course/'
# html = urllib2.urlopen(url)

class Login(object):
    def __init__(self):
        self.name = ''
        self.password = ''
        self.domain = ''

        self.cookieJar = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self, username, password, domain):
        '''设置用户信息'''
        self.name = username
        self.password = password
        self.domain = domain

    def login(self):
        '''登陆网站'''
        loginParam = {'domain': self.domain, 'email': self.name, 'password': self.password}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        req = urllib2.Request(loginurl, urllib.urlencode(loginParam), headers)

        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()

if __name__ == '__main__':
    userlogin = Login()
    username = 'username'
    password = 'password'
    domain = logindomain
    userlogin.setLoginInfo(username, password, domain)
    userlogin.login()