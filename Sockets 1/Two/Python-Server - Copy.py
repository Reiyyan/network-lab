import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print("Attempting to start Server...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server Started")
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on Host: {HOST} - PORT: {PORT}")
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)