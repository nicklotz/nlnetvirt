import socket
import threading
import base64
import json
import time

# Function to send messages to the server
def send_messages(client_socket, username):
    while True:
        # Prompt user for message input
        message = input("Enter message: ")
        if message.lower() == 'exit':
            # Exit loop to stop sending messages if user types 'exit'
            break
        # Create a message object with additional info (username, timestamp)
        message_obj = {
            "username": username,
            "timestamp": time.time(),
            "message": base64.b64encode(message.encode()).decode()
        }
        # Convert the message object to JSON and send it to the server
        json_message = json.dumps(message_obj)
        client_socket.sendall(json_message.encode())

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Wait for and receive messages from the server
            message = client_socket.recv(1024)
            if not message:
                # Exit loop if disconnected from server
                print("Disconnected from the server")
                break
            # Print the received message
            print(f"Received: {message.decode()}")
        except Exception as e:
            # Handle any exceptions that occur during message reception
            print(f"Error: {e}")
            break

# Main function to start the client
def start_client(host, port, username):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to the server at specified host and port
        client_socket.connect((host, port))
        # Print connection info, demonstrating network layer addressing
        print(f"Connected to server at {host}:{port} (Network Layer: Server's IP Address and Port)")
        
        # Get and print client's own network layer info (IP address and port)
        local_ip, local_port = client_socket.getsockname()
        print(f"Client's network info - IP: {local_ip}, Port: {local_port}")

        # Start a thread to listen for messages from the server
        thread = threading.Thread(target=receive_messages, args=(client_socket,))
        thread.start()

        # Enter message sending loop
        send_messages(client_socket, username)
    finally:
        # Ensure the socket is closed properly
        client_socket.close()

# Function to get user input for server connection details and username
def get_user_data():
    print("Welcome to the Chat Application!")
    host = input("Enter the server address (default: 127.0.0.1): ").strip() or "127.0.0.1"
    port = int(input("Enter the server port (default: 65432): ").strip() or 65432)
    username = input("Enter your username: ").strip()
    return username, host, port

if __name__ == "__main__":
    username, host, port = get_user_data()
    start_client(host, port, username)

