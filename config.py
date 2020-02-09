#Configuration for the script

#Webdriver, currently only supports Chrome
#While this is True, output emails will only go to the development address
TESTING = False

WEBDRIVER = 'Chrome'

#Set to true to run the webdriver in headless mode (not supported yet)

HEADLESS = False

#Set to false to have the script retrieve the facebook password from this file
#WARNING this is not secure and is strongly advised against
GET_PASS = True

#GECKODRIVER_PATH = 

CHROMEDRIVER_PATH = '/usr/local/bin/Chromedriver'

OUTPUT_DIR = 'data/'

FACEBOOK_LOGIN = 'treycarmichael98@gmail.com'

FACEBOOK_GROUP_URL = "https://www.facebook.com/groups/2798143833582929/members/"
