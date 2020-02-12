import os
import time
import getpass
import json
from datetime import datetime
import config 
from tools.browser_tools import *
from tools.html_tools import *
from tools.output_mgmt import *


#Variables defined by constants in config.py
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
        report = f.read()
    print('Preparing report for delivery.\n')

    dev_pass = getpass.getpass()

    send_report(dev_pass, testing)

    last_run = datetime.now()

    waiting = True
    print('The automator is now going into hibernation mode. It will briefly wake every 600 seconds to see if its time to generate the next report')
    while waiting:
        print('Sleeping for ten minutes before checking the date and time.')
        time.sleep(600)

        now = datetime.now()
        
        if now.day == last_run.day:
            print('Report already completed for today, going back to sleep')
            continue 
        elif now.day > last_run.day and now.hour == 8 and now.minute >= 25:
            print('Now within a margin of 5 minutes until expected report delivery\n')
            print('Initializing the script...')

            browser = init_driver(driver_name)
            facebook_auth(browser, login, login_pass)
            script_run(browser)

            last_run = datetime.now()
        
            print('Another day at the office :P')
            print('\nSending completed report to the client via Facebook Messenger')
            send_report(dev_pass, testing=False)
            delivered_at = datetime.now()
            print("Delivered report. Today's finish line: {}".format(delivered_at.ctime()))
            print('\nLogging execution status and results to "dev.log"')
            make_dev_log(message, delivered_at)
            print("Okay going back to sleep work is whooping my ass lol.")

        else:
            continue


def script_run(browser):
    group_members_page(browser, group_url)
    
    page_source = browser.page_source 
    print("Now loaded page source with all our currently desired content in.")

    total_in_group = get_member_count(page_source)
    admin_total = get_admin_count(page_source)

    members_in_group = total_in_group - admin_total


    members_as_dict = get_members(browser, members_in_group)

    now = datetime.now()
    print('Data scraped at {}'.format(now.ctime()))

    print("\nLoading data from the last execution in json file.")
    if os.path.isfile('group_members.json'):
        existing_members = json.loads(open("group_members.json").read())
    else:
        print("No json file found containing pre-existing data")
        existing_members = members_as_dict

    new_members = []
    print('Now iterating through both data sets and identifying new members since last execution\n')

    for member in members_as_dict:
        print(member + '\n')
        if existing_members.get(member) is None:
            print('!! New Member !!\n--------\n')
            new_members.append(member)
        else:
            print('---------\n')


    new_count = len(new_members)

    print("Identified {} new members in the group.".format(str(new_count)))


    with open('group_members.json', 'w') as f:
        json.dump(members_as_dict, f)

    print("Updated data in json file")

    with open('new_users.txt', 'w') as f:
        f.write(now.ctime())
        f.write('\n{} new members in group as of now.\n'.format(str(new_count)))

        for key, member in enumerate(new_members):
            line = "[{}]: ".format(str(key + 1)) + (" "*4) + "{}\n".format(member)
            f.write(line)
            f.write('-'*len(line) + '\n')

        f.write('\n')
        f.write('='* 20)

    print("Generated report and saved records to them.")

    browser.close()


if __name__ == "__main__":
    main()
            

