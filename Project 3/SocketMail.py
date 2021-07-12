from socket import *
import ssl
import base64
import sys

# Debug
verbose = False

# Login Info - Must have less secure apps allowed in Gmail.
username = "ccps706test@gmail.com"
password = "ryerson2021"

# Mail Details
if(len(sys.argv) == 2):
    receiver = sys.argv[1]
    msg = "\r\nI love computer networks!"
elif(len(sys.argv) == 3):
    receiver = sys.argv[1]
    msg = f"{sys.argv[2]}\r\n"
else:
    receiver = "reiyyan@gmail.com"
    msg = "\r\nI love computer networks!"
    
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = ("smtp.gmail.com", 465)
#Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
# Wrap socket with TLS wrapper to get security
#Fill in start
clientSocket = ssl.wrap_socket(socket(AF_INET, SOCK_STREAM), ssl_version=ssl.PROTOCOL_TLSv1)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Authentication
authMesg = 'AUTH LOGIN\r\n'
crlfMesg = '\r\n'

# Tell server we are trying to authenticate
clientSocket.send(authMesg.encode('utf-8'))
recv2 = clientSocket.recv(2048).decode()
if verbose:
    print(recv2)

# Encode Username and Pw for server must be in base64
user64 = base64.b64encode(username.encode('utf-8'))
pass64 = base64.b64encode(password.encode('utf-8'))

# Tell server our Username
clientSocket.send(user64)
clientSocket.send(crlfMesg.encode('utf-8'))
recv3 = clientSocket.recv(2048).decode()
if verbose:
    print(recv3)

# Tell server our Password
clientSocket.send(pass64)
clientSocket.send(crlfMesg.encode('utf-8'))
recv4 = clientSocket.recv(2048).decode()
if verbose:
    print(recv4)

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = f"MAIL FROM: <{username}>\r\n"
clientSocket.send(mailFrom.encode())
recv5 = clientSocket.recv(2048).decode()
if verbose:
    print(recv5)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
mailTo = f"RCPT TO: <{receiver}>\r\n"
clientSocket.send(mailTo.encode())
recv6 = clientSocket.recv(2048).decode()
if verbose:
    print(recv6)
# Fill in end

# Send DATA command and print server response.
# Fill in start
mailData = "DATA\r\n"
clientSocket.send(mailData.encode())
recv7 = clientSocket.recv(2048).decode()
if verbose:
    print(recv7)
# Fill in end

# Rei: Adding in section for to and subject (Optional)
subject = f"To: {receiver}\r\n" 
clientSocket.send(subject.encode())

subject = "Subject: CCPS706 Test Mail\r\n\r\n" 
clientSocket.send(subject.encode())

# Send message data.
# Fill in start
body = f"{msg} \r\n"
clientSocket.send(body.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv8 = clientSocket.recv(2048).decode()
if verbose:
    print(recv8)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitMail = "QUIT\r\n"
clientSocket.send(quitMail.encode())
recv9 = clientSocket.recv(2048).decode()
print(recv9)
# Fill in end

clientSocket.close()