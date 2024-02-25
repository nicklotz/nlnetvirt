import base64
import json
import time

def handle_client(client_socket):
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024)
            if not message:
                break

            # Decode JSON message
            message_obj = json.loads(message.decode())

            # Decode the Base64 encoded message
            decoded_message = base64.b64decode(message_obj['message']).decode()

            # Print the received message with username and timestamp
            print(f"[{message_obj['username']} @ {time.ctime(message_obj['timestamp'])}]: {decoded_message}")

        except ConnectionResetError:
            break
        except json.JSONDecodeError:
            print("Error decoding JSON")
            break
        except base64.binascii.Error:
            print("Error decoding Base64 message")
            break

    # Close the connection when done
    client_socket.close()

