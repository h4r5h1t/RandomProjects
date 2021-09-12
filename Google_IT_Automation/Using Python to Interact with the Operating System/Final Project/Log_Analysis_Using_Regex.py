'''

\w{3} [123][0-9]? [0-9][012]?:[0-5][0-9]:[0-5][0-9] [\w.]* ticky: (?P<event>\w+):? (?P<msg>[\w ]+) \[?#?(?P<tno>[\d]+)?\]?\s?\((?P<user>\w+)\)


re.search(r"ticky: ERROR: ([\w ]*) ", line)

re.search(r"ticky: INFO: ([\w ]*) ", line)
ticky: INFO:? ([\w ]+).*\((\w+)\)

ticky: (\w+):? ([\w ]+).*\((\w+)\)

\w.*ticky: (\w+):? ([\w ]+).*\((\w+)\)


\w.*ticky: ERROR:? (P?<error>[\w ]+).*\((?P<user>\w+)\)

1) For ERROR MSG (used error.group(1))
error = re.search(r"ticky: ERROR[: ]+([\w ]+).*", line)

2) For USER used (user.group('user'))
user = re.search(r"ticky: (?P<event>\w+).*\((?P<user>\w+)\)", line)



sorted(fruit.items())

import operator
sorted(fruit.items(), key=operator.itemgetter(0)) #based on key
sorted(fruit.items(), key=operator.itemgetter(1)) #based on value
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)

Full Name, Email Address
Blossom Gill, blossom@abc.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@abc.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@abc.edu
Aurora Grant, enim.non@abc.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@abc.edu
Simon Rivera, sri@abc.edu
Benedict Pacheco, bpacheco@abc.edu
Maisie Hendrix, mai.hendrix@abc.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@abc.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@abc.edu
Bree Campbell, breee@utnisia.net




sudo chmod  o+w /var/www/html
./csv_to_html.py user_emails.csv /var/www/html/<html-filename>.html

[linux-instance-external-IP]/[html-filename].html

'''


#!/usr/bin/env python3
import re
import csv
import operator

error_messages = {}
per_user = {}
logfile =r"/home/student-00-ac1e85f030cc/syslog.log"
pattern = r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"

with open(logfile, "r") as f:
	for line in f:
		result = re.search(pattern, line)
		if result is None:
			continue
		if result.groups()[0] == "INFO":
			category = result.groups()[0]
			message = result.groups()[1]
			name = str(result.groups()[2])[1:-1]
			if name in per_user:
				user = per_user[name]
				user[category] += 1
			else:
				per_user[name] = {'INFO':1, 'ERROR':0}
		if result.groups()[0] == "ERROR":
			category = result.groups()[0]
			message = result.groups()[1]
			name = str(result.groups()[2])[1:-1]
			error_messages[message] = error_messages.get(message, 0) + 1
			if name in per_user:
				user = per_user[name]
				user[category] += 1
			else:
				per_user[name] = {'INFO':0, 'ERROR':1}

sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = operator.itemgetter(1), reverse=True)
#sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = lambda x: x[1], reverse=True)
sorted_users = [("Username", "INFO", "ERROR")] + sorted(per_user.items())[0:8]
#sorted_users = [("Username", "INFO", "ERROR")] + sorted(per_user.items())

with open("error_message.csv", "w") as error_file:
	for line in sorted_messages:
		error_file.write("{}, {}\n".format(line[0], line[1]))

with open("user_statistics.csv", "w") as user_file:
	for line in sorted_users:
		if isinstance(line[1], dict):
			user_file.write("{}, {}, {}\n".format(line[0], line[1].get("INFO"), line[1].get("ERROR")))
		else:
			user_file.write("{}, {}, {}\n".format(line[0], line[1], line[2]))

