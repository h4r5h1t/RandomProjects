#!/usr/bin/env python3

import re
import csv
import operator

def errors_report(file,csv_file):
    errors = {}
    events = []
    with open(file,"r") as f:
        logs = f.readlines()
        for log in logs:
            line = log.strip()
            error = re.search(r"ticky: ERROR[: ]+([\w ']+).*", line)
            try:
                events.append(error.group(1).strip())
            except:
                continue
    f.close()

    for event in set(events):
        errors[event] = events.count(event)
    toperrors=sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
    errors_msg_dict = {}
    errors_msg_list = []
    for error in toperrors:
        errors_msg_dict["Error"] = error[0]
        errors_msg_dict["Count"] = error[1]
        errors_msg_dict_copy = errors_msg_dict.copy()
        errors_msg_list.append(errors_msg_dict_copy)
    column = ["Error","Count"]
    create_csv(errors_msg_list,column,csv_file)


def users_report(file,csv_file):
    users = []
    userdit = {}
    with open(file,"r") as f:
        logs = f.readlines()
        for log in logs:
            line = log.strip()
            user = re.search(r"ticky:.*\(([\w.]+)\)", line)
            if user.group(1) not in users:
                users.append(user.group(1))
        for user in sorted(users):
            info = 0
            error = 0
            for log in logs:
                line = log.strip()
                if user in line:
                    event = re.search(r"ticky:\s([A-Z]+).*",line)
                    if event.group(1) == "ERROR":
                        error = error + 1
                    else:
                        info = info + 1
            userdit[user] = [info,error]
        users_dict = {}
        users_list = []
        for user,key in userdit.items():
            users_dict["Username"] = user
            users_dict["INFO"] = key[0]
            users_dict["ERROR"] = key[1]
            users_dict_copy = users_dict.copy()
            users_list.append(users_dict_copy)
        column = ["Username","INFO","ERROR"]
        create_csv(users_list,column,csv_file)

    f.close() 


def create_csv(value,column,file):
    with open(file,"w") as f:
        writer = csv.DictWriter(f, fieldnames=column)
        writer.writeheader()
        writer.writerows(value)
    f.close()                


if __name__ == "__main__":
    file = "C:\\Users\\harsh\\Documents\\Programs\\LogRegex\\syslog.log"
    error_csv = "C:\\Users\\harsh\\Documents\\Programs\\LogRegex\\error_message.csv "
    user_csv = "C:\\Users\\harsh\\Documents\\Programs\\LogRegex\\user_statistics.csv"
    errors_report(file,error_csv)
    users_report(file,user_csv)