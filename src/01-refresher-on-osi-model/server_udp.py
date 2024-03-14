import socket
import base64
import json
import time

def print_decoded(message):
    # Decode the JSON message received from the client
    message_obj = json.loads(message.decode())
    decoded_message = base64.b64decode(message_obj['message']).decode()
    # Print the message with the sender's username and timestamp
    print(f"[{message_obj['username']} @ {time.ctime(message_obj['timestamp'])}]: {decoded_message}")

def start_server(host='127.0.0.1', port=65432):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    print(f"UDP Server is listening on {host}:{port}")

    while True:
        # Receive messages; recvfrom returns the message and the address of the sender
        message, addr = server_socket.recvfrom(1024)
        try:
            # Attempt to decode and print the message
            print_decoded(message)
        except (json.JSONDecodeError, base64.binascii.Error) as err:
            # Print any errors encountered during message decoding
            print(f"Error: {err}")

if __name__ == "__main__":
    start_server()

