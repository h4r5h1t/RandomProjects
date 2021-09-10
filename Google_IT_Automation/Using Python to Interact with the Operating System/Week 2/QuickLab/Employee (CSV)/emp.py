'''
For this lab, imagine you are an IT Specialist at a 
medium-sized company. 
The Human Resources Department at your company wants 
you to find out how many people are in each department. 
You need to write a Python script that reads a CSV 
file containing a list of the employees in the 
organization, counts how many people are in 
each department, and then 
generates a report using this information. 
The output of this script will be a plain text file. 
'''
'''
DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter. If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as the keys

We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object.

Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance. We will now register a dialect empDialect.
csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
'''
#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
	with open (csv_file_location) as file:
		csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
		employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
		employee_list = []
		for data in employee_file:
			employee_list.append(data)
		return employee_list

employee_list = read_employees("/home/gizmocom/Desktop/Vasvai/Programs/Py/Google Automation/Employee (CSV)/employees.csv")
#print(employee_list) -- /home/<username>/data/employees.csv

def process_data(employee_list):
	department_list = []
	for employee_data in employee_list:
		department_list.append(employee_data['Department'])
	department_data = {}
	for department_name in set(department_list):
		department_data[department_name] = department_list.count(department_name)
	return department_data

dictionary = process_data(employee_list)
#print(dictionary)

def write_report(dictionary, report_file):
	with open(report_file, "w+") as f:
	for k in sorted(dictionary):
		f.write(str(k)+':'+str(dictionary[k])+'\n')

write_report(dictionary, '/home/gizmocom/Desktop/Vasvai/Programs/Py/Google Automation/Employee (CSV)/report.txt')
