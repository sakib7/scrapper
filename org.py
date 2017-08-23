# -*- coding: utf-8 -*-
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import xlrd
import xlwt

csvpath = r"C:\Users\sakib\Desktop\python\data.xls"
book = xlrd.open_workbook(csvpath)
sheet = book.sheet_by_name("2017")

# my_url = 'https://summerofcode.withgoogle.com/organizations/6116707350347776/'
# my_url = 'https://summerofcode.withgoogle.com/organizations/4800434830049280/'
# my_url = 'https://summerofcode.withgoogle.com/organizations/'
my_url = 'https://www.iplocation.net/'


def loadFullPage(browser,pause):
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
        time.sleep(pause)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
    return browser

chromePath = r"C:\Users\sakib\Desktop\python\chromedriver_win32\chromedriver.exe"

PROXY = "66.85.19.190:65309" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chromePath,chrome_options=chrome_options)

chrome.get(my_url)
exit(0)
names = []
url_list = []
for x in range(0,201):
    url_list.append(sheet.cell(x,1).value)
    names.append(sheet.cell(x,0).value)

csvpath = r"C:\Users\sakib\Desktop\python\datawrite.xls"
book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("Orgs2017")
row = 0
for name,url in zip(names,url_list):
    chrome.get(url)
    loadFullPage(chrome, 3)
    projects = chrome.find_elements_by_class_name("project-card__right-header-content")
    count = len(projects)
    print(row, name, url, count)
    sheet.write(row, 0, name)
    sheet.write(row, 1, url)
    sheet.write(row, 2, count)
    row += 1
book.save(csvpath)



# x = 0
# row = 0
# freq = []
# for link in url_list:
#     my_url = link
#     chrome.get(my_url)
#     loadFullPage(chrome, 3)
#     projects = chrome.find_elements_by_class_name("project-card__right-header-content")
#     x += 1
#     row += 1
#     freq.append(len(projects))
#     sheet.write(row, 0, names[x - 1])
#     sheet.write(row, 1, freq[x - 1])
#     print(x,end=" | ")
#     print(names[x-1])
#     print("",end="    ")
#     print(freq[x-1],end=" projects total")
#     print()
#     print()
#     y = 0

# chrome.get(my_url)

