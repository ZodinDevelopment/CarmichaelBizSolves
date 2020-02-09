import bs4 as bs
from .browser_tools import load_more


def get_member_count(source):
    soup = bs.BeautifulSoup(source, 'lxml')
    member_browser = soup.find('div', attrs={'id': 'groupsMemberBrowser'})
    clearfix = member_browser.find('div', attrs={'class': 'clearfix'})

    total_in_group = int(clearfix.find('span').text)

    return total_in_group

def get_admin_count(source):
    soup = bs.BeautifulSoup(source, 'lxml')
    admin_section = soup.find('div', attrs={'id': 'groupsMemberSection_admins_moderators'})
    
    total_admins = int(admin_section.find('div', attrs={'class': 'clearfix'}).find('span').find('span').text)

    return total_admins

def get_members(browser, members_in_group):

    members = {}

    while len(members) < members_in_group:
        source = browser.page_source

        soup = bs.BeautifulSoup(source, 'lxml')
        member_section = soup.find('div', attrs={'id': 'groupsMemberSection_all_members'})

        a_tags = member_section.find_all('a')

        for a_tag in a_tags:
            name = a_tag.attrs.get('title')
            href = a_tag.attrs.get('href')
            if name is not None:
                if name not in members:
                    members[name] = href

        
        load_more(browser)

    return members


