from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
ls=[]
from hfdb import *
browser=webdriver.Chrome()
browser.get('https://www.now.vn/ha-noi/danh-sach-dia-diem-phuc-vu-trang-mieng-8-giao-tan-noi')
time.sleep(2)
ls=[]
for i in range(3):
    ele=browser.find_elements_by_xpath("//div[@class='item-restaurant']")
    for v in ele:
        name=v.find_element_by_xpath(".//h4[@class='name-res']").text
        address=v.find_element_by_xpath(".//div[@class='address-res']").text
        pic=v.find_element_by_xpath(".//a[1]//div[1]//img[1]").get_attribute('src')
        ls.append({'name':name,'pic':pic,'address':address})
    ele1=browser.find_element_by_xpath("//span[@class='icon icon-paging-next']")
    ele1.click()
    time.sleep(2)
print(ls)
# browser.close()