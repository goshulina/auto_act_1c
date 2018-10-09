# -*- coding: utf-8 -*-
from google_spreadsheet_DB import google_spreadsheets, list_maker
from buhgalter import main_buhgalter, get_current_pokupki
from yandex_analizator import handler, timeout
import datetime as dt
import time
import schedule

def main(days=3):  # add parsing/no_parsing mode
    t_delta = dt.timedelta(days=days)
    date_end = str(dt.datetime.today() - t_delta).split()[0]
    date_end = date_end.split('-')[2] + '-' + date_end.split('-')[1] + '-' + date_end.split('-')[0]
    acts = handler('https://balance.yandex.ru/acts.xml', None, date_end=date_end)
    timeout()
    list_maker()
    main_buhgalter(acts)

def job():
    print('a minute had come')

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(main)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)