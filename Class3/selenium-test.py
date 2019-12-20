from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='c:/DevOps/chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://translate.google.com/')
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source)
# driver.refresh()

# driver.find_element_by_id('source').click()
# driver.find_element_by_id('source').send_keys('hello')
# elements = driver.find_elements_by_id('source')
# elements[0].click()
# elements[0].send_keys('hello1')
element = driver.find_element_by_id('source')
if element.is_enabled():
    element.send_keys('hello')
    element.send_keys(Keys.ENTER)
    print(element.get_attribute('rows'))


# print(len(elements))
# x = elements[0]
# print(x)
# driver.find_element_by_xpath('//*[@id="source"]')

# driver.quit()
