import requests
from bs4 import BeautifulSoup
__author__ = 'Novemser'

responce = requests.get("http://4m3.tongji.edu.cn/eams/index.action")
soup = BeautifulSoup(responce.text, "html.parser")

print(soup.prettify())