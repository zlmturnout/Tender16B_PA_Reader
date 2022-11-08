import os, time, datetime, random
# import pandas and numpy
import pandas as pd
import numpy as np
import sqlite3

"""
Notes:
    data form for storage and process
time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
"""

dict_data = {'Energy': [230, 231, 232, 234, 234, 235],
             'RBV_Energy': [230.001, 231.002, 231.998, 233.002, 233.999, 235.0001],
             'RBV_MR': [10000, 10002, 10005, 10006, 10025, 10036],
             'RBV_GR': [60010, 60025, 60035, 60058, 60096, 60125],
             'Counts': [1, 0, 24, 35, 12, 16],
             'I0_V_PD': [2.5, 2.3, 2.6, 2.9, 3.1, 2.4],
             'I0_V_Au': [1.5, 2.1, 2.2, 2.8, 1.1, 1.8],
             'I0_V_Sample': [1.5, 1.6, 1.8, 2.0, 2.1, 1.6],
             'Time_Stamp': ['2021-04-30 15:47:11', '2021-04-30 15:47:15', '2021-04-30 15:47:18', '2021-04-30 15:47:23',
                            '2021-04-30 15:47:26', '2021-04-30 15:47:30']}
# data from Monchromator with timestamp
Mono_data = {'Energy': [230, 231, 232, 234, 234, 235],
             'RBV_Energy': [230.001, 231.002, 231.998, 233.002, 233.999, 235.0001],
             'RBV_MR': [10000, 10002, 10005, 10006, 10025, 10036],
             'RBV_GR': [60010, 60025, 60035, 60058, 60096, 60125],
             'Time_Stamp': ['2021-04-30 15:47:11', '2021-04-30 15:47:15', '2021-04-30 15:47:18', '2021-04-30 15:47:23',
                            '2021-04-30 15:47:26', '2021-04-30 15:47:30']
             }
# data from counter 996 with timestamp
Counter_data = {'Counts': [1, 0, 24, 35, 12, 16],
                'Time_Stamp': ['2021-04-30 15:47:11', '2021-04-30 15:47:15', '2021-04-30 15:47:18',
                               '2021-04-30 15:47:23',
                               '2021-04-30 15:47:26', '2021-04-30 15:47:30']
                }

# data from PD/Au convert via ADC with timestamp
I0_data = {'I0_V_PD': [2.5, 2.3, 2.6, 2.9, 3.1, 2.4],
           'I0_V_Au': [1.5, 2.1, 2.2, 2.8, 1.1, 1.8],
           'I0_V_Sample': [1.5, 1.6, 1.8, 2.0, 2.1, 1.6],
           'Time_Stamp': ['2021-04-30 15:47:11', '2021-04-30 15:47:15', '2021-04-30 15:47:18', '2021-04-30 15:47:23',
                          '2021-04-30 15:47:26', '2021-04-30 15:47:30']}


def dict_to_excel(data_dict: dict, path, filename):
    """
    save dict data to txt file in path/filename
    :param dic:
    :param path:
    :param filename:
    :return:
    """
    m = 1
    new_dict = {}
    file_in_path = os.path.join(path, filename)
    # change to the data from to standard dict {'key': pd.Series([list],index=[index])}
    for key in data_dict:
        num = len(data_dict[key])
        new_dict[key] = pd.Series(list(data_dict[key]), index=list(range(num)))
    pd_data = pd.DataFrame(new_dict)
    # excel writer
    excel_writer = pd.ExcelWriter(file_in_path)
    pd_data.to_excel(excel_writer)
    excel_writer.save()
    print('save to excel xlsx file successfully')


def dict_to_csv(data_dict: dict, path, filename:str='test.csv'):
    """
    save dict data to txt file in path/filename
    :param data_dict:
    :param path:
    :param filename: default='test.xlsx'
    :return:
    """
    # check path
    if os.path.isdir(path):
        new_path=path
    else:
        new_path=os.getcwd()
    m = 1
    new_dict = {}
    file_in_path = os.path.join(new_path, filename)
    # change to the data from to standard dict {'key': pd.Series([list],index=[index])}
    for key in data_dict:
        num = len(data_dict[key])
        new_dict[key] = pd.Series(list(data_dict[key]), index=list(range(num)))
    pd_data = pd.DataFrame(new_dict)
    # excel writer
    pd_data.to_csv(file_in_path)
    print('save to csv file successfully')

def dict_to_json(data_dict: dict, path, filename:str='test.json'):
    """
    save dict data to txt file in path/filename
    :param data_dict:
    :param path:
    :param filename: default='test.xlsx'
    :return:
    """
    # check path
    if os.path.isdir(path):
        new_path=path
    else:
        new_path=os.getcwd()
    m = 1
    new_dict = {}
    file_in_path = os.path.join(new_path, filename)
    # change to the data from to standard dict {'key': pd.Series([list],index=[index])}
    for key in data_dict:
        num = len(data_dict[key])
        new_dict[key] = pd.Series(list(data_dict[key]), index=list(range(num)))
    pd_data = pd.DataFrame(new_dict)
    # excel writer
    pd_data.to_json(file_in_path)
    print('save to csv file successfully')
