import csv



emp_list = []
with open ("/home/gizmocom/Desktop/employees.csv") as file:
	emp = csv.DictReader(file)
	for f in emp:
		emp_list.append(f)
dep = []
for f in emp_list:
	dep.append(f[" Department"].strip())
d = {}
for a in set(dep):
	d[a] = dep.count(a)

with open ("/home/gizmocom/Desktop/report.txt","a+") as file:
	for a in d:
		file.write("{}: {}\n".format(a,d[a]))
		

