import socket
import threading
import base64
import json
import time

# Function to decode and print the message received from the client
def print_decoded(message):
    # Decode the message from JSON format
    message_obj = json.loads(message.decode())
    # Decode the base64 encoded message content
    decoded_message = base64.b64decode(message_obj['message']).decode()
    # Print the message with additional info (username, timestamp)
    print(f"[{message_obj['username']} @ {time.ctime(message_obj['timestamp'])}]: {decoded_message}")

# Function to handle individual client connections
def handle_client(client_socket, addr):
    # Print the client's address (IP and port) upon connection
    print(f"Handling client {addr} (Network Layer: Client's IP Address and Port)")
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if not message:
                break
            # Decode and print the received message
            print_decoded(message)
        except Exception as err:
            # Handle any exceptions that occur during message handling
            print(f"Error: {err}")
            break
    # Close the client socket once the loop exits
    client_socket.close()

# Main function to start the server
def start_server(host='127.0.0.1', port=65432):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the specified host and port
    server_socket.bind((host, port))
    # Listen for incoming connections
    server_socket.listen()
    # Print server's listening address (demonstrates network layer addressing)
    print(f"Server started on {host}:{port} (Network Layer: IP Address and Port)")

    while True:
        # Accept new connections
        client_socket, addr = server_socket.accept()
        # Print the address of the connected client (network layer demonstration)
        print(f"Accepted connection from {addr} (Network Layer: Client's IP Address and Port)")
        # Handle the client in a new thread
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()

