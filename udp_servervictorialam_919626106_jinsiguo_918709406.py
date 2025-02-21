# UDP Server: 
# measure the throughput (amount of data received / time taken to receive them) 
# and send it back to the client

import socket
import time

SERVER_IP = "127.0.0.1"  # localhost
SERVER_PORT = 5555  # arbitrarily chosen socket

sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock_udp.bind((SERVER_IP, SERVER_PORT))

start = 0; end = 0
sizes = []
payload = []
src_addr = 0
first_time = 0

print("Server is receiving data now...")
print("SERVER METADTA: IP address: ", SERVER_IP, "; Port: ", SERVER_PORT)
# Receive the START message
data, src_addr = sock_udp.recvfrom(4096)
assert data == b"START"
start = time.time()

# Receive the payload
while True:
    data, src_addr = sock_udp.recvfrom(4096) # BLOCKING function call

    if data == b"STOP": 
        break

    sizes.append(len(data)) # Record number of bytes sent after first "correct" time recorded
    payload.append(data.decode())
    end = time.time()

# Measure throughput and send back to client
total_data = sum(sizes)
total_time = end - start
throughput = total_data / total_time
msg_str = f"Throughput: {(throughput / 1000):.3f} Kilobytes per second"

sock_udp.sendto(msg_str.encode(), src_addr)

print(f"Time that first packet was received: {start}")
print("Client IP address: ", src_addr[0])
print("Size of data received (bytes): ", total_data)
print("Time taken to receive (seconds): ", total_time)

print("Server process completed iPerfectly!")