# import socket
import threading
import socketserver

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        clientString = data.decode("utf-8")
        print(f"---------------------------------------------------------\nRunning on thread: {cur_thread}\nNew Client request at server\nClient requested: {clientString}")
        returnString = clientString.upper()
        response = str.encode(returnString)
        self.request.sendall(response)
        print(f"Sent Response: {returnString}")
        print("---------------------------------------------------------\n")

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
# ip, port = server.server_address

# start a thread with the server. 
# the thread will then start one more thread for each request.

try:
    print("Server loop running with Async Threading")
    server_thread = threading.Thread(target=server.serve_forever())
    # exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
except KeyboardInterrupt:
    print("Received Shutdown Request from Keyboard Interrupt!\nGoodbye! :)")
server.shutdown()