# -*- coding: utf-8 -*-
from app.google_spreadsheet_DB import google_spreadsheets, list_maker
from app.buhgalter import main_buhgalter, get_current_pokupki
from app.yandex_analizator import handler, timeout
import datetime as dt
import time
import numpy as np

def timeout():
    for i in range(10):
        time.sleep(np.random.choice(list(range(3, 10))))

def main(days, mode):  # add parsing/no_parsing mode
    t_delta = dt.timedelta(days=days)
    sheets = google_spreadsheets()
    # if sheets.worksheet('Sheet5').get_all_records()[0]['Акт №'] == 'Ебошь всех клиентосов сначала сначала':
    #     if mode == 0:
    #         sheets.worksheet('Sheet5').update_cell(2, 1, '')
    #         address = addresses_1c['main_address'] + addresses_1c['schet_factura']
    #         try:
    #             the_freshest_date = date_sercher(data_extractor_1C(address))
    #         except:
    #             # print("Не смог подключиться к Яндексу. Попробуем#  через пару минут")
    #             timeout()
    #             the_freshest_date = date_sercher(data_extractor_1C(address))
    #         dates = str(the_freshest_date - t_delta).split()[0].split('-')
    #         date_end = dates[2] + '-' + dates[1] + '-' + dates[0]
    #         # print('Скачиваю инфу об актах клиентосов из Яндекс.Баланса ')
    #         acts = handler('https://balance.yandex.ru/acts.xml', None, date_end=date_end)
    #         # print('Парсер Яндекса отработал')
    #         timeout()
    #         list_maker()
    #         main_buhgalter(acts)
    #     elif mode == 1:
    #         sheets.worksheet('Sheet5').update_cell(2, 1, '')
    #         address = addresses_1c['main_address'] + addresses_1c['schet_factura']
    #         try:
    #             the_freshest_date = date_sercher(data_extractor_1C(address))
    #         except:
    #             # print("Не смог подключиться к Яндексу. Попробуем#  через пару минут")
    #             timeout()
    #             the_freshest_date = date_sercher(data_extractor_1C(address))
    #         dates = str(the_freshest_date - t_delta).split()[0].split('-')
    #         date_end = dates[2] + '-' + dates[1] + '-' + dates[0]
    #         # print('Скачиваю инфу об актах клиентосов из Яндекс.Баланса ')
    #         handler('https://balance.yandex.ru/acts.xml', None, date_end=date_end)
    #         # print('Парсер Яндекса отработал')
    #     elif mode == 2:
    #         try:
    #             acts = get_current_pokupki()
    #         except:
    #             timeout()
    #             acts = get_current_pokupki()
    #         list_maker()
    #         main_buhgalter(acts)
    # else:
    if mode == 0:
        # date_end = str(last_date_sercher()[0] - t_delta).split()[0]
        date_end = str(dt.datetime.today() - t_delta).split()[0]
        date_end = date_end.split('-')[2] + '-' + date_end.split('-')[1] + '-' + date_end.split('-')[0]
        # print(date_end)
        # print('Скачиваю инфу об актах клиентосов из Яндекс.Баланса')
        acts = handler('https://balance.yandex.ru/acts.xml', None, date_end=date_end)
        # print('Парсер Яндекса отработал')
        timeout()
        list_maker()
        main_buhgalter(acts)
    elif mode == 1:
        # date_end = str(last_date_sercher()[0] - t_delta).split()[0]
        date_end = str(dt.datetime.today() - t_delta).split()[0]
        date_end = date_end.split('-')[2] + '-' + date_end.split('-')[1] + '-' + date_end.split('-')[0]
        # print(date_end)
        # print('Скачиваю инфу об актах клиентосов из Яндекс.Баланса')
        handler('https://balance.yandex.ru/acts.xml', None, date_end=date_end)
        # print('Парсер Яндекса отработал')
    elif mode == 2:
        try:
            acts = get_current_pokupki()
        except:
            timeout()
            acts = get_current_pokupki()
        list_maker()
        main_buhgalter(acts)

# 0 - all
# 1 - parsing only
# 2 - buh only