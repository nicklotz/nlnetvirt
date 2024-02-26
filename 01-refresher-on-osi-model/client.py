import socket
import threading
import base64
import json
import time

# Handles presentation-layer JSON formatting of messages
def send_messages(client_socket, username):
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break

        # Create message object with timestamp and username
        message_obj = {
            "username": username,
            "timestamp": time.time(),
            "message": base64.b64encode(message.encode()).decode()  # Base64 encode the message
        }

        # Convert the message object to JSON and send
        json_message = json.dumps(message_obj)
        client_socket.sendall(json_message.encode())

def receive_messages(client_socket):
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024)
            if not message:
                print("Disconnected from the server")
                break

            # Print the received message
            print(f"Received: {message.decode()}")

        except:
            # An exception will occur when the server is closed or connection is lost
            print("Disconnected from the server.")
            client_socket.close()
            break

def start_client(host, port, username):
    # Create a socket object using IPv4 and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server - part of session layer handling
    client_socket.connect((host, port))
    print(f"Connected to the server at {host}:{port}")

    # Create a thread for receiving messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Main loop for sending messages
    send_messages(client_socket, username)

    # Close the connection when done
    client_socket.close()

def get_user_data():
    # Application-layer UI for starting client
    print("Welcome to the Chat Application!")

    # Input for the server address with a default value
    host_input = input("Enter the server address (default: 127.0.0.1): ")
    host = host_input.strip() if host_input.strip() else "127.0.0.1"

    # Input for the server port with a default value
    port_input = input("Enter the server port (default: 65432): ")
    port = port_input.strip() if port_input.strip() else 65432

    username = input("Enter your username: ").strip()
    return username, host, port

if __name__ == "__main__":
    username, host, port = get_user_data()
    print(f"Connecting to {host}:{port} as {username}...")

    # Start the client with the provided information
    try:
        start_client(host, port, username)
    except ConnectionRefusedError:
        print(f"Failed to connect to the server at {host}:{port}. Please check the server status and try again.")

