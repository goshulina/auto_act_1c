# -*- coding: utf-8 -*-
headers = {'Accept': 'application/atom+xml,application/xml',
 'Accept-Charset': 'UTF-8',
 'Content-Type': 'application/atom+xml',
 'DataServiceVersion': '3.0;NetFx',
 'MaxDataServiceVersion': '3.0;NetFx',
 'User-Agent': '1C-Enterprise'}

# Спросить у бухгалтера или оставить такую
UA = {
    1: 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    2: 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.1+ (KHTML, like Gecko) Version/10.0.0.1337 Mobile Safari/537.1+',
    3: 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Mobile Safari/537.36',
    4: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    5: 'Mozilla/5.0 (Android 4.4; Mobile; rv:46.0) Gecko/46.0 Firefox/46.0',
    6: 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    7: 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    8: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.31',
    9: 'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1',
    10: 'Mozilla/5.0 (Linux; U; Android 4.4.4; en-US; XT1022 Build/KXC21.5-40) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30'}
months = {'апреля': '04',
          'мая': '05',
          'июня': '06',
          'июля': '07',
          'августа': '08',
          'сентября': '09',
          'октября': '10',
          'ноября': '11',
          'декабря': '12',
          'января': '01',
          'февраля': '02',
          'марта': '03'}

months_inverse = {'04': 'апреле',
          '05': 'мае',
          '06': 'июне',
          '07': 'июле',
          '08': 'августе',
          '09': 'сентябре',
          '10': 'октябре',
          '11': 'ноябре',
          '12': 'декабре',
          '01': 'январе',
          '02': 'феврале',
          '03': 'марте'}

months_inverse_2 = {'4': '04',
                    '5': '05',
                    '6': '06',
                    '7': '07',
                    '8': '08',
                    '9': '09',
                    '10': '10',
                    '11': '11',
                    '12': '12',
                    '1': '01',
                    '2': '02',
                    '3': '03',
                    '13': '13',
                    '14': '14',
                    '15': '15',
                    '16': '16',
                    '17': '17',
                    '18': '18',
                    '19': '19',
                    '20': '20',
                    '21': '21',
                    '22': '22',
                    '23': '23',
                    '24': '24',
                    '25': '25',
                    '26': '26',
                    '27': '27',
                    '28': '28',
                    '29': '29',
                    '30': '30',
                    '31': '31',
                    }

addresses_1c = {
    'main_address': 'https://login:pass@terminal.scloud.ru/base/odata/standard.odata/',
    'contragenti': 'Catalog_Контрагенты',
    'schet_factura': 'Document_СчетФактураПолученный',
    'act_creation': 'Document_ПоступлениеТоваровУслуг',
    'schet_pokupatelu': 'Document_СчетНаОплатуПокупателю'
}

act_creation_schema = '''<entry><category term="StandardODATA.Document_ПоступлениеТоваровУслуг" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/><title type="text"/><author/><summary/><content type="application/xml"><m:properties xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"><d:DeletionMark>false</d:DeletionMark><d:Date>2018-07-07T07:00:00</d:Date><d:Posted>true</d:Posted><d:ВидОперации>ПокупкаКомиссия</d:ВидОперации><d:Организация_Key>cbb38ee1-01c0-11e8-80c4-0cc47ab29cf7</d:Организация_Key><d:Склад_Key>0d861b95-a705-11e5-ba67-3085a93ddca2</d:Склад_Key><d:ПодразделениеОрганизации_Key>00000000-0000-0000-0000-000000000000</d:ПодразделениеОрганизации_Key><d:Контрагент_Key>e5e0705f-01cc-11e8-8d25-00155d461204</d:Контрагент_Key><d:ДоговорКонтрагента_Key>e5e07060-01cc-11e8-8d25-00155d461204</d:ДоговорКонтрагента_Key><d:СпособЗачетаАвансов>Автоматически</d:СпособЗачетаАвансов><d:СчетУчетаРасчетовСКонтрагентом_Key>c7fd5bc2-a704-11e5-ba67-3085a93ddca2</d:СчетУчетаРасчетовСКонтрагентом_Key><d:СчетУчетаРасчетовПоАвансам_Key>c7fd5bc3-a704-11e5-ba67-3085a93ddca2</d:СчетУчетаРасчетовПоАвансам_Key><d:СчетУчетаРасчетовПоТаре_Key>c7fd5c28-a704-11e5-ba67-3085a93ddca2</d:СчетУчетаРасчетовПоТаре_Key><d:ВалютаДокумента_Key>e29ec0ec-a704-11e5-ba67-3085a93ddca2</d:ВалютаДокумента_Key><d:СчетНаОплатуПоставщика_Key>00000000-0000-0000-0000-000000000000</d:СчетНаОплатуПоставщика_Key><d:НомерВходящегоДокумента>81685491</d:НомерВходящегоДокумента><d:ДатаВходящегоДокумента>2018-06-20T00:00:00</d:ДатаВходящегоДокумента><d:Грузоотправитель_Key>00000000-0000-0000-0000-000000000000</d:Грузоотправитель_Key><d:Грузополучатель_Key>00000000-0000-0000-0000-000000000000</d:Грузополучатель_Key><d:Ответственный_Key>d4ab5e80-67ee-11e8-9732-00155d462203</d:Ответственный_Key><d:Комментарий>ГШН-бухгалерБ-842394971-1 от 20 июня 2018</d:Комментарий><d:КратностьВзаиморасчетов>1</d:КратностьВзаиморасчетов><d:КурсВзаиморасчетов>1</d:КурсВзаиморасчетов><d:НДСВключенВСтоимость>false</d:НДСВключенВСтоимость><d:СуммаВключаетНДС>true</d:СуммаВключаетНДС><d:СуммаДокумента>3960.00</d:СуммаДокумента><d:ТипЦен_Key>00000000-0000-0000-0000-000000000000</d:ТипЦен_Key><d:РучнаяКорректировка>false</d:РучнаяКорректировка><d:УдалитьУчитыватьНДС>false</d:УдалитьУчитыватьНДС><d:УдалитьПредъявленСчетФактура>false</d:УдалитьПредъявленСчетФактура><d:УдалитьНомерВходящегоСчетаФактуры/><d:УдалитьДатаВходящегоСчетаФактуры>0001-01-01T00:00:00</d:УдалитьДатаВходящегоСчетаФактуры><d:УдалитьНДСПредъявленКВычету>false</d:УдалитьНДСПредъявленКВычету><d:УдалитьКодВидаОперации/><d:УдалитьКодСпособаПолучения>0</d:УдалитьКодСпособаПолучения><d:КодВидаТранспорта></d:КодВидаТранспорта><d:НДСНеВыделять>false</d:НДСНеВыделять><d:ТТНВходящаяЕГАИС_Key>00000000-0000-0000-0000-000000000000</d:ТТНВходящаяЕГАИС_Key><d:ЕстьМаркируемаяПродукцияГИСМ>false</d:ЕстьМаркируемаяПродукцияГИСМ><d:МОЛ_Key>00000000-0000-0000-0000-000000000000</d:МОЛ_Key><d:МестонахождениеОС_Key>00000000-0000-0000-0000-000000000000</d:МестонахождениеОС_Key><d:ГруппаОС/><d:СпособОтраженияРасходовПоАмортизации_Key>00000000-0000-0000-0000-000000000000</d:СпособОтраженияРасходовПоАмортизации_Key><d:ОбъектыПредназначеныДляСдачиВАренду>false</d:ОбъектыПредназначеныДляСдачиВАренду><d:Оборудование m:type="Collection(StandardODATA.Document_ПоступлениеТоваровУслуг_Оборудование_RowType)"/><d:ОбъектыСтроительства m:type="Collection(StandardODATA.Document_ПоступлениеТоваровУслуг_ОбъектыСтроительства_RowType)"/><d:Товары m:type="Collection(StandardODATA.Document_ПоступлениеТоваровУслуг_Товары_RowType)"/><d:Услуги m:type="Collection(StandardODATA.Document_ПоступлениеТоваровУслуг_Услуги_RowType)"/><d:ВозвратнаяТара m:type="Collection(StandardODATA.Document_ПоступлениеТоваровУслуг_ВозвратнаяТара_RowType)"/><d:ЗачетАвансов m:type="Collection(StandardODATA.Document_ПоступлениеТоваровУслуг_ЗачетАвансов_RowType)"/><d:АгентскиеУслуги m:type="Collection(StandardODATA.Document_ПоступлениеТоваровУслуг_АгентскиеУслуги_RowType)"><d:element m:type="StandardODATA.Document_ПоступлениеТоваровУслуг_АгентскиеУслуги_RowType"><d:LineNumber>1</d:LineNumber><d:Номенклатура_Key>cd5b7e2f-0453-11e8-a837-00155d461301</d:Номенклатура_Key><d:Содержание>Размещение рекламных материалов на проекте Яндекс.Директ в июне 2018 года</d:Содержание><d:Количество>1</d:Количество><d:Цена>3960.00</d:Цена><d:Сумма>3960.00</d:Сумма><d:СтавкаНДС>НДС18</d:СтавкаНДС><d:СуммаНДС>604.07</d:СуммаНДС><d:Контрагент_Key>e5e07079-01cc-11e8-8d25-00155d461204</d:Контрагент_Key><d:ДоговорКонтрагента_Key>e5e0707a-01cc-11e8-8d25-00155d461204</d:ДоговорКонтрагента_Key><d:СчетРасчетов_Key>c7fd5c2e-a704-11e5-ba67-3085a93ddca2</d:СчетРасчетов_Key></d:element></d:АгентскиеУслуги><d:ОсновныеСредства m:type="Collection(StandardODATA.Document_ПоступлениеТоваровУслуг_ОсновныеСредства_RowType)"/></m:properties></content></entry>'''

provodka_schema = '''<entry><category term="StandardODATA.Document_СчетФактураПолученный" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/><title type="text"/><author/><summary/><content type="application/xml"><m:properties xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"><d:Ref_Key>29b2686c-8bde-11e8-80ce-0cc47ab4051b</d:Ref_Key><d:DataVersion>AAAABAAAAAE=</d:DataVersion><d:DeletionMark>false</d:DeletionMark><d:Posted>true</d:Posted><d:Организация_Key>cbb38ee1-01c0-11e8-80c4-0cc47ab29cf7</d:Организация_Key><d:ВидСчетаФактуры>НаПоступление</d:ВидСчетаФактуры><d:Контрагент_Key>e5e0705f-01cc-11e8-8d25-00155d461204</d:Контрагент_Key><d:ДоговорКонтрагента_Key>e5e07060-01cc-11e8-8d25-00155d461204</d:ДоговорКонтрагента_Key><d:НомерВходящегоДокумента>20180707000229</d:НомерВходящегоДокумента><d:ДатаВходящегоДокумента>2018-06-20T00:00:00</d:ДатаВходящегоДокумента><d:Исправление>false</d:Исправление><d:НомерИсправления>0</d:НомерИсправления><d:ДатаИсправления>0001-01-01T00:00:00</d:ДатаИсправления><d:ИсправляемыйСчетФактура_Key>00000000-0000-0000-0000-000000000000</d:ИсправляемыйСчетФактура_Key><d:НомерИсходногоДокумента/><d:ДатаИсходногоДокумента>0001-01-01T00:00:00</d:ДатаИсходногоДокумента><d:УдалитьУчитыватьИсправлениеИсходногоДокумента>false</d:УдалитьУчитыватьИсправлениеИсходногоДокумента><d:УдалитьНомерИсправленияИсходногоДокумента>0</d:УдалитьНомерИсправленияИсходногоДокумента><d:УдалитьДатаИсправленияИсходногоДокумента>0001-01-01T00:00:00</d:УдалитьДатаИсправленияИсходногоДокумента><d:НДСПредъявленКВычету>true</d:НДСПредъявленКВычету><d:Продавец_Key>00000000-0000-0000-0000-000000000000</d:Продавец_Key><d:Комитент_Key>00000000-0000-0000-0000-000000000000</d:Комитент_Key><d:ДоговорКомитента_Key>00000000-0000-0000-0000-000000000000</d:ДоговорКомитента_Key> <d:ДокументОснование>29b2686c-8bde-11e8-80ce-0cc47ab4051b</d:ДокументОснование><d:ДокументОснование_Type>StandardODATA.Document_ПоступлениеТоваровУслуг</d:ДокументОснование_Type> <d:СчетФактураБезНДС>false</d:СчетФактураБезНДС><d:КодВидаОперации>01</d:КодВидаОперации><d:КодСпособаПолучения>1</d:КодСпособаПолучения><d:СуммаДокумента>3540.00</d:СуммаДокумента><d:СуммаУвеличение>0</d:СуммаУвеличение><d:СуммаУменьшение>0</d:СуммаУменьшение><d:СуммаНДСДокумента>540.00</d:СуммаНДСДокумента><d:СуммаНДСУвеличение>0</d:СуммаНДСУвеличение><d:СуммаНДСУменьшение>0</d:СуммаНДСУменьшение><d:ВалютаДокумента_Key>e29ec0ec-a704-11e5-ba67-3085a93ddca2</d:ВалютаДокумента_Key><d:Ответственный_Key>d4ab5e80-67ee-11e8-9732-00155d462203</d:Ответственный_Key><d:Комментарий/><d:РучнаяКорректировка>false</d:РучнаяКорректировка><d:СформированПриВводеНачальныхОстатковНДС>false</d:СформированПриВводеНачальныхОстатковНДС><d:УдалитьКорректировочныйСчетФактура>false</d:УдалитьКорректировочныйСчетФактура><d:УдалитьНаАванс>false</d:УдалитьНаАванс><d:БланкСтрогойОтчетности>false</d:БланкСтрогойОтчетности><d:КППКонтрагента/><d:СводныйКорректировочный>false</d:СводныйКорректировочный><d:ПредставлениеНомера>20180620000377</d:ПредставлениеНомера><d:ВозвратЧерезКомиссионера>false</d:ВозвратЧерезКомиссионера><d:Субкомиссионер_Key>00000000-0000-0000-0000-000000000000</d:Субкомиссионер_Key><d:СчетФактураВыданныйПокупателю_Key>00000000-0000-0000-0000-000000000000</d:СчетФактураВыданныйПокупателю_Key><d:СуммаДокументаКомиссия>3540.00</d:СуммаДокументаКомиссия><d:СуммаНДСДокументаКомиссия>540.00</d:СуммаНДСДокументаКомиссия><d:СуммаУвеличениеКомиссия>0</d:СуммаУвеличениеКомиссия><d:СуммаУменьшениеКомиссия>0</d:СуммаУменьшениеКомиссия><d:СуммаНДСУвеличениеКомиссия>0</d:СуммаНДСУвеличениеКомиссия><d:СуммаНДСУменьшениеКомиссия>0</d:СуммаНДСУменьшениеКомиссия><d:СводныйКомиссионный>false</d:СводныйКомиссионный><d:ИсправлениеСобственнойОшибки>false</d:ИсправлениеСобственнойОшибки><d:НомерВходящегоДокументаДоИзменения/><d:ДатаВходящегоДокументаДоИзменения>0001-01-01T00:00:00</d:ДатаВходящегоДокументаДоИзменения><d:НомерИсправленияДоИзменения>0</d:НомерИсправленияДоИзменения><d:ДатаИсправленияДоИзменения>0001-01-01T00:00:00</d:ДатаИсправленияДоИзменения><d:КодВидаОперацииДоИзменения/><d:ИННКонтрагентаДоИзменения/><d:КППКонтрагентаДоИзменения/><d:ИННКонтрагента/><d:КодВидаОперацииНаУменьшение/><d:КодВидаОперацииНаУменьшениеДоИзменения/><d:ДокументыОснования m:type="Collection(StandardODATA.Document_СчетФактураПолученный_ДокументыОснования_RowType)"></d:ДокументыОснования><d:Авансы m:type="Collection(StandardODATA.Document_СчетФактураПолученный_Авансы_RowType)"/><d:СчетаФактурыВыданныеПокупателям m:type="Collection(StandardODATA.Document_СчетФактураПолученный_СчетаФактурыВыданныеПокупателям_RowType)"/><d:Продавцы m:type="Collection(StandardODATA.Document_СчетФактураПолученный_Продавцы_RowType)"/><d:ПлатежноРасчетныеДокументы m:type="Collection(StandardODATA.Document_СчетФактураПолученный_ПлатежноРасчетныеДокументы_RowType)"/></m:properties></content></entry>'''