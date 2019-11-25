from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from hfdb import *
browser=webdriver.Chrome()
browser.get('https://www.foody.vn/da-nang')
time.sleep(2)
ele=browser.find_elements_by_xpath("//div[@id='box-delivery']//div[@class='n-listitems']//li")
for i in ele:
    name=i.find_element_by_xpath(".//span[@class='none-quality-text ng-binding']").text
    address=i.find_element_by_xpath(".//div[@class='address limit-text ng-binding']").text
    pic=i.find_element_by_xpath(".//div[1]//a[1]//img[1]").get_attribute('src')
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
    if check_food(address)==1:
      insert_food(name,pic,address,duong,quan,tinh)

# ele=browser.find_elements_by_xpath("//div[@class='item-restaurant']")
# for v in ele:
#     name=v.find_element_by_xpath(".//h4[@class='name-res']").text
#     address=v.find_element_by_xpath(".//div[@class='address-res']").text
#     pic=v.find_element_by_xpath(".//a[1]//div[1]//img[1]").get_attribute('src')
    

browser.close()