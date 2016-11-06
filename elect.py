# coding=utf-8
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

URL_MAIN = 'http://202.120.165.79:8801/default.aspx'
URL_LOCATION = 'http://202.120.165.79:8801/usedRecord.aspx'


def getVIEWSTATE(soup):
    view_input = soup.find(id="__VIEWSTATE")
    return view_input['value']


def getVIEWSTATEGENERATOR(soup):
    event_input = soup.find(id="__VIEWSTATEGENERATOR")
    return event_input['value']


def getRestMoney(soup):
    input = soup.find(class_="number orange")
    return input


def make_query(operner, url, eventTarget, viewstate, viewstategeneratoe, drlouming, drceng, DropDownList1,
               txt_fangjian, radio):
    print drlouming
    print drceng
    body = {
        '__EVENTTARGET': eventTarget,
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': viewstategeneratoe,
        'DropDownList1': DropDownList1,
        'txt_fangjian': txt_fangjian,
        'drlouming': drlouming,
        'drceng': drceng,
        'radio': radio,
        'ImageButton1.x': 65,
        'ImageButton1.y': 16
    }

    request = urllib2.Request(url, urllib.urlencode(body))

    request.add_header('Host', '202.120.165.79:8801')
    request.add_header('Referer', 'http://202.120.165.79:8801/Default.aspx')
    request.add_header('Origin', 'http://202.120.165.79:8801')
    request.add_header('Upgrade-Insecure-Requests', '1')
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')

    response = operner.open(request)
    content = response.read()

    return content


def make_request(operner, url, eventTarget, viewstate, viewstategeneratoe, drlouming, drceng, DropDownList1,
                 txt_fangjian):
    body = {
        '__EVENTTARGET': eventTarget,
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': viewstategeneratoe,
        'DropDownList1': DropDownList1,
        'txt_fangjian': txt_fangjian,
        'drlouming': drlouming,
        'drceng': drceng,
    }

    request = urllib2.Request(url, urllib.urlencode(body))

    request.add_header('Host', '202.120.165.79:8801')
    request.add_header('Referer', 'http://202.120.165.79:8801/Default.aspx')
    request.add_header('Origin', 'http://202.120.165.79:8801')
    request.add_header('Upgrade-Insecure-Requests', '1')
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')

    response = operner.open(request)
    content = response.read()
    soup = BeautifulSoup(content, "lxml")

    viewState = getVIEWSTATE(soup)
    viewstateGenerator = getVIEWSTATEGENERATOR(soup)

    return viewState, viewstateGenerator


cookie = cookielib.LWPCookieJar()
operner = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(operner)

page_main = urllib2.urlopen(URL_MAIN).read()
soup = BeautifulSoup(page_main, "lxml")

viewState = getVIEWSTATE(soup)
viewstategenerator = getVIEWSTATEGENERATOR(soup)

viewState, viewstategenerator = make_request(operner, URL_MAIN, 'drlouming', viewState,
                                                           viewstategenerator, "5", "", "", "")
viewState, viewstategenerator = make_request(operner, URL_MAIN, 'drceng', viewState, viewstategenerator,
                                                           "5", "4834", "", "")
viewState, viewstategenerator = make_request(operner, URL_MAIN, 'DropDownList1', viewState,
                                                           viewstategenerator, "5", "4834", "4845", "")
responseData = make_query(operner, URL_MAIN, '', viewState, viewstategenerator, "5",
                                                           "4834", "4845", "19528", "usedR")

print getRestMoney(BeautifulSoup(responseData, "lxml"))