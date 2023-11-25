import sys
import socket
from datetime import datetime

#define the target
if len(sys.argv) == 2:
   target = socket.gethostbyname(sys.argv[1]) #Translate hostname to ip4
else:
   print("Invalid amount of arguments.")
   print("Syntax: pyhton 3 scanner.py <ip>")

#Creating a banner
print('-' * 50)
print("Scanning target: " +target)
print("Time Started: "+str(datetime.now()))
print('-' * 50)

#Scanning ports
try:
  for port in range(50,85):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
          print(f"Port {port} is open")
    s.close()
except KeyboardInterrupt :
       print("\nExiting program.")
       sys.exit()
except socket.gaierror :
       print("\nHostname could not be resolved.")
       sys.exit()   
except socket.error :
       print("\nCould not connect to a server.")
       sys.exit()       