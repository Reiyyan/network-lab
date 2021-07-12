import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    message = input("Client A Running - Please Enter your message: ")
    try:
        inputBytes = str.encode(message)
        sock.sendall(inputBytes)
        response = str(sock.recv(1024))
        print("Received: {}".format(response))
    finally:
        sock.close()

client(HOST, PORT)