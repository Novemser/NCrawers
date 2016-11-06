# coding=utf-8
__author__ = 'Novemser'

import urllib2
from time import sleep

url = "http://jiading.tongji.edu.cn:8080/TJbus/getTicketServlet?username=1452640&get_ticket_time=1445724001945&bus_id=2_6"

while (True):
    responce = urllib2.urlopen(url)
    print responce.read()
    sleep(0.5)