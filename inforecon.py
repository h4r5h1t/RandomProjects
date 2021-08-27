import sys
import requests
import json
import socket

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <url>")
    sys.exit(1)
req = requests.get(f"https://{sys.argv[1]}")
if req.status_code != 200:
    print(f"Error: {req.status_code}")
    sys.exit(1)
print(f"\nHeader Information:\n\n{str(req.headers)}\n\n")

gethost = socket.gethostbyname(sys.argv[1])
print(f"The IP address of {sys.argv[1]} is {gethost}\n")

#now we need to get the location of the host
# geo_req = requests.get(f"http://freegeoip.net/json/{gethost}")
# geo_json = json.loads(geo_req.text)
# print(f"The location of {sys.argv[1]} is {geo_json['city']}, {geo_json['region_name']}, {geo_json['country_name']}")

#now we need to get the location of the host using the api ipinfo
ipinfo_req = requests.get(f"http://ipinfo.io/{gethost}/json")
ipinfo_json = json.loads(ipinfo_req.text)
print(f"Location: {ipinfo_json['loc']}")
print(f"Region: {ipinfo_json['region']}")
print(f"City: {ipinfo_json['city']}") 
print(f"Country: {ipinfo_json['country']}")

