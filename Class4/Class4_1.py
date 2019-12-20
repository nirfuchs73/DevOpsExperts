from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
# chrome_driver = webdriver.Chrome(executable_path='c:/DevOps/chromedriver.exe')
chrome_driver = webdriver.Chrome(
    executable_path='c:/DevOps/chromedriver.exe', options=chrome_options)
# geckod_river = webdriver.Firefox(executable_path='c:/DevOps/geckodriver.exe')
chrome_driver.implicitly_wait(5)
# geckod_river.implicitly_wait(5)


# 1. Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. FireFox – http://www.ynet.co.il
def func_1():
    # chrome_driver.get('http://www.walla.co.il')
    chrome_driver.get('http://www.google.com')
    # geckod_river.get('http://www.ynet.co.il')


# 2. In one of the browsers you open do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you created in clause 1.
def func_2():
    title = chrome_driver.title
    print(title)
    chrome_driver.refresh()
    title1 = chrome_driver.title
    print(title1)


# 3. Open a few browsers, locate any element, does the
# element has the same locators in the other browser? Yes
def func_3():
    chrome_driver.execute_script("window.open('http://www.google.com')")
    # print(chrome_driver.current_window_handle)
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    input1 = chrome_driver.find_element_by_xpath(
        '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    input1.send_keys('browsers 1')
    chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
    input2 = chrome_driver.find_element_by_xpath(
        '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    input2.send_keys('browsers 1')


# 4. Create a test with the following:
#  Open Google Translate web page
#  Write anything in Hebrew in the text area
def func_4():
    chrome_driver.get('https://translate.google.com/')
    element = chrome_driver.find_element_by_xpath('//*[@id="source"]')
    element.send_keys('שלום')


# 5.
#  Open Youtube web page
#  Type a name of a song
#  Click on search.
def func_5():
    chrome_driver.get('https://www.youtube.com/')
    searchEl = chrome_driver.find_element_by_xpath('//*[@id="search"]')
    searchEl.send_keys('sultans of swing')
    buttonEl = chrome_driver.find_element_by_xpath(
        '//*[@id="search-icon-legacy"]')
    buttonEl.click()


#  Open Chrome browser on Google Translate website: https://translate.google.com/
#  Find translation text field (the one you send keys to)
# with 3 different locators and print the WebElement you created.
def func_6():
    chrome_driver.get('https://translate.google.com/')
    element1 = chrome_driver.find_element_by_xpath('//*[@id="source"]')
    element2 = chrome_driver.find_element_by_id('source')
    element3 = chrome_driver.find_element_by_class_name(
        'tlid-source-text-input')
    print(element1)
    print(element2)
    print(element3)


# 7.
#  Open Chrome browser on Facebook website
# https://www.facebook.com/
#  Login into Facebook (No need to send me credentials).
def func_7():
    chrome_driver.get('https://www.facebook.com/')
    emailEL = chrome_driver.find_element_by_id('email')
    emailEL.send_keys('email')
    passEL = chrome_driver.find_element_by_id('pass')
    passEL.send_keys('password')
    submittEL = chrome_driver.find_element_by_id('loginbutton')
    # //*[@id="loginbutton"]
    submittEL.click()


# 8.
#  Open Chrome browser on any webpage.
#  Delete all cookies from browser.
#  Make sure all cookies are deleted by printing all cookies
# stored in the browser.
def func_8():
    chrome_driver.get('http://www.google.com/')
    print(chrome_driver.get_cookies())
    chrome_driver.delete_all_cookies()
    print(chrome_driver.get_cookies())


# 9.
#  Open any browser on "Github" website.
#  https://github.com/
#  Enter “Selenium” keyword in search textfield
#  Press Enter to search (through code - of course).
def func_9():
    chrome_driver.get('https://github.com/')
    searchEl = chrome_driver.find_element_by_xpath(
        '/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]')
    searchEl.send_keys('selenium')
    searchEl.send_keys(Keys.ENTER)


#  Find a way to disable all extensions in
# o Chrome
# o Firefox
# o Internet Explorer.
#  Run browsers without extensions.
def func_10():
    chrome_driver.get('http://www.google.com/')


def main():
    # func_1()
    # func_2()
    # func_3()
    # func_4()
    # func_5()
    # func_6()
    # func_7()
    # func_8()
    # func_9()
    func_10()


if __name__ == "__main__":
    main()
