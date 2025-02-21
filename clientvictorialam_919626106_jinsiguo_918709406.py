# import socket
# import json
# import threading

# # Server Code
# def server(host='127.0.0.1', port=7000):
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((host, port))
#     server_socket.listen(5)
#     print(f"Server listening on {host}:{port}")
    
#     while True:
#         conn, addr = server_socket.accept()
#         data = conn.recv(1024).decode()
#         if data:
#             print(f"Server received: {data}")
#             response = data[::-1]  # Just reversing the string as a simple response
#             conn.send(response.encode())
#             print(f"Server sent: {response}")
#         conn.close()

# # Proxy Server Code
# def proxy_server(host='127.0.0.1', port=8000, blocklist=None):
#     if blocklist is None:
#         blocklist = set()
    
#     proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     proxy_socket.bind((host, port))
#     proxy_socket.listen(5)
#     print(f"Proxy Server listening on {host}:{port}")
    
#     while True:
#         conn, addr = proxy_socket.accept()
#         data = conn.recv(1024).decode()
#         if data:
#             print(f"Proxy received: {data}")
#             request = json.loads(data)
#             server_ip, server_port, message = request["server_ip"], request["server_port"], request["message"]
            
#             if server_ip in blocklist:
#                 error_msg = "Error: Blocked IP"
#                 conn.send(error_msg.encode())
#                 print(f"Proxy sent: {error_msg}")
#             else:
#                 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
#                     server_sock.connect((server_ip, server_port))
#                     server_sock.send(message.encode())
#                     response = server_sock.recv(1024).decode()
#                     conn.send(response.encode())
#                     print(f"Proxy forwarded response: {response}")
#         conn.close()

# def client(proxy_host='127.0.0.1', proxy_port=8000, server_ip='127.0.0.1', server_port=7000, message='ping'):
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((proxy_host, proxy_port))
#     request = json.dumps({"server_ip": server_ip, "server_port": server_port, "message": message})
#     client_socket.send(request.encode())
#     response = client_socket.recv(1024).decode()
#     print(f"Client received: {response}")
#     client_socket.close()

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

server_ip = '127.0.0.2'
server_port = 8888

client_ip = '127.0.0.1'
client_port = 7000

message = ''.join(random.choices(string.ascii_lowercase, k=4))
print(message)
data = {"server_ip": server_ip, "server_port": server_port, "message": message}

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((proxy_ip, proxy_port))

# I realize I need to encode the json_data
# https://stackoverflow.com/questions/39817641/how-to-send-a-json-object-using-tcp-socket-in-python
json_data = json.dumps(data)
client_socket.send(json_data.encode())
response = client_socket.recv(1024).decode()
print(response)
client_socket.close()


