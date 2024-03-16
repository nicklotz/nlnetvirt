import socket
import base64
import json
import time

def send_acknowledgment(client_addr, server_socket):
    ack_message = json.dumps({"status": "Received"})
    server_socket.sendto(ack_message.encode(), client_addr)

def print_decoded(message):
    message_obj = json.loads(message.decode())
    decoded_message = base64.b64decode(message_obj['message']).decode()
    print(f"[{message_obj['username']} @ {time.ctime(message_obj['timestamp'])}]: {decoded_message}")

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Server is listening on {host}:{port}")

    while True:
        message, addr = server_socket.recvfrom(1024)
        try:
            print_decoded(message)
            send_acknowledgment(addr, server_socket)
        except (json.JSONDecodeError, base64.binascii.Error) as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    start_server()

