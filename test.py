# -*- coding: utf-8 -*-
from google_spreadsheet_DB import send_infa, google_spreadsheets, list_maker
from buhgalter import get_current_pokupki, main_buhgalter, get_contragents_dogovors# , data_extractor_1C, contragenti_extractor_1C
# from data_temp import *
# import requests
# import xml.etree.ElementTree as ET
from tqdm import tqdm
import time
import numpy as np


def timeout():
    for i in tqdm(range(3)):
        time.sleep(np.random.choice(list(range(1, 3))))


list_maker()
# try:
#     acts = get_current_pokupki()
# except:
#     timeout()
#     acts = get_current_pokupki()
# main_buhgalter(acts)
