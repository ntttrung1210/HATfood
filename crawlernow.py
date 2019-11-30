from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from hfdb import *
browser=webdriver.Chrome()
browser.get('https://www.now.vn/ha-noi/danh-sach-dia-diem-giao-tan-noi?q=h%E1%BB%A7%20ti%E1%BA%BFu')
time.sleep(2)
for i in range(3):
    ele=browser.find_elements_by_xpath("//div[@class='item-restaurant']")
    for v in ele:
        name=v.find_element_by_xpath(".//h4[@class='name-res']").text
        address=v.find_element_by_xpath(".//div[@class='address-res']").text
        pic=v.find_element_by_xpath(".//a[1]//div[1]//img[1]").get_attribute('src')
        quan=''
        duong=''
        tinh=''
        for i in range(len(address)-1,-1,-1):
            if address[i-1]==',' and address[i]==' ':
                break
            else:
                tinh=address[i]+tinh
        for v in range(i-2,-1,-1):
            if address[v-6]==',' and address[v]==' ':
                break
            else:
                quan=address[v]+quan
        for i in range(v-7,-1,-1):
            if address[i-1].isdigit() and address[i]==' ':
                break
            else:
                duong=address[i]+duong
        # ls.append({'name':name,'pic':pic,'address':address})
        if pic!='' and check_food(address)==1:
            insert_food(name,pic,address,duong,quan,tinh)
    ele1=browser.find_element_by_xpath("//span[@class='icon icon-paging-next']")
    ele1.click()
    time.sleep(2)
browser.close()