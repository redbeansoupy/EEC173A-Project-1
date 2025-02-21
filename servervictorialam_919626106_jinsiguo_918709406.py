import socket
import json

# def proxy(host='127.0.0.1', port=8000, blocklist=None):
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

# To run:
# 1. Run Proxy
# python proxy_servervictorialam_919626106_jinsiguo_918709406.py
# 2. Run Server
# python servervictorialam_919626106_jinsiguo_918709406.py
# 3. Run client
# python clientvictorialam_919626106_jinsiguo_918709406.py

client_ip ='127.0.0.1'
client_port = 7000

proxy_ip = '127.0.0.1'
proxy_port = 6000

server_ip = '127.0.0.1'
server_port = 8888

blocklist = set('127.0.0.2')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}")

while True:
    # The link here helped me to debug -> I didn't use accept at first
    # https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
    proxy_socket, proxy_addr = server_socket.accept()
    data = proxy_socket.recv(1024).decode()
    if data:
        print(f"Server received: {data}")
        send_proxy_msg = "DONE"
        proxy_socket.send(send_proxy_msg.encode())
        proxy_socket.close()
        break

        


