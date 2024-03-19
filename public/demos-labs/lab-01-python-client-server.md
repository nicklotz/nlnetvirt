# Lab 1: Client-Server Application in Python

**Note:** the Python labs in this class assume Python 3. 

## A. Write the server application

1. In a terminal shell (or on your desktop), create a file called **server.py**.

```
touch server.py
```

2. Open server.py and paste the following code.

```python
import socket
import threading
import base64
import json
import time

def print_decoded(message):
    message_obj = json.loads(message.decode())
    decoded_message = base64.b64decode(message_obj['message']).decode()
    print(f"[{message_obj['username']} @ {time.ctime(message_obj['timestamp'])}]: {decoded_message}")

def handle_exception(err):
    if isinstance(err, ConnectionResetError):
        print("Connection reset error occurred")
        return True
    elif isinstance(err, json.JSONDecodeError):
        print("Error decoding JSON")
        return True
    elif isinstance(err, base64.binascii.Error):
        print("Error decoding Base64 message")
        return True
    return False

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break  # If no message, exit the loop
            print_decoded(message)
        except (ConnectionResetError, json.JSONDecodeError, base64.binascii.Error) as err:
            if handle_exception(err):
                break  # Exit the loop if an exception handler returned True
    client_socket.close()  # Close the client socket when done

def manage_client_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
    print(f"Active connections: {threading.active_count() - 1}")

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server is listening on {host}:{port}")
    while True:
        manage_client_connection(server_socket)

if __name__ == "__main__":
    start_server()
```

3. Save and close server.py.

4. Run the server and test that it is listening.

```
python3 server.py
```

The output should look read similar to: `The server is listening on <IP>:<Port>`.

5. Type `CTRL-C` to exit the program.

## B. Write the client application

1. In a terminal shell (or on your desktop), create a file called **client.py**.

```
touch client.py
```

2. Open client.py and paste the following code.

```python
import socket
import threading
import base64
import json
import time

def send_messages(client_socket, username):
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break  # Exit loop to stop sending messages
        message_obj = {
            "username": username,
            "timestamp": time.time(),
            "message": base64.b64encode(message.encode()).decode()
        }
        json_message = json.dumps(message_obj)
        client_socket.sendall(json_message.encode())

def receive_messages(client_socket):
    while True:
        try:
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
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to the server at {host}:{port}")
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()
    send_messages(client_socket, username)
    client_socket.close()  # Close the socket when done

def get_user_data():
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
```

3. Save and close client.py.

4. Test the client.

```
python3 client.py
```

The output should begin with `Welcome to Chat Application!` followed by a prompt.

5. Type `CTRL-C` to exit the program.

## C. Run the server and client together

1. In one terminal window, run the server application.

```
python3 server.py
```

2. In a *second* terminal window, run the client application.

```
python3 client.py
```

3. From the client application, when prompted for the server address, type **Return** to accept the default server IP.

4. From the client application, when prompted for the server port, type `12345`, then **Return**.

5. When prompted for a username, type your first name, then **Return**.

6. Note the connection error. Run `python3 client.py` to run the client program again.

7. Type **Return** to accept the default server IP. Then type **Return** to accept the default port. 

8. Enter your first name when prompted, then type **Return**.

9. Navigate to the shell where you have server.py running. What do you see in the output?

10. Navigate back to the shell where you have client.py running. Enter some text in the message prompt, followed by **Return**. Repeat once or twice more.

11. Navigate back to the server shell. What do you see in the output?

12. Open a *third* terminal window. Run `python3 client.py` to run a second client instance.

13. Press **Return** twice to accept the default server IP and port. 

14. When prompted for a username, enter a different name here (doesn't matter what, could be made up).

15. When prompted to enter a message, enter whatever you'd like and press **Return**. Repeat once or twice more.

16. Navigate back to the server shell. What do you see?

17. Alternate sending messages from both clients a few times. How does that appear in the server log?

18. From the server shell, type `CTRL-C` twice to kill the server.

19. Navigate back to the clients. What message do you see?

20. Type `exit` from each client to close both programs.
