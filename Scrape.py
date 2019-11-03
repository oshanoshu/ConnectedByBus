import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome("C://Users//bisha//Documents//chromedriver_win32//chromedriver.exe")
driver.get("https://us.megabus.com/stops")

content = driver.page_source
soup = BeautifulSoup(content,"html.parser")

CityDict ={}
CityArr=[]
CityIDArr=[]
all_tags = soup.find_all('a', attrs={'data-parent': "#accordion"})
for tag in all_tags:
    CityArr.append(tag.string.strip())


all_CityIds = soup.find_all('ul', attrs={'class':"list-unstyled"})

for item in all_CityIds:
    listVal = item.find_all('a')
    str = listVal[0]['onclick']
    arr = str.split('(')
    idArr = re.findall("'(\w+)'",arr[1])
    id = idArr[0]
    CityIDArr.append(id)

for city, id in zip(CityArr, CityIDArr):
    CityDict[city] = id


file = open("CityDict.txt", "a")
file.write(CityDict.__str__())
file.close()
