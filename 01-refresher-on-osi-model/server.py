import socket
import threading
import base64
import json
import time

def print_decoded(message):
    # Decode the JSON-encoded message received from the client
    message_obj = json.loads(message.decode())
    decoded_message = base64.b64decode(message_obj['message']).decode()
    # Print the message with sender's username and timestamp
    print(f"[{message_obj['username']} @ {time.ctime(message_obj['timestamp'])}]: {decoded_message}")

def handle_exception(err):
    # Handle specific exceptions and return True if a break from the loop is needed
    if isinstance(err, ConnectionResetError):
        print("Connection reset error occurred")
        return True
    elif isinstance(err, json.JSONDecodeError):
        print("Error decoding JSON")
        return True
    elif isinstance(err, base64.binascii.Error):
        print("Error decoding Base64 message")
        return True
    return False

def handle_client(client_socket):
    # This function runs in a separate thread for each client
    while True:
        try:
            # Blocking call to receive data from the client
            message = client_socket.recv(1024)
            if not message:
                break  # If no message, exit the loop

            print_decoded(message)

        except (ConnectionResetError, json.JSONDecodeError, base64.binascii.Error) as err:
            if handle_exception(err):
                break  # Exit the loop if an exception handler returned True

    client_socket.close()  # Close the client socket when done

def manage_client_connection(server_socket):
    # Accept a new connection from a client
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    # Create and start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

    print(f"Active connections: {threading.active_count() - 1}")

def start_server(host='127.0.0.1', port=65432):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    # Listen for incoming connections
    server_socket.listen()
    print(f"Server is listening on {host}:{port}")

    while True:
        # Wait and accept new client connections
        manage_client_connection(server_socket)

if __name__ == "__main__":
    start_server()

