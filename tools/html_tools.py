import bs4 as bs
from .browser_tools import load_more


def get_member_count(source):
    soup = bs.BeautifulSoup(source, 'lxml')
    member_browser = soup.find('div', attrs={'id': 'groupsMemberBrowser'})
    clearfix = member_browser.find('div', attrs={'class': 'clearfix'})
    total_in_group = int(clearfix.find('span').text)

    print('Alleged total number of individuals in the group: {}\n'.format(str(total_in_group)))

    return total_in_group

def get_admin_count(source):
    soup = bs.BeautifulSoup(source, 'lxml')
    admin_section = soup.find('div', attrs={'id': 'groupsMemberSection_admins_moderators'})

    total_admins = int(admin_section.find('div', attrs={'class': 'clearfix'}).find('span').find('span').text)

    print('There are currently {} admins and moderators running this group.'.format(str(total_admins)))

    return total_admins

def get_members(browser, members_in_group):
    print('Now loading web page contents into browser')
    load_more(browser)

    members = {}
    source = browser.page_source 
    soup = bs.BeautifulSoup(source , 'lxml')
    member_section = soup.find('div', attrs={'id': 'groupsMemberSection_all_members'})

    print('Identified container with all our desired content.')
    print("Crawling through it's contents and scraping our loot.")

    a_tags = member_section.find_all('a')
    for a_tag in a_tags:
        name = a_tag.attrs.get('title')
        href = a_tag.attrs.get('href')
        if name is not None:
            if name not in members:
                print(name + '....\n')
                members[name] = href

    print('Finished, member names have been scraped from page source code.\nParsed {} names today!'.format(str(len(members))))

    return members




