# import socket module
from socket import socket, AF_INET, SOCK_STREAM
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
#Fill in start
# I will use localhost
serverSocket.bind(('127.0.0.1', 1992))
serverSocket.listen(1)
#Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    #Fill in end

    try:
        isImage = False
        # Fill in start
        message = connectionSocket.recv(1024)
        #Fill in end
        filename = message.split()[1]
        nameStr = filename.decode()

        if(nameStr.find("html") > 0):
            isImage = False
        else:
            isImage = True
            
        if (isImage):
            outputdata = open(filename[1:], 'rb')
            myImageBytes = outputdata.read()
            connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
            connectionSocket.send("Content-Type: image/jpeg\r\n".encode())
            connectionSocket.send("Accept-Ranges: bytes\r\n\r\n".encode())
        else:
            f = open(filename[1:])
            outputdata = f.read()
            f.close()

            # Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            #Fill in end

        # Send the content of the requested file to the client
        if(isImage):
            connectionSocket.send(myImageBytes)
        else:
            for i in range(0, len(outputdata)):
                # print(outputdata[i])

                    connectionSocket.send(outputdata[i].encode())
                # connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        # connectionSocket.send('404 Not Found'.encode())
        #Fill in end
        # Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
