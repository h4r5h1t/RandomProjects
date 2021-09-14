import smtplib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--email", help="Sender Email address [eg. -e xyz@gmail.com]", required=True)
parser.add_argument("-p", "--passwd", help="Password [eg. -p pass123]", required=True)
parser.add_argument("-eF", "--emailFile", help="Text file of Receiver Email address [eg. -eF emails.txt]", required=True)
parser.add_argument("-mF", "--msgFile", help="Text File of Message [eg. -mF message.txt]")
parser.add_argument("-m", "--msg", help="Prompt for Message ", action="store_true")
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
args = parser.parse_args()

#email sending function
def send_email(email, passwd, receivers, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    print(server.login(email, passwd))
    for mail in receivers:
        #server.sendmail(email, mail, msg)
        if args.verbose:
            print(f"Email sent to {mail}")        
    server.quit() 
    print("\nAll Email sent successfully")



#Receiver Emails
receivers = []
with open (args.emailFile) as emails:
    for email in emails:
        r = email.strip() 
        receivers.append(r)

#Message 
if args.msg:
    print("\nEnter your message:\n")
    sub = input("Subject: ")
    body = input("Message Body: ")
    msg = f"Subject:{sub}\n{body}"

elif args.msgFile:
    msg = ""
    with open (args.msgFile) as msgs:
        for m in msgs:
            msg += m
else:
    print("Please use -m flag if you want to prompt for message or use -mF flag with msg file")

send_email(args.email, args.passwd, receivers, msg)



# email = input("Enter your email: ")
# password = input("Enter your password: ")
# message = input("Enter your message:")
# send_email(email, password, message)


