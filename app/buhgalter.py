# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET
import re
from dateutil import parser
from app.google_spreadsheet_DB import google_spreadsheets
from app.data_temp import *
import time
import numpy as np


def get_current_pokupki():
    address = 'https://login:pass@terminal.scloud.ru/base/odata/standard.odata/Document_ПоступлениеТоваровУслуг'
    response = requests.get(address, headers=headers)
    response = response.content.decode('utf-8')
    acts = []
    tree = ET.ElementTree(ET.fromstring(response))
    for n, elem in enumerate(tree.iter()):
        if elem.text != None:
            if 'НомерВходящегоДокумента' in elem.tag:
                acts.append(elem.text)
    return acts


def get_contragents_dogovors():
    address = 'https://login:pass@terminal.scloud.ru/base/odata/standard.odata/Catalog_ДоговорыКонтрагентов'
    try:
        response = requests.get(address)
        content = response.content.decode('utf-8')
        tree = ET.ElementTree(ET.fromstring(content))
    except:
        timeout()
        response = requests.get(address)
        content = response.content.decode('utf-8')
        tree = ET.ElementTree(ET.fromstring(content))
    companies_docs = {}
    for n, elem in enumerate(tree.iter()):
        if 'Ref_Key' in str(elem.tag):
            try:
                companies_docs[elem.text]
                x = elem.text
            except:
                companies_docs.update({elem.text: []})
                x = elem.text
        elif 'Owner_Key' in str(elem.tag):
            companies_docs[x].append(elem.text)
        elif 'Description' in str(elem.tag):  # and 'Агентский договор' not in str(elem.text):
            companies_docs[x].append(elem.text)
    return companies_docs


def contragenti_extractor_1C(address):
    try:
        response = requests.get(address)
        content = response.content.decode('utf-8')
        tree = ET.ElementTree(ET.fromstring(content))  #### TRY CAT
    except:
        timeout()
        response = requests.get(address)
        content = response.content.decode('utf-8')
        tree = ET.ElementTree(ET.fromstring(content))  #### TRY CAT
    companies = {}
    x = ''
    for n, elem in enumerate(tree.iter()):
        if 'Ref_Key' in str(elem.tag) or 'Description' in str(elem.tag):
            if len(elem.text.split('-')) >= 5:
                try:
                    companies[elem.text]
                    x = elem.text
                except:
                    companies.update({elem.text: ''})
                    x = elem.text
            else:
                companies.update({x: elem.text})
    return companies


def timeout():
    for i in range(3):
        time.sleep(np.random.choice(list(range(1, 3))))


def data_extractor_1C(address):
    try:
        response = requests.get(address)
        content = response.content.decode('utf-8')
        tree = ET.ElementTree(ET.fromstring(content))
    except:
        timeout()
        response = requests.get(address)
        content = response.content.decode('utf-8')
        tree = ET.ElementTree(ET.fromstring(content))
    properties = {}
    x = ''
    properties_dates = {}
    for n, elem in enumerate(tree.iter()):
        if 'Контрагент_Key' in str(elem.tag) or 'Комментарий' in str(elem.tag):
            if elem.text is not None:
                if len(elem.text.split('-')) == 5:
                    try:
                        properties[elem.text]
                        properties_dates[elem.text]
                        x = elem.text
                    except:
                        properties.update({elem.text: []})
                        properties_dates.update({elem.text: []})
                        x = elem.text
                else:
                    properties[x].append(elem.text.split()[0])
                    try:
                        properties_dates[x].append(elem.text.split('от ')[1].split('2018')[0] + '2018')
                    except:
                        properties_dates[x].append('')
    return properties, properties_dates


def company_name_returner(scheta_oplat, schet):
    for i in scheta_oplat.values():
        try:
            if schet in i['Комментарий']:
                return i['Контрагент_Key'], i['ДоговорКонтрагента_Key']
            else:
                continue
        except:
            print('exception')
            continue
            # Комментарий field has a value of None


def date_sercher(data):
    count = None
    for i in data.values():
        if count == None:
            count = parser.parse(i['Date'].split('T')[0], dayfirst=False)
        else:
            if parser.parse(i['Date'].split('T')[0], dayfirst=False) < count:
                continue
            else:
                count = parser.parse(i['Date'].split('T')[0], dayfirst=False)
                # check = i
    return count


def buhgalter_sercher(schet):
    sheets = google_spreadsheets()
    sheet = sheets.worksheet('Sheet5')
    for i in sheet.get_all_records():
        if i['Счет'] == schet:
            return i
        else:
            continue


def field_sercher(data, field, key, key_field):
    for i in data.values():
        if i[key_field] == key and i[key_field] != None:
            return i[field]


def request_act_body_filler(company, parsed_data, b_schet, company_id, mode, dogovor=None):
    global act_creation_schema, provodka_schema
    # date_today = str(dt.datetime.today()).split()[0] + 'T00:00:00'
    date = parsed_data[0]['Дата'][:-3].split()[2] + '-' + months[
        parsed_data[0]['Дата'][:-3].split()[1]] + '-' + months_inverse_2[
               parsed_data[0]['Дата'][:-3].split()[0]] + 'T07:00:00'
    date_2 = parsed_data[0]['Дата'][:-3].split()[2] + '-' + months[
        parsed_data[0]['Дата'][:-3].split()[1]] + '-' + months_inverse_2[
               parsed_data[0]['Дата'][:-3].split()[0]] + 'T00:00:00'
    if mode == 'act':
        comment = 'ГШН-бухгалер ' + b_schet + ' от ' + parsed_data[0]['Дата для коммента'] + ' ' + company
        act_creation_schema = act_creation_schema.split('<d:НомерВходящегоДокумента>')[
                                  0] + '<d:НомерВходящегоДокумента>' + str(
            parsed_data[0]['Акт №']) + '</d:НомерВходящегоДокумента>' + \
                              act_creation_schema.split('<d:НомерВходящегоДокумента>')[1].split(
                                  '</d:НомерВходящегоДокумента>')[1]
        ### DATES
        act_creation_schema = act_creation_schema.split('<d:ДатаВходящегоДокумента>')[
                                  0] + '<d:ДатаВходящегоДокумента>' + date_2 + '</d:ДатаВходящегоДокумента>' + \
                              act_creation_schema.split('<d:ДатаВходящегоДокумента>')[1].split(
                                  '</d:ДатаВходящегоДокумента>')[1]
        # print(act_creation_schema)
        act_creation_schema = act_creation_schema.split('<d:Date>')[0] + '<d:Date>' + date + '</d:Date>' + \
                              act_creation_schema.split('<d:Date>')[1].split('</d:Date>')[1]
        ###
        # print(act_creation_schema)
        act_creation_schema = act_creation_schema.split('<d:Комментарий>')[
                                  0] + '<d:Комментарий>' + comment + '</d:Комментарий>' + \
                              act_creation_schema.split('<d:Комментарий>')[1].split('</d:Комментарий>')[1]
        act_creation_schema = act_creation_schema.split('<d:СуммаДокумента>')[0] + '<d:СуммаДокумента>' + \
                              re.sub(r'\,', '.', parsed_data[0]['Сумма'].split('руб')[0]) + '</d:СуммаДокумента>' + \
                              act_creation_schema.split('<d:СуммаДокумента>')[1].split('</d:СуммаДокумента>')[1]
        act_creation_schema = act_creation_schema.split('на проекте Яндекс.Директ в ')[
                                  0] + 'на проекте Яндекс.Директ в ' + \
                              months_inverse[date.split('-')[1]] + ' 2018 года</d:Содержание>' + \
                              act_creation_schema.split('на проекте Яндекс.Директ в ')[1].split(
                                  '2018 года</d:Содержание>')[1]
        act_creation_schema = act_creation_schema.split('<d:Цена>')[0] + '<d:Цена>' + re.sub(r'\,', '.', parsed_data[0][
            'Сумма'].split('руб')[0]) + '</d:Цена>' + act_creation_schema.split('<d:Цена>')[1].split('</d:Цена>')[1]
        act_creation_schema = act_creation_schema.split('<d:Сумма>')[0] + '<d:Сумма>' + re.sub(r'\,', '.',
                                                                                               parsed_data[0][
                                                                                                   'Сумма'].split(
                                                                                                   'руб')[
                                                                                                   0]) + '</d:Сумма>' + \
                              act_creation_schema.split('<d:Сумма>')[1].split('</d:Сумма>')[1]

        act_creation_schema = act_creation_schema.split('<d:СуммаНДС>')[0] + '<d:СуммаНДС>' + \
                              re.sub(r'\s', '', re.sub(r'\,', '.', parsed_data[0]['В т.ч. НДС'].split(' руб')[0])) + \
                              '</d:СуммаНДС>' + act_creation_schema.split('<d:СуммаНДС>')[1].split('</d:СуммаНДС>')[1]

        act_creation_schema = act_creation_schema.split('<d:Содержание>')[0] + '<d:Содержание>' + \
                              act_creation_schema.split('<d:Содержание>')[1].split('<d:Контрагент_Key>')[
                                  0] + '<d:Контрагент_Key>' + company_id + '</d:Контрагент_Key>' + \
                              act_creation_schema.split('<d:Содержание>')[1].split('<d:Контрагент_Key>')[1].split(
                                  '</d:Контрагент_Key>')[1]

        act_creation_schema = act_creation_schema.split('<d:Содержание>')[0] + '<d:Содержание>' + \
                              act_creation_schema.split('<d:Содержание>')[1].split('<d:ДоговорКонтрагента_Key>')[
                                  0] + '<d:ДоговорКонтрагента_Key>' + dogovor + '</d:ДоговорКонтрагента_Key>' + \
                              act_creation_schema.split('<d:Содержание>')[1].split('<d:ДоговорКонтрагента_Key>')[
                                  1].split(
                                  '</d:ДоговорКонтрагента_Key>')[1]

        return act_creation_schema
    else:
        provodka_schema = provodka_schema.split('<d:Ref_Key>')[0] + '<d:Ref_Key>' + mode + '</d:Ref_Key>' + \
                          provodka_schema.split('<d:Ref_Key>')[1].split('</d:Ref_Key>')[1]
        provodka_schema = provodka_schema.split('<d:НомерВходящегоДокумента>')[0] + '<d:НомерВходящегоДокумента>' + str(
            parsed_data[0]['Счет-фактура №']) + '</d:НомерВходящегоДокумента>' + \
                          provodka_schema.split('<d:НомерВходящегоДокумента>')[1].split('</d:НомерВходящегоДокумента>')[
                              1]
        provodka_schema = provodka_schema.split('<d:ДатаВходящегоДокумента>')[
                              0] + '<d:ДатаВходящегоДокумента>' + date_2 + '</d:ДатаВходящегоДокумента>' + \
                          provodka_schema.split('<d:ДатаВходящегоДокумента>')[1].split('</d:ДатаВходящегоДокумента>')[1]
        provodka_schema = provodka_schema.split('<d:ДокументОснование>')[
                              0] + '<d:ДокументОснование>' + mode + '</d:ДокументОснование>' + \
                          provodka_schema.split('<d:ДокументОснование>')[1].split('</d:ДокументОснование>')[1]
        provodka_schema = provodka_schema.split('<d:СуммаДокумента>')[0] + '<d:СуммаДокумента>' + \
                          parsed_data[0]['Сумма'].split('руб')[0] + '</d:СуммаДокумента>' + \
                          provodka_schema.split('<d:СуммаДокумента>')[1].split('</d:СуммаДокумента>')[1]

        provodka_schema = provodka_schema.split('<d:СуммаНДСДокумента>')[0] + '<d:СуммаНДСДокумента>' + \
                          re.sub(r'\,', '.', parsed_data[0]['В т.ч. НДС'].split(' руб')[0]) + '</d:СуммаНДСДокумента>' + \
                          provodka_schema.split('<d:СуммаНДСДокумента>')[1].split('</d:СуммаНДСДокумента>')[1]

        provodka_schema = provodka_schema.split('<d:СуммаДокументаКомиссия>')[0] + '<d:СуммаДокументаКомиссия>' + \
                          re.sub(r'\,', '.', parsed_data[0]['Сумма'].split('руб')[0]) + '</d:СуммаДокументаКомиссия>' + \
                          provodka_schema.split('<d:СуммаДокументаКомиссия>')[1].split('</d:СуммаДокументаКомиссия>')[1]
        nds = re.sub(r'\,', '.', parsed_data[0]['В т.ч. НДС'].split(' руб')[0])
        nds = re.sub(r'\s', '', nds)
        provodka_schema = provodka_schema.split('<d:СуммаНДСДокументаКомиссия>')[0] + '<d:СуммаНДСДокументаКомиссия>' + \
                          nds + '</d:СуммаНДСДокументаКомиссия>' + \
                          provodka_schema.split('<d:СуммаНДСДокументаКомиссия')[1].split(
                              '</d:СуммаНДСДокументаКомиссия>')[1]
        return provodka_schema


def response_sender_checker(body, address):
    response = requests.post(address, data=body.encode('utf-8'), headers=headers)
    response = response.content.decode('utf-8')
    if 'error' or 'exception' or 'Exception' in response:
        return False
    else:
        try:
            return response.split('<d:Ref_Key>')[1].split('</d:Ref_Key>')[0]
        except:
            print(response)


def main_buhgalter(acts):
    """
    Мы берем каждый счет из нашего списка, и ищем такой же в Document_СчетНаОплатуПокупателю.
    Если находим там его, значит счет поступил и можно делать проводку.
    Тут нам нужна только информация о компании, которая оплачивает.
    И нужно только ее название. Для этого мы находим запись в Document_СчетНаОплатуПокупателю и
    вытаскиваем КЛЮЧ компании. С этим ключем мы идем в Catalog_Контрагенты и находим название компании там.
    """
    print('Скачиваю контрагентов, их договора, поступленые счета-фактуры, текущие записи об актах')
    # with open('file.txt', 'a+') as file:
    #     file.write(';' + 'Скачиваю контрагентов, их договора, поступленые счета-фактуры, текущие записи об актах')
    scheta_oplat, scheta_oplat_dates = data_extractor_1C(
        addresses_1c['main_address'] + addresses_1c['schet_pokupatelu'])
    acts = acts
    companies = contragenti_extractor_1C(addresses_1c['main_address'] + addresses_1c['contragenti'])
    contragents_dogovors = get_contragents_dogovors()
    # with open('file.txt', 'a+') as file:
    #     file.write(';' + 'Скачал. Приступаю к записи инфы в 1С')
    sheets = google_spreadsheets()
    sheet_B = sheets.worksheet('Sheet6')
    data_sheet = sheets.worksheet('Sheet5')
    all_records = data_sheet.get_all_records()
    print("Скачал. Приступаю к записи инфы в 1С")
    scheta_old = []
    all_data = []
    for i in sheet_B.get_all_records():
        if i['Счета клиентосов'] != '':
            scheta_old.append(i['Счета клиентосов'])
    for n, i in enumerate(scheta_old):
        print(n)
        delete_flag = False
        for k, v in scheta_oplat.items():
            for value in v:
                if i in value:
                    print(i)
                    company = companies[k]
                    company_id = list(companies.keys())[list(companies.keys()).index(k)]
                    ### Скачиваем договора
                    current_data_for_docs = {}
                    for xk, xv in contragents_dogovors.items():
                        if company_id == xv[0]:
                            current_data_for_docs.update({xv[1]: xk})
                    ### скачали
                    dogovor = None
                    if len(current_data_for_docs) == 1:
                        dogovor = list(current_data_for_docs.values())[0]
                    else:
                        # Если длина договора больше 1 Пройдемся по ним и попробуем найти агентский
                        for names, docs in current_data_for_docs.items():
                            if 'Агентский договор' in names or 'Агентсткий договор' in names:
                                dogovor = docs
                                break
                            else:
                                # Если в списке нет агентского договора оставляем последний
                                dogovor = docs
                                continue
                    for d in all_records:
                        if d['Счет'] == i and str(d['Акт №']) not in acts:  # and count == 0:
                            indx = scheta_oplat[k].index(value)
                            date_for_comment = scheta_oplat_dates[k][indx]
                            all_data.append(d)
                            all_data[0].update({'Дата для коммента': date_for_comment})
                            body = request_act_body_filler(company, all_data, i, company_id, 'act', dogovor=dogovor)
                            # with open('file.txt', 'a+') as file:
                            #     file.write(';' + 'Создаю акт в 1С' + i)
                            print(i, 'Создаю акт в 1С')
                            print(body)
                            try:
                                # pass
                                response = requests.post(addresses_1c['main_address'] + addresses_1c['act_creation'],
                                                         data=body.encode('utf-8'), headers=headers)
                                response = response.content.decode('utf-8')
                                print(response)
                                guid_key = response.split('<d:Ref_Key>')[1].split('</d:Ref_Key>')[0]
                            except:
                                # pass
                                # with open('file.txt', 'a+') as file:
                                #     file.write(';' + 'Пробую второй раз')
                                timeout()
                                response = requests.post(addresses_1c['main_address'] + addresses_1c['act_creation'],
                                                         data=body.encode('utf-8'), headers=headers)
                                response = response.content.decode('utf-8')
                                print(response)
                                try:
                                    guid_key = response.split('<d:Ref_Key>')[1].split('</d:Ref_Key>')[0]
                                except:
                                    # with open('file.txt', 'a+') as file:
                                    #     file.write(';' + 'Шото пошло не так. продолжим')
                                    continue
                            # with open('file.txt', 'a+') as file:
                            #     file.write(';' + 'Акт создан. Заводим счет фактуру')
                            print('Акт создан. Заводим счет фактуру')
                            provodka = request_act_body_filler(company, all_data, i, None, guid_key)
                            all_data = []
                            success = response_sender_checker(provodka, addresses_1c['main_address'] + addresses_1c[
                                'schet_factura'])
                            print('Успех. Делаем проводки')
                            # with open('file.txt', 'a+') as file:
                            #     file.write(';' + 'Успех. Делаем проводки')
                            ### address = "https://login:pass@terminal.scloud.ru/base/odata/standard.odata/Document_ПоступлениеТоваровУслуг(guid'{}')/Post()".format(
                            ###     guid_key
                            ### )
                            ### requests.post(address)
                            delete_flag = False
                            # count += 1
                            if delete_flag:
                                print('И конено же удаляем запись в Гугл Доке')
                                # with open('file.txt', 'a+') as file:
                                #     file.write(';' + 'И конено же удаляем запись в Гугл Доке')
                                sheets = google_spreadsheets()
                                sheet_B = sheets.worksheet('Sheet6')
                                sheet_data = sheets.worksheet('Sheet5')
                                try:
                                    x = sheet_B.find(i)
                                except:
                                    print('Cell not found. Попробуйте перезаписать изформацию для счета в гугл доке')
                                    # with open('file.txt', 'a+') as file:
                                    #     file.write(
                                    #         ';' + 'Cell not found. Попробуйте перезаписать изформацию для счета в гугл доке')
                                    continue
                                sheet_B.update_cell(x.row, 1, '')
                                y = sheet_data.find(i)
                                for iii in range(1, 7):
                                    sheet_data.update_cell(y.row, iii, '')
                                try:
                                    with open('file.txt', 'a+') as file:
                                        file.write(
                                            ';' + 'Поищем другие акты с таким счетом')
                                    y = sheet_data.find(i)
                                    start_row = len(sheet_B.get_all_records()) + 2
                                    sheet_B.update_cell(start_row, 1, i)
                                    with open('file.txt', 'a+') as file:
                                        file.write(
                                            ';' + 'Нашли')
                                except:
                                    with open('file.txt', 'a+') as file:
                                        file.write(
                                            ';' + 'Не нашли')
                            else:
                                sheets = google_spreadsheets()
                                sheet_errors = sheets.worksheet('Sheet7')
                                start_row = len(sheet_errors.get_all_records()) + 2
                                sheet_B.update_cell(start_row, 1, i)
                                pass
                        elif str(d['Акт №']) in acts:
                            sheets = google_spreadsheets()
                            sheet_B = sheets.worksheet('Sheet6')
                            sheet_data = sheets.worksheet('Sheet5')
                            try:
                                x = sheet_B.find(i)
                            except:
                                pass
                            sheet_B.update_cell(x.row, 1, '')
                            try:
                                y = sheet_data.find(i)
                            except:
                                pass
                            try:
                                for iii in range(1, 7):
                                    sheet_data.update_cell(y.row, iii, '')
                            except:
                                pass
                            try:
                                y = sheet_data.find(i)
                                start_row = len(sheet_B.get_all_records()) + 2
                                sheet_B.update_cell(start_row, 1, i)
                            except:
                                continue
