# coding=utf-8
__author__ = 'Novemser'

import urllib
import urllib2
import cookielib
import re
from time import sleep
from bs4 import BeautifulSoup

s1 = 'http://4m3.tongji.edu.cn/eams/samlCheck'

loginUrl_v2 = 'https://ids.tongji.edu.cn:8443/nidp/saml2/sso?sid=0&sid=0'

loginUrl_step2 = 'https://ids.tongji.edu.cn:8443/nidp/saml2/sso?sid=0'

mainPageUrl = 'http://4m3.tongji.edu.cn/eams/home.action'
cardInfoMain = 'http://urp.tongji.edu.cn/index.portal'

cardInfo_userInfoService = 'http://urp.tongji.edu.cn/index.portal?.pn=p84'
cardInfo_page = 'http://urp.tongji.edu.cn/index.portal?.pn=p84_p468_p469'

CARD_DETAIL = "http://urp.tongji.edu.cn/index.portal?.p=Znxjb20ud2lzY29tLnBvcnRhbC5zaXRlLnYyLmltcGwuRnJhZ21lbnRXaW5kb3d8ZjEwODJ8dmlld3xub3JtYWx8YWN0aW9uPXBlcnNvbmFsU2FsYXJ5UXVlcnk_"

# urlTest1
# 欢迎信息 eg:欢迎使用教务系统,今天是2015-10-1,本周是2015-2016学年1学期  第3周
# 系统公告的各种标题
urlTest1 = 'http://4m3.tongji.edu.cn/eams/home!welcome.action'

# urlTest2
# 左侧子菜单 eg:个人选课,本研互选
urlTest2 = 'http://4m3.tongji.edu.cn/eams/home!submenus.action?menu.id=menu_panel'

# urlTest3
# 课表菜单
urlTest3 = 'http://4m3.tongji.edu.cn/eams/courseTableForStd.action'

# urlTest4
# 课表
urlTest4 = 'http://4m3.tongji.edu.cn/eams/courseTableForStd!courseTable.action'

cookie = cookielib.LWPCookieJar()
operner = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(operner)

# 有两种表单格式
# 第一种是4m3上的
value = {'goto': 'http://4m3.tongji.edu.cn:80/eams/home.action',
         'gotoOnFail': 'http://4m3.tongji.edu.cn:80/eams/login.action?error=1&username=333&password=37693cfc748049e45d87b8c7d8b9aacd',
         'Login.Token1': '1452681',  # 学号
         'Login.Token2': 'a20131002',  # 密码
         'session_locale': 'zh_CN',
         'submitBtn': '登陆'}

# 第二种是一体化认证系统上的
# 两种都可以使用
# 替换成自己的用户名和密码即可
value_v2 = {'IDToken0': '',
            'IDToken1': '1452681',
            'IDToken2': 'a20131002',
            'goto': 'null',
            'IDButton': '登陆',
            'gx_charset': 'UTF-8'}

value_v3 = {
    "option":"credential",
    "Ecom_User_ID":"1452681",
    "Ecom_Password":"a20131002",
    "submit":"登录"
}

# 选课网似乎没有设置验证headers
# 所以headers可以不管
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Referer': 'http://4m3.tongji.edu.cn/eams/login.action',
    'Origin': 'http://4m3.tongji.edu.cn',
    'Host': 'tjis2.tongji.edu.cn:58080'}

# 对表单进行编码
postData = urllib.urlencode(value_v3)
# 提交请求
req = urllib2.Request(loginUrl_v2, postData)

# 伪造UA，referer
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')

result = operner.open(s1)

soup = BeautifulSoup(result.read(), "lxml")

s2 = soup.meta.attrs['content'][6:]


result = operner.open(s2)

soup = BeautifulSoup(result.read(), "lxml")

s3 = 'https://ids.tongji.edu.cn:8443' + soup.form.attrs['action']

result = operner.open(s3)

soup = BeautifulSoup(result.read(), "lxml")

s4 = soup.form.attrs['action']

# req.add_header('Referer', s3)
# req.add_header('Host', 'ids.tongji.edu.cn:8443')
result = operner.open(req, postData)

s4text = result.read()
s5 = re.findall('top.location.href=\'(.*?)\'', s4text)[0]

result = operner.open(s5)

soup = BeautifulSoup(result.read(), "lxml")

s6 = soup.form.attrs['action']

SAMLResponse = soup.form.contents[1].attrs['value']
RelayState = soup.form.contents[3].attrs['value']

value = {
    'RelayState': RelayState,
    'SAMLResponse': SAMLResponse
}
postData = urllib.urlencode(value)
req = urllib2.Request(s6, postData)
result = operner.open(req, postData)


print result.read()

# 打印Cookie做测试
# for item in cookie:
#     print item
#

# 现在提取课表信息，其实只需要提交一个表单就可以
# 这个ids号码可以通过分析jQuery得到
# 这里填写的ids是我自己的。。不知道其他账号可以不？（可以

postDataCourseTable = {'ignoreHead': '1',
                       'setting.kind': 'std',
                       'startWeek': '1',
                       'semester.id': '101',
                       'ids': '845951019'}
data = urllib.urlencode(postDataCourseTable)
request = urllib2.Request(urlTest4, data)

# result_2 = operner.open(urlTest2)
# result_3 = operner.open(urlTest3)
result_4 = operner.open(request)

print result_4.read()
# # 强行破解出大家的课表。。。
# for a in range(8, 10):
#     for b in range(5, 10):
#         for c in range(0, 10):
#             for d in range(0, 10):
#                 postDataCourseTable['ids'] = '84594'+str(a)+str(b)+str(c)+str(d)
#                 postData = urllib.urlencode(postDataCourseTable)
#                 req = urllib2.Request(urlTest4, postData)
#                 resultCourse = operner.open(req)
#
#                 # 用BeautifulSoup简单处理一下
#                 soup = BeautifulSoup(resultCourse.read(), "html.parser")
#
#                 print soup.prettify()
#                 sleep(15)

# 查询校园卡
# postData = {"name": "1",
#             "startDate": "2016-01-01",
#             "endDate": "2016-01-23",
#             "submitQuery": "查询"}
#
# data = urllib.urlencode(postData)
# request = urllib2.Request(CARD_DETAIL, data)
# result_card_query = operner.open(request)
#
# print result_card_query.read()