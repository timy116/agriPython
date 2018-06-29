'''
Created on 2018年6月29日

@author: so6370
'''

monthlyEmployee_dict = {}

def load_monthly_employee():
    for line in open('..\\..\\input\\106_MonthlyEmployee.txt', 'r', encoding = 'utf-8', errors = 'ignore'):
        sample_lsit = line.strip().split('\t')
        farm_id = sample_lsit[0].strip()
        monthlyEmployee_dict[farm_id] = sample_lsit


load_monthly_employee()

# for e in monthlyEmployee_dict:
#     print(e, ':', monthlyEmployee_dict[e])
