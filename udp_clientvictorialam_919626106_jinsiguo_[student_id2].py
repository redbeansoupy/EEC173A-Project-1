# UDP Client
# Take in number of megabytes x between 25 and 200 as an input
# Generate a payload of size x MB and send to the server
# Print the throughput received from the server
# Also print: 
# - The data sent from the client and its timestamp.
# - The timestamp when the data is received on the server side.
# - Both sent and received data.
# - The IP addresses of the client and server.

import socket
import sys


# Validate input
if len(sys.argv) != 2:
    print("Usage: udp_xyzabc.py [size in MB to send]")
    exit(1)
if sys.argv[1].isdigit() == False:
    print("Not a number!")
    exit(1)

size_mb = int(sys.argv[1])



