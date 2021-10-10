import pandas as pd
import openpyxl

f = pd.read_csv('course.csv', header=None)
f.columns = ['Regno', 'Name', 'sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10', 'sub11',
             'sub12', 'sub13', 'sub14', 'sub15', 'sub16', 'sub17', 'sub18', 'sub19', 'sub20']

f.drop_duplicates(subset="Regno", keep='first', inplace=True)

d = f.sort_values(by=['sub1', 'sub2', 'sub3'], ascending=True)
SUBJECTList = ['t1-Financial Statement Analysis - Manaswee Samal', 't1-IT Consulting - Sriram Rajagopalan']
for SUBJECTName in SUBJECTList:
    f1 = d[(d['sub1'] == SUBJECTName) | (d['sub2'] == SUBJECTName) | (d['sub3'] == SUBJECTName) | (
                d['sub4'] == SUBJECTName) |
           (d['sub5'] == SUBJECTName) | (d['sub6'] == SUBJECTName) | (d['sub7'] == SUBJECTName) | (
                       d['sub8'] == SUBJECTName) | (d['sub9'] == SUBJECTName) |
           (d['sub10'] == SUBJECTName) | (d['sub11'] == SUBJECTName) | (d['sub12'] == SUBJECTName) | (
                       d['sub13'] == SUBJECTName) | (d['sub14'] == SUBJECTName) |
           (d['sub15'] == SUBJECTName) | (d['sub16'] == SUBJECTName) | (d['sub17'] == SUBJECTName) | (
                       d['sub18'] == SUBJECTName) | (d['sub19'] == SUBJECTName) |
           (d['sub20'] == SUBJECTName)]

    f1.index.name = SUBJECTName
    f2 = f1.filter(['Name'])

    for i in range(len(SUBJECTList)):
        if SUBJECTList[i] == SUBJECTName:
            f2.to_csv(SUBJECTName + '.csv', encoding='utf-8', index=False)
            f4 = pd.read_csv(SUBJECTName + '.csv')
            f4 = f2.rename(columns={'Name': SUBJECTName}, inplace=False)
            f4.to_csv(SUBJECTName + 'List.csv', encoding='utf-8', index=False)
l1 = pd.read_csv(SUBJECTList[0] + 'List.csv')
l2 = pd.read_csv(SUBJECTList[1] + 'List.csv')

