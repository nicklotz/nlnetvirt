# Client.py to handle response from server

import socket
import threading
import base64
import json
import time

def send_messages(client_socket, username):
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break  # Exit loop to stop sending messages
        message_obj = {
            "username": username,
            "timestamp": time.time(),
            "message": base64.b64encode(message.encode()).decode()
        }
        json_message = json.dumps(message_obj)
        client_socket.sendall(json_message.encode())

def decode_response(message):
    message_obj = json.loads(message.decode())
    decoded_message = base64.b64decode(message_obj['response']).decode()
    return decoded_message

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print("Disconnected from the server")
                break
            decoded_message = decode_response(message)
            print(f"Received: {decoded_message}")
        except Exception as e:
            print(f"An error occurred: {e}")
            client_socket.close()
            break

def start_client(host, port, username):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to the server at {host}:{port}")
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()
    send_messages(client_socket, username)
    client_socket.close()  # Close the socket when done

def get_user_data():
    print("Welcome to the Chat Application!")
    host = input("Enter the server address (default: 127.0.0.1): ").strip() or "127.0.0.1"
    port = int(input("Enter the server port (default: 65432): ").strip() or 65432)
    username = input("Enter your username: ").strip()
    return username, host, port

if __name__ == "__main__":
    username, host, port = get_user_data()
    print(f"Connecting to {host}:{port} as {username}...")
    try:
        start_client(host, port, username)
    except ConnectionRefusedError:
        print(f"Failed to connect to the server at {host}:{port}. Please check the server status and try again.")
