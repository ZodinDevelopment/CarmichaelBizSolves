from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 


def init_driver(driver_name):
    if driver_name == 'Chrome':
        browser = webdriver.Chrome()
    print('Webdriver intialized')
    return browser

def facebook_auth(browser, login, login_pass):
    print('Getting facebook auth for this session.')
    browser.get('http://www.facebook.com')
    
    username = browser.find_element_by_id('email')
    password = browser.find_element_by_id('pass')
    submit = browser.find_element_by_id('loginbutton')

    #Login like a human!
    username.send_keys(login)
    password.send_keys(login_pass)
    submit.click()
    print('Successfully retrieved login token for this webdriver instance.')

def group_members_page(browser, page_url):
    print('Now using this authorized session to navigate to the web content containing our information of interest.')
    actions = webdriver.ActionChains(browser)
    keys = Keys()
    browser.get(group_url)

    print('Letting browser catch up and render necessary dynamic content')
    time.sleep(6)

    actions.send_keys(keys.ESCAPE)
    actions.perform()

def load_more(browser):
    print('Data of interest is not loaded into page source until scrolled in.\n')

    print('Scrolling all of the dynamic content into source.')
    browser.execute("window.scrollTo(0, document.body.scrollHeight);")

    source = browser.page_source 
    raw_size = len(source)
    data_loading = True

    while data_loading:
        print('More content still hidden from source.')
        last_size = raw_size
        time.sleep(1)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        source = browser.page_source
        raw_size = len(source)

        if raw_size = last_size:
             print("All available content for this web page is now loaded into source.")
             data_loading = False 



