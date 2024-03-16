# Lab 02: UDP Client-Server

## A. Write a UDP server application

1. Create a new file called `server_udp.py`.

```
touch server_udp.py
```

2. Paste the following code into server_udp.py

```python
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
```

3. Save and close server_udp.py.

4. Test the server application. The output should read "Server is listening on <IP>:<Port>".

```
python3 server_udp.py
```

5. Type `CTRL-C` to kill the server.

## B. Write a UDP client application 

1. Create a new file called `client_udp.py`.

```
touch client_udp.py
```

2. Paste the following code into client_udp.py. What differences do you notice from the previous lab's client application?

```python
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
```

3. Save and close client_udp.py.

4. Try running the client application.

```
python3 client_udp.py
```

5. Press **Return** to accept the default when prompted for the server address.

6. Press **Return** to accept the default when prompted for the client address.

7. When prompted for a username, enter your first name, then press **Return**.

8. Enter any message when prompted. Why don't we see a connection attempt before the message prompt like in the previous lab's client application?

9. Press **Return** to send the message, then wait a couple seconds. Was the transmission successful? Why or why not?
