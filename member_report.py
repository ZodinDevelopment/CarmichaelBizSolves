import os
import time
import getpass
import json
from datetime import datetime
import config
from core.browser_tools import *
from core.html_tools import *
from core.gmail_client import *

group_url = config.FACEBOOK_GROUP_URL
login = config.FACEBOOK_LOGIN
driver_name = config.WEBDRIVER
driver_path = config.CHROMEDRIVER_PATH
output_dir = config.OUTPUT_DIR
testing = config.TESTING
def main():
    login_pass = getpass.getpass()

    browser = init_driver(driver_name)

    facebook_auth(browser, login, login_pass)

    script_run(browser)

    with open('new_users.txt', 'r') as f:
        message = f.read()

    print('Enter SMTP Auth password.')
    mail_pass = getpass.getpass()

    setup_gmail(message, mail_pass, testing)

    last_run = datetime.now()


    while True:
        time.sleep(600)

        now = datetime.now()

        if str(now.hour) == '9' or now.timestamp - last_run.timestamp() >= 86400:
            script_run(browser)

            last_run = datetime.now()

        else:
            continue

def script_run(browser):

    group_members_page(browser, group_url)
    page_source = browser.page_source

    total_in_group = get_member_count(page_source)
    admin_total = get_admin_count(page_source)

    members_in_group = total_in_group - admin_total

    members_as_dict = get_members(browser, members_in_group)

    now = datetime.now()


    if os.path.isfile('group_members.json'):
        existing_members = json.loads(open('group_members.json').read())

    else:
        existing_members = members_as_dict

    new_members = []

    for member in members_as_dict:
        if existing_members.get(member) is None:
            new_members.append(member)

    new_count = len(new_members)

    with open('group_members.json', 'w') as f:
        json.dump(members_as_dict, f)

    with open('new_users.txt', 'w') as f:
        f.write(now.ctime())
        f.write('\n{} new members in group as of {}:{}:{}'.format(str(new_count), now.hour, now.minute, now.second))

        for key, member in enumerate(new_members):
            f.write("[{}]: {}\n".format(str(key), member))

        f.write('\n')
        f.write('='*20)

    print('Successfully saved records.')



if __name__ == '__main__':
    main()


