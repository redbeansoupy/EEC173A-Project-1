# UDP Server: 
# measure the throughput (amount of data received / time taken to receive them) 
# and send it back to the client

import socket
import time

SERVER_IP = "127.0.0.1"  # localhost
SERVER_PORT = 5555  # arbitrarily chosen socket

sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock_udp.bind((SERVER_IP, SERVER_PORT))

times = [0, 0]
sizes = []
src_addr = 0
print("Server is receiving data now...")
while True:
    data, src_addr = sock_udp.recvfrom(4096) # BLOCKING function call
    now = time.time()
    if times[0] != 0: # If this not is the first record (this is scuffed, i know LOL)
        sizes.append(len(data)) # Record number of bytes sent after first "correct" time recorded
        times[1] = now
    else:
        times[0] = now

    if len(sizes) > 10000: # Enough samples!
        break

# Measure throughput and send back to client
total_data = sum(sizes)
total_time = times[1] - times[0]
throughput = total_data / total_time
msg_str = f"Throughput: {(throughput / 1000000):.3f} Megabytes per second"

sock_udp.sendto(msg_str.encode(), src_addr)
# print("total_data: ", total_data)
# print("total_time: ", total_time)

print("Completed execution iPerfectly!")