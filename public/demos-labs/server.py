import socket
import threading
import base64
import json
import time

def print_decoded(message):
    message_obj = json.loads(message.decode())
    decoded_message = base64.b64decode(message_obj['message']).decode()
    print(f"[{message_obj['username']} @ {time.ctime(message_obj['timestamp'])}]: {decoded_message}")

def handle_exception(err):
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
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break  # If no message, exit the loop
            print_decoded(message)
        except (ConnectionResetError, json.JSONDecodeError, base64.binascii.Error) as err:
            if handle_exception(err):
                break  # Exit the loop if an exception handler returned True
    client_socket.close()  # Close the client socket when done

def manage_client_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
    print(f"Active connections: {threading.active_count() - 1}")

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server is listening on {host}:{port}")
    while True:
        manage_client_connection(server_socket)

if __name__ == "__main__":
    start_server()
