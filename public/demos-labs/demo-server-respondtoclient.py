# Server.py that generates response and sends to client

import socket
import threading
import base64
import json
import time

def print_decoded(message):
    message_obj = json.loads(message.decode())
    decoded_message = base64.b64decode(message_obj['message']).decode()
    print(f"[{message_obj['username']} @ {time.ctime(message_obj['timestamp'])}]: {decoded_message}")
    return message_obj['username']  # Return the username for response

def compose_response(username):
    response_message = f"Hello, {username}! Your message was received at {time.ctime()}."
    encoded_message = base64.b64encode(response_message.encode()).decode()  # Base64 encode
    return json.dumps({"response": encoded_message}).encode()  # Wrap in JSON and encode

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
                break
            username = print_decoded(message)
            response = compose_response(username)
            client_socket.sendall(response) 
        except (ConnectionResetError, json.JSONDecodeError, base64.binascii.Error) as err:
            if handle_exception(err):
                break
    client_socket.close()

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
