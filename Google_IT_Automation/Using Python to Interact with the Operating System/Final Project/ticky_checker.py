#!/usr/bin/env python3
''' The logfile to be processed has to be passed  to the script'''
''' as an argument'''
import re
import sys
import csv
import operator

def statistics(logfile):

  per_user = {}
  error = {}

  with open(logfile, "r") as file:
    for line in file.readlines():
      pattern = r": ([A-Z]*) ([\w ']*) [\[\]\d# ]*\(([\w\.]*)\)$"
      message = re.search(pattern, line)
      log_type = message.group(1)
      log_message = message.group(2)
      log_user = message.group(3)
      #to create the error statistics
      if log_type == "ERROR":
        if log_message in error:
          error[log_message] += 1
        else:
          error[log_message] = 1
      #to create the user statistics
      if log_user in per_user:
        if log_type == "ERROR":
          per_user[log_user][log_type] += 1
        elif log_type == "INFO":
          per_user[log_user][log_type] += 1
      else:
        if log_type == "ERROR":
          per_user[log_user] = {"ERROR": 1, "INFO": 0}
        elif log_type == "INFO":
          per_user[log_user] = {"ERROR": 0, "INFO": 1}

#Here, the dictionaries will be sorted
  per_user = sorted(per_user.items())
  error = sorted(error.items(), key = operator.itemgetter(1), reverse = True)
  return per_user, error

def to_csv(per_user, error):
  with open("user_statistics.csv", "w") as users_csv:
    writer = csv.writer(users_csv)
    writer.writerow(["Username", "INFO", "ERROR"])
    for item in per_user:
      user, log_type = item
      line = [user,log_type["INFO"],log_type["ERROR"]]
      writer.writerow(line)
  with open("error_message.csv", "w") as error_csv:
    writer = csv.writer(error_csv)
    writer.writerow(["Error","Count"])
    writer.writerows(error)

if __name__ == "__main__":
  logfile = sys.argv[1]
  per_user, error = statistics(logfile)
  to_csv(per_user,error)


