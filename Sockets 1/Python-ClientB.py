import socket
# import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    print("Client B Connected to Socket...")
    message = input("Client B Running - Please Enter your message: ")
    inputBytes = str.encode(message)
    sock.sendall(inputBytes)

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print(f"Client Sent:                {message}")
print(f"Server Replied with:        {received}")