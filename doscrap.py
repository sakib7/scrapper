from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

my_url = 'https://summerofcode.withgoogle.com/organizations/'


# uClient = ureq(my_url)
# pagehtml = uClient.read()
# uClient.close()
#
# page_soup = soup(pagehtml,"html.parser")
#
# containers = page_soup.findAll("div",{"class":"organization-card__container"})

def loadFullPage(browser,pause):
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = (newHeight - 300)
    return browser


chromePath = r"C:\Users\sakib\Desktop\python\chromedriver_win32\chromedriver.exe"
chrome = webdriver.Chrome(chromePath)
chrome.get(my_url)


elem = chrome.find_element_by_tag_name("body")

no_of_pagedowns = 4

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    no_of_pagedowns-=1
    print(no_of_pagedowns)

# chrome.find_element_by_xpath("""/html/body/div/div/div[1]/ui-view/div/ui-view/ui-view/div/div/section/div/div[1]/soc-organizations-list/div/div[8]/md-card/div""").click()

cardlist = chrome.find_elements_by_class_name("organization-card__container")
print(len(cardlist))

names = []
links = []
dic = {}
x=0
for card in cardlist:
    card.click()
    time.sleep(1)
    title = chrome.find_element_by_class_name("organization-card__title")
    link = chrome.find_element_by_class_name("md-primary")

    t = title.get_attribute('innerHTML')
    l = link.get_attribute("href")
    names.append(t)
    links.append(l)
    dic[t]=l

    if x == 10:
        break
    else:
        x+=1
        print(x , end=" ")
        print(names[-1])





for title,link in dic.items():
    print (title , end=" ")
    print (link)

    chrome.get(link)
    loadFullPage(chrome,1)




chrome.quit()