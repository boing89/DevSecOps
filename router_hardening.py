
from telnetlib inport Telnet
import argparse
import time
import sys

# Argument parsing
parser = argparse. ArgumentParser(description='Telnet configuration script.') 
parser.add_argument('--host', required=True, help='IP address of the router') 
parser.add_argument('--port', type=int, required=True, help='Telnet port') 
args = parser.parse_args()

host = args.host
port = args.port

#List of Telnet commands to be executed
commands = [
    "terminal length 0", # Disable paging of command output 
    "configure terminal", #Enter configuration mode
    "security passwords min-length 10", # Set the password minimum length 
    "service password-encryption",
    "aaa new-model",
    "aaa authentication login default local enable",
    "login block-for 60 attempts 2 within 30",
    "login on-success log",
    "login on-failure log",
    "line con 0", # Enter console line configuration mode 
    "privilege level 15"
    "Logging synchronous" # Prevent console output from interfering with input
    "exec-timeout 15", 
    "login authentication default",
    "exit",
    "line vty 0 15", # Enter VTY line configuration mode 
    "exec-timeout 15", 
    "logging synchronous",
    "exit",
    "end", # Exit configuration node
    "write memory", # Save configuration
    "exit" # Exit Telnet session
]
try:
    tn = Telnet (host, port)
    time.sleep(2) # Wait for the connection to establish
    for command in commands:
        tn.write(command.encode('ascii') + b"\n")
        print(f"Sent: {command}")
        time.sleep(3) # Wait for the command to execute 
    tn.write(b"exit\n")
    tn.close()
