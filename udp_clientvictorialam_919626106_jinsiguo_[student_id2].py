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
import time

# Source: https://realpython.com/python-sockets/
SERVER_IP = "127.0.0.1"  # localhost
SERVER_PORT = 5555  # arbitrarily chosen socket

CLIENT_IP = "127.0.0.1"
CLIENT_PORT = 7777

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
start = time.time()
payload = bytearray(size_mb * 1000000)
for i in range(size_mb * 1000000): # For fun, fill this with lowercase alphabet
    payload[i] = 97 + (i % 26)

print(f"Completed string generation--Took {(time.time() - start):.2f} seconds.")

# Send this payload to the server using UDP
# Source: https://wiki.python.org/moin/UdpCommunication
# ---- socket.AF_INET is a macro for internet in general
# ---- socket.SOCK_DGRAM is a macro representing UDP
sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_udp.bind((CLIENT_IP, CLIENT_PORT))

i = 0
segment_size=1500
print("Client is sending data now...")
while i < len(payload): # Send in bunches of 1.5KB (maximum for my system)
    segment = payload[i:min(i + segment_size, len(payload))]
    bytes_sent = sock_udp.sendto(segment, (SERVER_IP, SERVER_PORT))
    i += segment_size

# UDP is connectionless so we don't use socket.listen()
print("Client is listening for a response...")
data, server_addr = sock_udp.recvfrom(4096) # buffer size is 4096 bytes (blocking)
print(data.decode())