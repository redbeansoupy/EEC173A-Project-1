# [x] The client sends the correct data to the proxy, not directly to the server (5 points)
# [x] The proxy extracts the server’s IP from the client's data (3 points)
# [x] The proxy implements IP filtering (5 points)
# [x] The proxy sends the correct data to the server on behalf of the client (7 points)
# [x] The server extracts the proxy’s IP from the proxy’s data (3 points)
# [x] The server sends the correct information back to the proxy, and the proxy forwards that
# information to the client (7 points)

# To run:
# 1. Run Proxy
# python proxy_servervictorialam_919626106_jinsiguo_918709406.py
# 2. Run Server
# python servervictorialam_919626106_jinsiguo_918709406.py
# 3. Run client
# python clientvictorialam_919626106_jinsiguo_918709406.py

import random
import string
import socket
import json

proxy_ip = '127.0.0.1'
proxy_port = 6000

server_ip = '127.0.0.1'
input_server = input("Enter 'block' to test block mode, anything else to send normally: ")
if (input_server.lower() == "block"):
    server_port = 7777
else: 
    server_port = 8888

client_ip = '127.0.0.1'
# client_port = 7000

message = ''.join(random.choices(string.ascii_lowercase, k=4))
print("Random 4 letter string: ", message)
data = {"server_ip": server_ip, "server_port": server_port, "message": message}
print("Json data: ", data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Socket reuse -> it was giving error if I run client multiple times
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind((client_ip, 0))

# Notes: I want to make it continue to set up connection and send multiple
client_socket.connect((proxy_ip, proxy_port))
# Notes: I realize I need to encode the json_data
# https://stackoverflow.com/questions/39817641/how-to-send-a-json-object-using-tcp-socket-in-python
json_data = json.dumps(data)
client_socket.send(json_data.encode())
response = client_socket.recv(1024).decode()
print("Feedback: ", response)
client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()


