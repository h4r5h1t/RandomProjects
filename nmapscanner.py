import nmap
import sys

target = sys.argv[1]
ports = [21,22,80,139,443,8080]
if len(sys.argv) < 2:
    print("Usage: nmapscanner.py <target>") 

# if len(sys.argv) == 3:
#     ports.append(sys.argv[2].strip(','))

nm = nmap.PortScanner()
print(f"Scanning {target} for ports 21,22,80,139,443,8080...\n")

for port in ports: 
    portscan = nm.scan(target,str(port))
    print(f"Port {Port} is {portscan['scan'][target][tcp][port]['state']}\n"
print(f"Host {target} is {portscan['scan'][target]['status']['state']}")
