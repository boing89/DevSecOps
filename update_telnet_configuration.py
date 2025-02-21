import argparse
import time
import sys
from telnetlib import Telnet

# Argument parsing
parser = argparse.ArgumentParser(description='Telnet configuration script.')
parser.add_argument('--host', required=True, help='IP address of the router')
parser.add_argument('--port', type=int, required=True, help='Telnet port')
args = parser.parse_args()

host = args.host
port = args.port

# List of Telnet commands to be executed
commands = [
    "terminal length 0",  # Disable paging of command output
    "configure terminal",  # Enter configuration mode
    "hostname majorp",  # Set the hostname
    "end",  # Exit configuration mode
    "write memory",  # Save configuration
    "exit"  # Exit Telnet session
]

try:
    tn = Telnet(host, port)
    time.sleep(2)  # Wait for the connection to establish
    for command in commands:
        tn.write(command.encode('ascii') + b"\n")
        print(f"Sent: {command}")
        time.sleep(3)  # Wait for the command to execute
    tn.write(b"exit\n")
    tn.close()
except Exception as e:
    sys.exit(f"An error occurred: {e}")
