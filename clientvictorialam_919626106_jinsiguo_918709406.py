import socket
import json

# Basic of client
def client(proxy_host='127.0.0.1', proxy_port=8000, server_ip='127.0.0.1', server_port=7000, message='ping'):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((proxy_host, proxy_port))
    request = json.dumps({"server_ip": server_ip, "server_port": server_port, "message": message})
    client_socket.send(request.encode())
    response = client_socket.recv(1024).decode()
    print(f"Client received: {response}")
    client_socket.close()