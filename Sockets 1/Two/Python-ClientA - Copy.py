import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

print("Attempting to start Client A")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    myInput = input("Client A Connected - Please enter your string:")
    inputBytes = str.encode(myInput)
    s.sendall(inputBytes)
    data = s.recv(1024)

print("Received", repr(data))
print("Closing Client A")