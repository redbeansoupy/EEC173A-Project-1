import socket
import json

# To run:
# 1. Run Proxy
# python proxy_servervictorialam_919626106_jinsiguo_918709406.py
# 2. Run Server
# python servervictorialam_919626106_jinsiguo_918709406.py
# 3. Run client
# python clientvictorialam_919626106_jinsiguo_918709406.py

server_ip = '127.0.0.1'
server_port = 8888


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}")

try: 
    while True:
        # The link here helped me to debug -> I didn't use accept at first
        # https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
        proxy_socket, proxy_addr = server_socket.accept()
        data = proxy_socket.recv(1024).decode()
        if data:
            print(f"Server received: {data}")
            send_proxy_msg = "DONE"
            proxy_socket.send(send_proxy_msg.encode())
            proxy_socket.shutdown(socket.SHUT_RDWR)
            proxy_socket.close()
except KeyboardInterrupt:
    print("\nServer shutting down.")
finally:
    server_socket.close()

        


