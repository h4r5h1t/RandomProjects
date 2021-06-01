import sys
import requests
import json 
import socket 

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

req = requests.get(f"https://{sys.argv[1]}")
print("\n"+str(req.headers))

ip = socket.gethostbyname(sys.argv[1])
print("\nThe IP of "+sys.argv[1]+ f" is {ip}\n")


#ipinfo.io -- api for getting gerolocation

req_geo = requests.get(f"https://ipinfo.io/{ip}/json")
resv = json.loads(req_geo.text)
print ("Hostname: " + resv ['hostname'])
print ("Location: " + resv ['loc'])
print ("City: " + resv ['city'])
print ("Region: " + resv ['region'])
print ("County: " + resv['country'])
print ("Org: " + resv ['org'])
