from telnetlib import Telnet
import argparse
import time
import sys

#Argument parsing
parser = argparse. ArgumentParser(description='Telnet configuration script for Cisco router.') 
parser.add_argument('--host', required=True, help='IP address of the router') 
parser.add_argument('--port', type=int, required=True, help='Telnet port') 
args parser.parse_args()

host = args.host
port = args.port

#List of Telnet commands to be executed
commands [
    "enable", # Enter privileged exec mode
    "configure terminal", # Enter global configuration mode
    "interface GigabitEthernet2", # Enter interface configuration mode for g2
    "ip address 182.20.20.1 255.255.255.0", # Set IP address for g2
    "no shutdown", #Enable the interface g2
    "exit", # Exit interface configuration mode
    "Interface GigabitEthernet3", # Enter interface configuration mode for g3 
    "ip address 192.20.20.1 255.255.255.0", # Set IP address for g3
    "no shutdown", # Enable the interface g3
    "exit", # Exit interface configuration mode 
    "end", # Exit global configuration mode 
    "write memory", # Save configuration
    "exit" # Exit Telnet session
]

def send_commands(tn, commands):
    for command in commands:
    tn.write(command.encode('ascii') + b"\n")
    response = tn.read_until(b"#", timeout=10).decode('ascii') # Read until prompt 
    print("Sent: {command}")
    print("Response: {response}")
    time.sleep(3) # Adjust delay as needed

try:
    tn = Telnet (host, port)
    time.sleep(2) # Wait for connection to establish

    #Read initial prompt
    response = tn.read_until(b">", timeout=10).decode('ascii') 
    print(f"Initial Response: {response}")
    
    send_commands(tn, commands)

    #Ensure all commands are processed
    tn.read_until(b"#", timeout=10)
