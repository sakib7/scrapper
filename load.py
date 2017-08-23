# -*- coding: utf-8 -*-
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import xlwt
csvpath = r"C:\Users\sakib\Desktop\python\data.xls"
book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("2017")

my_url = 'https://summerofcode.withgoogle.com/organizations/'



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

chrome = webdriver.Chrome(chromePath)
chrome.get(my_url)
loadFullPage(chrome,3)

cardlist = chrome.find_elements_by_class_name("organization-card__container")
print(len(cardlist))

names = []
links = []
dic = {}
x=0
row=0
for card in cardlist:
    card.click()
    time.sleep(1)
    title = chrome.find_element_by_class_name("organization-card__title")
    link = chrome.find_element_by_class_name("md-primary")

    t = title.get_attribute('innerHTML')
    l = link.get_attribute("href")
    names.append(t)
    links.append(l)

    sheet.write(row, 0, t)
    sheet.write(row, 1, l)
    row += 1
    x+=1
    print(x, end=" | ")
    print(names[-1] , end=" | ")
    print(links[-1])

# x = 0
# row = 0
# freq = []
# for link in links:
#
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
    # for project in projects:
    #     elem = project.find_element_by_class_name("pos-rel")
    #     intern = elem.find_element_by_tag_name("h2").text
    #     intern_project =elem.find_element_by_tag_name("div").find_element_by_tag_name("a").text
    #     y += 1
    #     print("        ",end="")
    #     print(y,end=" | ")
    #     print(intern, end=" | ")
    #     print(intern_project)
    #     sheet.write(row,0,names[x-1])
    #     sheet.write(row,1,intern)
    #     sheet.write(row,2,intern_project)
    #     sheet.write(row,3,freq[x-1])
    #     row += 1

book.save(csvpath)