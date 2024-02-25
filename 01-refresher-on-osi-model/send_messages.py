import base64
import json
import time

def send_messages(client_socket, username):
    while True:
        # User input for the message to send
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

