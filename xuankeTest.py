# coding=utf-8
__author__ = 'Novemser'

URL_BASE = "http://xuanke.tongji.edu.cn/"
URL_CheckImage = "CheckImage"
URL_LOGIN = "http://tjis2.tongji.edu.cn:58080/amserver/UI/Login"
URL_MAIN = "http://xuanke.tongji.edu.cn/tj_login/index_main.jsp"
URL_TEST = "http://xuanke.tongji.edu.cn/tj_xuankexjgl/score/query/student/cjcx.jsp"
URL_FRAME = 'http://xuanke.tongji.edu.cn/tj_login/frame.jsp'
URL_TOP = 'http://xuanke.tongji.edu.cn/tj_login/top.jsp'
URL_INFO_LEFT = 'http://xuanke.tongji.edu.cn/tj_login/info_left.jsp'
URL_INFO = 'http://xuanke.tongji.edu.cn/tj_login/info.jsp'
URL_LOGIN_TREE = 'http://xuanke.tongji.edu.cn/tj_login/loginTree.jsp'
URL_INDEX_MAIN = 'http://xuanke.tongji.edu.cn/tj_login/index_main.jsp'
URL_BOTTON = 'http://xuanke.tongji.edu.cn/tj_login/bottom.jsp'
URL_INDEX_JSP = 'http://xuanke.tongji.edu.cn/index.jsp'

import urllib
import urllib2
import cookielib
from time import sleep
from bs4 import BeautifulSoup

cookie = cookielib.MozillaCookieJar()
operner = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(operner)


def addHeaderForReq(request, referer):
    request.add_header("Host", "xuanke.tongji.edu.cn")
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    request.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    request.add_header("Accept-Encoding", "gzip, deflate")
    request.add_header("Referer", referer)
    request.add_header("Connection", "keep-alive")


# 下载验证图片
request = urllib2.Request(URL_BASE + URL_CheckImage)
result = operner.open(request)
try:
    out = open('checkCode.jpg', 'wb')
    out.write(result.read())
    out.flush()
    out.close()
    print 'get code success'
except IOError:
    print 'file wrong'

# 输入验证图片
img_code = raw_input("please input code: ")
print 'your code is %s' % img_code

# 第一步 提交登陆表单
value = {"Login.Token1": "1452681",
         "Login.Token2": "a20131002",
         "T3": img_code,
         "goto": "http://xuanke.tongji.edu.cn/pass.jsp?checkCode=" + img_code,
         "gotoOnFail": "http://xuanke.tongji.edu.cn/deny.jsp?checkCode=" + img_code + "&account=1452681&password=BED0648254DF3D9BA9350683817275CE"}

postData = urllib.urlencode(value)
request_login = urllib2.Request(URL_LOGIN, postData)
result_login = operner.open(request_login)

# 第二步 pass?checkCode
checkUrl = 'http://xuanke.tongji.edu.cn/pass.jsp?checkCode=' + img_code
print checkUrl
request_checkCode = urllib2.Request(checkUrl)
addHeaderForReq(request_checkCode, URL_INDEX_JSP)
# 打印header的每一项
# print request_checkCode.header_items()
result_checkCode = operner.open(request_checkCode)
print request_checkCode.read()
# result = urllib2.urlopen(URL_MAIN)
# result = urllib2.urlopen(URL_TEST)

# print result.read()
