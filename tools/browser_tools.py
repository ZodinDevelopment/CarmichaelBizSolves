from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
#import bs4 as bs

def init_driver(driver_name):
    if driver_name == "Chrome":

        browser = webdriver.Chrome()

    return browser

def facebook_auth(browser, login, login_pass):
    browser.get('http://www.facebook.com')

    username = browser.find_element_by_id('email')
    password = browser.find_element_by_id('pass')
    submit = browser.find_element_by_id('loginbutton')

    username.send_keys(login)
    password.send_keys(login_pass)
    submit.click()

def group_members_page(browser, group_url):
    actions = webdriver.ActionChains(browser)
    browser.get(group_url)

    keys = Keys()
    actions.send_keys(keys.ESCAPE)
    actions.perform()
def load_more(browser):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    source = browser.page_source
    raw_size = len(source)
    
    data_loading = True 
    #soup = bs.BeautifulSoup(browser.page_source, 'lxml')
    #section = soup.find('div', attrs={'id': 'groupsMemberSection_all_members'})

    while data_loading:
        
        last_size = raw_size 
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        source = browser.page_source
        raw_size = len(source)

        if raw_size == last_size:
            data_loading = False




