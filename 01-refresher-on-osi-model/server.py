import socket
import threading
from handle_client import *

def start_server(host='127.0.0.1', port=65432):
    # Create a socket object using IPv4 and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen()

    print(f"Server is listening on {host}:{port}")

    while True:
        # Accept a new connection
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

        # Print the number of active connections
        print(f"Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
