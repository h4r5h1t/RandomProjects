#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Resolving Hostname to IP addr

else:
    print(f"Usage: {sys.argv[0]} <host>")


# Adding Bannner

print("-" * 50)
print(f"Scanning Target {target}")
print(f"Time started : {datetime.now()}")
print("-" * 50)

try:
    for port in range(0, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)        
        result = sock.connect_ex((target, port)) # connect_ex returns 0 if connection is successful
        if result == 0:
            print(f"Port {port} is open")
    sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C \t Existing the program")
    sys.exit()
except socket.error:
    print(f"Couldn't connect to the server")
    sys.exit()
except socket.gaierror():
    print("Hostname could not be resolved")
    sys.exit()
