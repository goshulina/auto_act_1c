# -*- coding: utf-8 -*-
from robobrowser import RoboBrowser
import numpy as np
import time
import re
import dateutil.parser as dparser
from data_temp import *
from google_spreadsheet_DB import send_infa
from buhgalter import get_current_pokupki


def login():
    # if proxy:
    #     session = Session()
    #     session.proxies = {'http': proxys[np.random.choice(list(proxys.keys()))]}
    #     # session.proxies = {'http': proxys['telega']}
    #     # session.proxies = {'http': proxys['p1']}
    #     browser = RoboBrowser(session=session, history=True, user_agent=UA[np.random.choice(list(UA.keys()))])
    # else:
    browser = RoboBrowser(history=True, user_agent=UA[np.random.choice(list(UA.keys()))])
    # browser = RoboBrowser(history=True)
    login_url = 'https://passport.yandex.ru/passport'
    try:
        browser.open(login_url)
        form = browser.get_form(action=re.compile(r'passport\.yandex\.ru'))
        form['login'].value = '<...>'
        form['passwd'].value = '<...>'
        browser.submit_form(form)
        return browser
    except:
        # print('trying to login again.')
        # login(proxy)
        pass


def if_end_date_reached(date_end, current_raw_date):
    date_end = dparser.parse(date_end, fuzzy_with_tokens=True, ignoretz=True, dayfirst=True, fuzzy=True)[0]
    current_date = current_raw_date.split()[0] + '-' + months[current_raw_date.split()[1]] + '-' + \
                   current_raw_date.split()[2]
    current_date = dparser.parse(current_date, fuzzy_with_tokens=True, ignoretz=True, dayfirst=True, fuzzy=True)[0]
    if current_date >= date_end:
        return False
    else:
        return True


def get_links(path, browser):
    browser.open(path)
    out = browser.select('td.b-payments__td')
    links = [span.a for span in out]
    links = [i for i in links if i != None]
    check_links = [links[ii].attrs['href'] for ii in range(len(links))]
    out = browser.select('div.pages')
    links = [span.a for span in out]
    pages = [out[0].find_all('a')[i].attrs['href'] for i in range(len(out[0].find_all('a'))) if
             'pn=' in out[0].find_all('a')[i].attrs['href']]
    try:
        current_page = path.split('pn=')[1]
        for i in pages:
            if int(i.split('pn=')[1]) == int(current_page) + 1:
                next_page = i
                break
    except:
        next_page = pages[0]
    return check_links, next_page


def act_pages_checker(path, browser):
    browser.open('https://balance.yandex.ru' + path)
    info = []
    info_res = []
    try:
        for n, i in enumerate(browser.select('table.b-payments')[0].select('td')):
            try:
                info.append(i.text)
            except:
                pass
        for ii in range(2, len(info) - 6, 8):
            info_res.append([info[ii], info[ii + 1], info[ii + 2], info[ii + 3], info[ii + 4]])
        return info_res
    except:
        return False


def timeout():
    for i in range(10):
        time.sleep(np.random.choice(list(range(2, 10))))


def login_and_get_links(start_page, browser):
    if browser == None:
        browser = login()
        links_for_check = get_links(start_page, browser)
        return browser, links_for_check[0], links_for_check[1]
    else:
        links_for_check = get_links(start_page, browser)
        return links_for_check[0], links_for_check[1]

def handler(start_page, browser, date_end='31-03-2018',
            reconnect=False):  # , proxy_use=False):# , ):# , update_status=False):
    # if update_status:
    #     statuses_dict = get_cells_with_status()
    if reconnect:
        browser = browser
        links_for_check, next_page = login_and_get_links(start_page, browser)
    else:
        browser, links_for_check, next_page = login_and_get_links(start_page, None)
    infa_page = []
    try:
        acts = get_current_pokupki()
    except:
        timeout()
        acts = get_current_pokupki()
    for i in browser.select('tbody')[1].select('tr'):
        info = []
        for ii in i:
            try:
                info.append(ii.text)
            except:
                continue
        date = re.sub(r'(\xa0)+', ' ', info[3])
        summ = re.sub(r'(\xa0)+|\s', '', info[4])
        nds = re.sub(r'(\xa0)+', ' ', info[5])
        schet = re.sub(r'(\n)+|\s', '', info[7])
        infa_page.append([info[1], info[2], date, summ, nds, schet])
    send_infa(infa_page, 'Sheet5', acts)  # must be a list of lists
    if if_end_date_reached(date_end, date):
        # print('stopped. reason: date stage reached')
        return acts
    timeout()
    # for schet_factura, link in dict(zip([item[0] for item in infa_page], links_for_check)).items():
    #     response = act_pages_checker(link, browser)
    #     if response:
    #         spreadsheet_appender(schet_factura, response)
    #         timeout()
    #     else:
    #         spreadsheet_appender(schet_factura)
    #         timeout()
    # print(next_page)
    handler('https://balance.yandex.ru' + next_page, browser, date_end=date_end, reconnect=True)
    # try:
    #     handler('https://balance.yandex.ru' + next_page, browser, date_end=date_end, reconnect=True)#, proxy_use=False, reconnect=False)#beggining=np.random.choice([True, False]))
    # except:
    #     handler('https://balance.yandex.ru' + next_page, browser, date_end=date_end, reconnect=True)#, proxy_use=False, reconnect=False)#beggining=np.random.choice([True, False]))
