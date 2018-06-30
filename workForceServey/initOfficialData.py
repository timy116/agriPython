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
        farm_id = row[0]
        id_type = farm_id + '-' + row[1]
        
        if not id_type in distinct_dict:
            value = int(row[2])
            insurance_type = int(row[1])
            
            if insurance_type == 60 or insurance_type == 66:
                pass
            
            else:
                distinct_dict[id_type] = value * 12
    
#     for e in distinct_dict:
#         print(e, ':', distinct_dict[e])
    del distinct_dict
    
    annuity = [45, 48, 35, 36, 37, 38, 55, 56, 57, 59]
    sheet = wb.sheet_by_index(1)
    count = 0
    prev_id = ''
    prev_value = 0
    
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        farm_id = row[0]
        insurance_type = int(row[1])
        value = int(row[2])
        
        if prev_id == '':
            prev_id = farm_id
    
        if insurance_type in annuity:
            pay = value
            count += 1
            
            if not id == prev_id:
                prev_id = farm_id
                prev_value = value
                pay = prev_value * (13 - count)
                count = 0
            
            else:
                pass
    
    sheet = wb.sheet_by_index(2)
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        farm_id = row[0]
        value = row[2]
        
    sheet = wb.sheet_by_index(3)
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        farm_id = row[0]
        value = row[2]
        
load_insurance()


    
