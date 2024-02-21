import socket
import threading

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
            print("An error occurred. Disconnected from the server.")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        # User input for the message to send
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break

        # Send the message to the server
        client_socket.sendall(message.encode())

def start_client(host='127.0.0.1', port=65432):
    # Create a socket object using IPv4 and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to the server at {host}:{port}")

    # Create a thread for receiving messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Main loop for sending messages
    send_messages(client_socket)

    # Close the connection when done
    client_socket.close()

if __name__ == "__main__":
    start_client()

