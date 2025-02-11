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
HOST_IP = "127.0.0.1"  # localhost
PORT = 5555  # arbitrarily chosen socket

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

# Send this payload to the server using UDP
# Source: https://wiki.python.org/moin/UdpCommunication
# ---- socket.AF_INET is a macro for internet in general
# ---- socket.SOCK_DGRAM is a macro representing UDP
sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(int(size_mb / 5)): # Send in bunches of 5MB because 25MB was too big
    sock_udp.sendto(payload[i * 5000:(i + 1) * 5000], (HOST_IP, PORT))

# UDP is connectionless so we don't use socket.listen()
while True:
    data, addr = sock_udp.recvfrom(4096) # buffer size is 1024 bytes
    print(data)