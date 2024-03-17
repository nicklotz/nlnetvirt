import socket
import base64
import json
import time

def compose_message(username, message):
    return {
        "username": username,
        "timestamp": time.time(),
        "message": base64.b64encode(message.encode()).decode()
    }

def transmit_and_wait_ack(client_socket, server_address, message_obj):
    json_message = json.dumps(message_obj)
    client_socket.sendto(json_message.encode(), server_address)
    try:
        client_socket.settimeout(2.0)
        ack_message, _ = client_socket.recvfrom(1024)
        ack_obj = json.loads(ack_message.decode())
        if ack_obj.get("status") == "Received":
            print("Server acknowledged receipt of the message.")
        else:
            print("Received unknown acknowledgment from the server.")
    except socket.timeout:
        print("Timed out waiting for acknowledgment from the server.")
    finally:
        client_socket.settimeout(None)

def send_messages(client_socket, server_address, username):
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        message_obj = compose_message(username, message)
        transmit_and_wait_ack(client_socket, server_address, message_obj)

def get_user_data():
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
    print(f"Ready to send messages to {host}:{port} as {username}.")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        send_messages(client_socket, server_address, username)
    finally:
        client_socket.close()

