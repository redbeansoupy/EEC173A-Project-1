import socket
import json

# To run:
# 1. Run Proxy
# python proxy_servervictorialam_919626106_jinsiguo_918709406.py
# 2. Run Server
# python servervictorialam_919626106_jinsiguo_918709406.py
# 3. Run client
# python clientvictorialam_919626106_jinsiguo_918709406.py

proxy_ip = '127.0.0.1'
proxy_port = 6000

blocklist = [7777]

proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
proxy_socket.bind((proxy_ip, proxy_port))
proxy_socket.listen(5)
print(f"Proxy Server listening on {proxy_ip}:{proxy_port}")

try: 
    while True:
        # The link here helped me to debug -> I didn't use accept at first
        # https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
        client_socket, client_addr = proxy_socket.accept()
        data = client_socket.recv(1024).decode()
        if data:
            print(f"Proxy received: {data}")
            json_data = json.loads(data)
            # data = {"server_ip": server_ip, "server_port": server_port, "message": message}
            server_ip = json_data["server_ip"]
            server_port = json_data["server_port"]
            message = json_data["message"]

            print(f"Server IP: {server_ip}")
            print(f"Server Port: {server_port}")
            print(f"Message: {message}")

            if server_port in blocklist:
                print("Error, on blocklist")
                send_back_msg = "Error, not allowed address"
                client_socket.send(send_back_msg.encode())
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()
            else:
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_socket.connect((server_ip, server_port))
                server_socket.send(message.encode())
                response = server_socket.recv(1024).decode()
                print("response: ", response)
                client_socket.send(response.encode())
                print("response send to Client")
                server_socket.shutdown(socket.SHUT_RDWR)
                server_socket.close()
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()
except KeyboardInterrupt:
    print("\nProxy shutting down.")
finally:
    proxy_socket.close()
