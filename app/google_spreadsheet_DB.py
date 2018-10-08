# -*- coding: utf-8 -*-
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dateutil import parser
from app.data_temp import months


def google_spreadsheets():
    scope = ['https://spreadsheets.google.com/feeds']
    cred = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(cred)
    sheets = client.open('adjoy')
    return sheets


def last_date_sercher():
    sheets = google_spreadsheets()
    sheet_B = sheets.worksheet('Sheet5')
    checker = [parser.parse('1995-03-22', dayfirst=False)]
    for i in sheet_B.get_all_records():
        try:
            ii = parser.parse(i['Дата'].split()[2] + '-' + months[i['Дата'].split()[1]] + '-' + i['Дата'].split()[0],
                              dayfirst=False)
            if ii > checker[0]:
                checker[0] = ii
        except:
            continue
    return checker


def list_maker():
    sheets = google_spreadsheets()
    sheet_B = sheets.worksheet('Sheet6')
    sheet_data = sheets.worksheet('Sheet5')
    all_scheta = []
    old_scheta = []
    for i in sheet_data.get_all_records():
        all_scheta.append(i['Счет'])
    all_scheta = set(all_scheta)
    if sheet_B.get_all_records()[0]['Счета клиентосов'] == 'Ебошь всех клиентосов сначала':
        sheet_B.update_cell(2, 1, '')
        for item in all_scheta:
            start_row = len(sheet_B.get_all_records()) + 2
            sheet_B.update_cell(start_row, 1, item)
    else:
        for i in sheet_B.get_all_records():
            if i != '':
                old_scheta.append(i['Счета клиентосов'])
        old_scheta = set(old_scheta)
        scheta_to_append = list(all_scheta - old_scheta)
        send_infa(scheta_to_append, 'Sheet6')

def send_infa(infa_page, page, acts=None):
    sheets = google_spreadsheets()
    sheet = sheets.worksheet(page)
    flag = False
    if acts != None:
        for l in infa_page:
            if type(l) == list:
                start_row = len(sheet.get_all_records()) + 2
                for n, item in enumerate(l):
                    if n == 0:
                        try:
                            x = sheet.find(item)
                            flag = False
                        except:
                            flag = True
                    if n == 0 and item in acts:
                        break
                    else:
                        if flag:
                            sheet.update_cell(start_row, n + 1, item)
            else:
                if l in acts:
                    break
                else:
                    start_row = len(sheet.get_all_records()) + 2
                    sheet.update_cell(start_row, 1, l)
    else:
        for l in infa_page:
            if type(l) == list:
                start_row = len(sheet.get_all_records()) + 2
                for n, item in enumerate(l):
                    if n == 0:
                        try:
                            x = sheet.find(item)
                            flag = False
                        except:
                            flag = True
                    if flag:
                        sheet.update_cell(start_row, n + 1, item)
            else:
                start_row = len(sheet.get_all_records()) + 2
                sheet.update_cell(start_row, 1, l)


