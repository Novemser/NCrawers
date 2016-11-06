# coding=utf-8
import urllib2
import urllib
__author__ = 'Novemser'

url = 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
values = {"username": "2072806652@qq.com", "password": "a19951106"}
request = urllib2.Request(url, urllib.urlencode(values))
response = urllib2.urlopen(request)
print response.read()