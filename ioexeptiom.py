# -*- coding: utf-8 -*-
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlwt
csvpath = r"C:\Users\sakib\Desktop\python\data1.xls"
book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("s1")
sheet.write(0,0,"Memduh Gökırmak")
book.save(csvpath)

#
# csvpath = r"C:\Users\sakib\Desktop\python\data.csv"
# with open(csvpath, 'w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';')
#     writer.writerow('my_utf8_string')
#     writer.writerow("Memduh Gökırmak".encode('utf-8'))

