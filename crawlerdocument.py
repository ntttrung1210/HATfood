from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from hfdb import*
from selenium.webdriver.common.action_chains import ActionChains
import time
browser=webdriver.Chrome()
# browser.get("http://viendinhduong.vn/vi/dinh-duong-va-suc-khoe.html")
# time.sleep(2)
# ele=browser.find_elements_by_xpath("//div[@class='item col-md-4 col-xs-6 col-lg-4 col-sm-4']")
# for v in ele:
#     name=v.find_element_by_xpath("./a").text
#     pic=v.find_element_by_xpath(".//img").get_attribute("src")
#     link=v.find_element_by_xpath("./a").get_attribute("href")
#     insert_doc(name,pic,link)
ls=get_all_doc()
for v in range(5):
    ll=ls[v]['link']
    browser.get(ll)
    time.sleep(1)
    content=browser.find_element_by_xpath("//div[@id='divDetailContent']").text
    insert_content(content)