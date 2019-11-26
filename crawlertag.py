from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from hfdb import *
browser=webdriver.Chrome()
browser.get('https://www.now.vn/ho-chi-minh/danh-sach-dia-diem-phuc-vu-mi-pho-giao-tan-noi')
for i in range(3):
    ele=browser.find_elements_by_xpath("//div[@class='item-restaurant']")
    for v in ele:
        name=v.find_element_by_xpath(".//h4[@class='name-res']").text
        address=v.find_element_by_xpath(".//div[@class='address-res']").text
        pic=v.find_element_by_xpath(".//a[1]//div[1]//img[1]").get_attribute('src')
        insert_mipho(name,pic,address)
    ele1=browser.find_element_by_xpath("//span[@class='icon icon-paging-next']")
    ele1.click()
    time.sleep(2)
# browser.close()