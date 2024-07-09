import requests
import _constants as c
import _utils as u
import csv

# SERVICES
LOGFILE = c.LOGFILE
INIFILE = c.INIFILE
DEBUG = c.DEBUG
CODEPAGE = c.CODEPAGE

# SH5 WEB API CONNECT
HOST = c.SH5_WEB_API_HOST
PORT = c.SH5_WEB_API_PORT
USER = c.SH5_USER
PSW = c.SH5_PSW

# CSV FOLDER
PATH = c.CSV_PATH

# SH5 DICTS PROCEDURES
DEPARTS = c.SH5_DEPARTS
GGROUPS = c.SH5_GGROUPS
GOODS = c.SH5_GOODS
CORRS = c.SH5_CORRS
GOODSITEM = c.SH5_GOODSITEM
GDOCS = c.SH5_GDOCS


# SH5 DEFINITIONS
def sh5_api_request_exec(prc_name: str, params: list) -> dict:
    """ SH5 WEB API: exec_request function - sh5exec. """

    func_name = u.get_func_name()
    try:
        request = requests.post(
            url=f'http://{HOST}:{PORT}/api/sh5exec',
            json={
                "UserName": USER,
                "Password": PSW,
                "ProcName": prc_name,
                "Input": params
            }
        )
        request.raise_for_status()
        result = request.json()

    except Exception as e:
        u.write_log(func_name, True, e)
    else:
        if DEBUG:
            u.write_log(func_name, False, f"SH5 API request is succesful:\n'{result}'.")

        return result


def departs_to_csv(json_data: dict):
    """ Departs json to CSV. """

    func_name = u.get_func_name()
    for table in json_data['shTable']:
        if table['head'] == '106':
            fields = table['fields']
            values = list(zip(*table['values']))  # Transpose the list of lists to match fields

            with open(f'{PATH}/{DEPARTS}.csv', 'w', newline='', encoding=CODEPAGE) as file:
                writer = csv.writer(file)
                writer.writerow(fields)  # Write the header
                writer.writerows(values)  # Write the data rows

            if DEBUG:
                u.write_log(func_name, False, f"Data has been written to Departs.csv'.")


def ggroups_to_csv(json_data: dict):
    """ GGroups json to CSV. """

    func_name = u.get_func_name()
    for table in json_data['shTable']:
        if table['head'] == '209':
            fields = table['fields']
            values = list(zip(*table['values']))  # Transpose the list of lists to match fields

            with open(f'{PATH}/{GGROUPS}.csv', 'w', newline='', encoding=CODEPAGE) as file:
                writer = csv.writer(file)
                writer.writerow(fields)  # Write the header
                writer.writerows(values)  # Write the data rows

            if DEBUG:
                u.write_log(func_name, False, f"Data has been written to GGroups.csv'.")


def corrs_to_csv(json_data: dict):
    """ Corrs json to CSV. """

    func_name = u.get_func_name()
    for table in json_data['shTable']:
        if table['head'] == '107':
            fields = table['fields']
            values = list(zip(*table['values']))  # Transpose the list of lists to match fields

            with open(f'{PATH}/{CORRS}.csv', 'w', newline='', encoding=CODEPAGE) as file:
                writer = csv.writer(file)
                writer.writerow(fields)  # Write the header
                writer.writerows(values)  # Write the data rows

            if DEBUG:
                u.write_log(func_name, False, f"Data has been written to Corrs.csv'.")


def goods_to_csv(json_data: dict):
    """ Goods json to CSV. """

    func_name = u.get_func_name()
    for table in json_data['shTable']:
        if table['head'] == '210':
            fields = table['fields']
            values = list(zip(*table['values']))  # Transpose the list of lists to match fields

            with open(f'{PATH}/{GOODS}.csv', 'w', newline='', encoding=CODEPAGE) as file:
                writer = csv.writer(file)
                writer.writerow(fields)  # Write the header
                writer.writerows(values)  # Write the data rows

            if DEBUG:
                u.write_log(func_name, False, f"Data has been written to GGroups.csv'.")


def goodsitem_to_csv(json_data: dict):
    """ GoodsItem json to CSV. """

    func_name = u.get_func_name()
    for table in json_data['shTable']:
        if table['head'] == '210':
            fields = table['fields']
            values = list(zip(*table['values']))  # Transpose the list of lists to match fields

            with open(f'{PATH}/{GOODSITEM}.csv', 'w', newline='', encoding=CODEPAGE) as file:
                writer = csv.writer(file)
                writer.writerow(fields)  # Write the header
                writer.writerows(values)  # Write the data rows

            if DEBUG:
                u.write_log(func_name, False, f"Data has been written to GGroups.csv'.")


def gdocs_to_csv(json_data: dict):
    """ GoodsItem json to CSV. """

    func_name = u.get_func_name()
    for table in json_data['shTable']:
        if table['head'] == '111':
            fields = table['fields']
            values = list(zip(*table['values']))  # Transpose the list of lists to match fields

            with open(f'{PATH}/{GDOCS}.csv', 'w', newline='', encoding=CODEPAGE) as file:
                writer = csv.writer(file)
                writer.writerow(fields)  # Write the header
                writer.writerows(values)  # Write the data rows

            if DEBUG:
                u.write_log(func_name, False, f"Data has been written to GGroups.csv'.")


# DEBUG ------------------------------------------------------------------------------------

# Запрос и запись подразделений / складов
# departs = sh5_api_request_exec(DEPARTS, [])
# print(departs)
# departs_to_csv(departs)

# Запрос и запись групп товаров
# ggroups = sh5_api_request_exec(GGROUPS, [])
# print(ggroups)
# ggroups_to_csv(ggroups)

# Запрос и запись корреспондентов
# corrs = sh5_api_request_exec(CORRS, [])
# print(corrs)
# corrs_to_csv(corrs)

# Запрос и запись товаров по rid-у группы товаров
# ggroup_rid = 5
# goods_params = [
#     {
#         "head": "209",
#         "original": ["1"],  # RID товарной группы
#         "values": [
#             [ggroup_rid]  # значение RID
#         ]
#
#     }
# ]
# goods = sh5_api_request_exec(GOODS, goods_params)
# print(goods)
# goods_to_csv(goods)

# Запрос и запись товара по его rid-у
# goodsitem_rid = 785
# goodsitem_params = [
#     {
#         "head": "210",
#         "original": ["1"],  # RID товара
#         "values": [
#             [goodsitem_rid]  # значение RID
#         ]
#
#     }
# ]
# goodsitem = sh5_api_request_exec(GOODSITEM, goodsitem_params)
# print(goodsitem)
# goodsitem_to_csv(goodsitem)

# Запрос списка всех накладных
# gdocs = sh5_api_request_exec(GDOCS, [])
# print(gdocs)
# gdocs_to_csv(gdocs)

# Запрос списка накладных начиная с даты
# start_date = '2024-05-23'
# gdocs_startdate_params = [
#     {
#         "head": "108",
#         "original": ["1"],  # RID товара
#         "values": [
#             [start_date]  # значение RID
#         ]
#
#     }
# ]
# gdocs = sh5_api_request_exec(GDOCS, gdocs_startdate_params)
# print(gdocs)
# gdocs_to_csv(gdocs)

# Запрос списка накладных за период
start_date = '2024-05-23'
stop_date = '2024-06-21'
gdocs_dateperiod_params = [
    {
        "head": "108",
        "original": ["1", "2", "6"],
        "values": [
            [start_date],
            [stop_date],
            ["1", "8"]
        ]

    }
]
gdocs = sh5_api_request_exec(GDOCS, gdocs_dateperiod_params)
print(gdocs)
gdocs_to_csv(gdocs)
