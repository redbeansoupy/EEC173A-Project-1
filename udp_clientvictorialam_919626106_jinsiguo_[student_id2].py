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

# Source: https://realpython.com/python-sockets/
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Validate input
if len(sys.argv) != 2:
    print("Usage: udp_xyzabc.py [size in MB to send]")
    exit(1)
if sys.argv[1].isdigit() == False:
    print("Not a number!")
    exit(1)

size_mb = int(sys.argv[1])
if (size_mb < 25 or size_mb > 200):
    print("size must be between 25 and 200")
    exit(1)


# Generate payload of size "size_mb"
payload = bytearray(size_mb * 1000)
for i in range(size_mb * 1000): # For fun, fill this with lowercase alphabet
    payload[i] = 97 + (i % 26)
payload_bstr = ''.join(format(byte, '08b') for byte in payload)
assert len(payload_bstr) == size_mb / 8000 # 8000 bits per megabyte

