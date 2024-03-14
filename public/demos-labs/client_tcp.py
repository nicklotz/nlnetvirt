import socket
import threading
import base64
import json
import time

def send_messages(client_socket, username):
    # This function allows the user to send messages to the server
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break  # Exit loop to stop sending messages

        # Prepare the message with a timestamp, username, and encode the message content in Base64
        message_obj = {
            "username": username,
            "timestamp": time.time(),
            "message": base64.b64encode(message.encode()).decode()
        }

        # Convert the message object to a JSON string and send it to the server
        json_message = json.dumps(message_obj)
        client_socket.sendall(json_message.encode())  # TCP ensures the message is sent reliably

def receive_messages(client_socket):
    # Function to receive messages from the server
    while True:
        try:
            # Blocking call to wait for messages from the server
            message = client_socket.recv(1024)
            if not message:
                print("Disconnected from the server")
                break  # Exit loop if disconnected

            print(f"Received: {message.decode()}")

        except:
            print("Disconnected from the server.")
            client_socket.close()
            break  # Exit loop on exception

def start_client(host, port, username):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to the server at {host}:{port}")

    # Start a thread to listen for messages from the server
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Main loop for sending messages
    send_messages(client_socket, username)

    client_socket.close()  # Close the socket when done

def get_user_data():
    # Collect user input for connection details and username
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

