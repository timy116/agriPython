'''
Created on 2018年6月29日

@author: so6370
'''
import xlrd

monthlyEmployee_dict = {}

def load_monthly_employee():
    for line in open('..\\..\\input\\106_MonthlyEmployee.txt', 'r', encoding = 'utf-8', errors = 'ignore'):
        sample_lsit = line.strip().split('\t')
        farm_id = sample_lsit[0].strip()
        monthlyEmployee_dict[farm_id] = sample_lsit

def load_insurance():
    wb = xlrd.open_workbook('..\\..\\input\\insurance.xlsx')
    sheet = wb.sheet_by_index(0)
    distinct_dict = {}
    
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        id = row[0]
        id_type = id + '-' + row[1]
        
        if not id_type in distinct_dict:
            value = int(row[2])
            type = int(row[1])
            
            if type == 60 or type == 66:
                pass
            
            else:
                distinct_dict[id_type] = value * 12
    
#     for e in distinct_dict:
#         print(e, ':', distinct_dict[e])
    
    
    annuity = [45, 48, 35, 36, 37, 38, 55, 56, 57, 59]
    sheet = wb.sheet_by_index(1)
    count = 0
    prev_id = ''
    prev_value = 0

load_insurance()



    
