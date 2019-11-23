from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from hfdb import *
browser=webdriver.Chrome()
browser.get('https://www.now.vn/bo-suu-tap/best-seller-thang-9hn')
time.sleep(2)
list_food=[]
ele=browser.find_elements_by_xpath("//div[@class='item-restaurant']")
for v in ele:
    name=v.find_element_by_xpath(".//h4[@class='name-res']").text
    address=v.find_element_by_xpath(".//div[@class='address-res']").text
    pic=v.find_element_by_xpath(".//a[1]//div[1]//img[1]").get_attribute('src')
    street=''
    quan=''
    duong1=''
    duong=''
    tinh=''
    for v in range(len(address)):
        if address[v]!=',':
            street=street+address[v]
        else:
            break
    for i in range(v+7,len(address)):
        if address[i]!=',':
            quan=quan+address[i]
        else:
            break
    for j in range(i+2,len(address)):
        tinh=tinh+address[j]
    for v in range(len(street)-1,-1,-1):
        if not street[v].isdigit() or street[v]==' ':
            duong1=street[v]+duong1
        else:
            break
    for v in range(1,len(duong1)):
        duong=duong+duong1[v]
    insert_food(name,pic,address,duong,quan,tinh)

browser.close()