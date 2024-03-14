import socket
import base64
import json
import time

def send_messages(client_socket, server_address, username):
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            # Exit the loop if the user types 'exit'
            break

        # Create a message object with the current timestamp, username, and the base64 encoded message
        message_obj = {
            "username": username,
            "timestamp": time.time(),
            "message": base64.b64encode(message.encode()).decode()
        }

        # Convert the message object to JSON and send it to the server
        json_message = json.dumps(message_obj)
        # Use sendto to send the message to the server's address
        client_socket.sendto(json_message.encode(), server_address)

def get_user_data():
    # Collect user input for server address, port, and username
    print("Welcome to the UDP Chat Application!")
    host_input = input("Enter the server address (default: 127.0.0.1): ")
    host = host_input.strip() if host_input.strip() else "127.0.0.1"
    port_input = input("Enter the server port (default: 65432): ")
    port = int(port_input.strip()) if port_input.strip() else 65432
    username = input("Enter your username: ").strip()
    return username, host, port

if __name__ == "__main__":
    username, host, port = get_user_data()
    server_address = (host, port)
    print(f"Connecting to {host}:{port} as {username}...")

    # Create a UDP socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Start sending messages to the server
        send_messages(client_socket, server_address, username)
    finally:
        # Ensure the socket is closed properly when the program is done
        client_socket.close()

