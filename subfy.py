#!/usr/bin/env python
# This is my subdomain finder tool

import requests

domain = input("Enter domain: ") #it asks for domain
path = input("Enter the path of subdomains file (wordlists): ") 
file = open(path, 'r') #subdomains file

content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"
    url = f"https://{subdomain}.{domain}" #another variable
    try:
        requests.get(url) #sends requests
    except requests.ConnectionError:
        pass
    else:
        print("Discovered subdomains: ", url)
