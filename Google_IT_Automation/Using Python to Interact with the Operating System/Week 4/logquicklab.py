#!/usr/bin/env python3
'''Imagine one of your colleagues is struggling with a program that keeps throwing an error. Unfortunately, the program's source code is too complicated to easily find the error there. The good news is that the program outputs a log file you can read! Let's write a script to search the log file for the exact error, then output that error into a separate file so you can work out what's wrong.

What you'll do
Write a script to search the log file using regex to find for the exact error.
Report the error into a separate file so you know what's wrong for further analysis.

Month Day hour:minute:second mycomputername "process_name"["random 5 digit number"] "ERROR/INFO/WARN" "Error description"
'''

import sys
import os
import re

def error_search(log_file):
	error = input("What is the error? ").split()
	returned_errors = []
	with open(log_file, mode='r',encoding='UTF-8') as file:
		for log in  file.readlines():
		error_patterns = ["error"] #to filter out all the ERROR logs only. We can change this to view other types of logs such as INFO and WARN or siplmy leave it balnk to fetch all types of logs, irrespective of their type.
		for i in error:
			error_patterns.append((error.lower())) # adding user given error for filtering 
			for error_pattern in error_patterns:
				if re.search(error_pattern, log.lower()):
					returned_errors.append(log) #adding the log line which have inputed error
	return returned_errors 

def file_output(returned_errors):
	with open(os.path.expanduser('~') + '/Desktop/errors_found.log', 'w') as file:
		for error in returned_errors:
			file.write(error)
if __name__ == "__main__":
	log_file = sys.argv[1]
	returned_errors = error_search(log_file)
	file_output(returned_errors)
	sys.exit(0)