import socket
import threading
import socketserver

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        clientString = data.decode("utf-8")
        print(clientString)
        # response = bytes("{}: {}".format(cur_thread.name, data))
        response = data
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
ip, port = server.server_address

# start a thread with the server. 
# the thread will then start one more thread for each request.
server_thread = threading.Thread(target=server.serve_forever)

# exit the server thread when the main thread terminates
# server_thread.daemon = True
server_thread.start()

print("Server loop running in thread:", server_thread.name)

# server.shutdown()
# import time

# time.sleep(5)