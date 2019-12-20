from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='c:/DevOps/chromedriver.exe')
driver.implicitly_wait(5)

driver.get('https://gofile.io/?t=uploadFiles/')

element = driver.find_element_by_id('divDragDrop')
if element.is_enabled():
    element.send_keys('C:/Users/fuchs/Desktop/DevOps/test.js')
