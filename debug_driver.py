from main import start_driver
import socket
import threading

def handle_client(client_socket, session_url):
    client_socket.send(session_url.encode())

    while True:
        command = client_socket.recv(1024).decode()
        if command == 'quit':
            break
        client_socket.close()

driver = start_driver('debug', None, None)

session_url = driver.command_executor._url

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)

while True:
    client_socket, _ = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket, session_url))
    client_handler.start()