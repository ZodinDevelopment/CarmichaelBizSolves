from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


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
    browser.get(group_url)

def load_more(browser):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")




