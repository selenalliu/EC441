from socket import *
import sys

# Message to be sent

msg = '\r\n I love sending e-mails!'.encode()
endmsg = '\r\n.\r\n'.encode()

# Choose a BU mail server and call it mailserver
mailserver = "relay.bu.edu"

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM) # same as web server program

host = mailserver
port = 25
clientSocket.connect((host,port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
	sys.exit(1)

# Send HELO command and print server response
heloCommand = ('HELO ' + mailserver + '\r\n').encode()
print(heloCommand)
clientSocket.send(heloCommand)

recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server')
	sys.exit(1)

# Send MAIL FROM command and print server response. Only use your own email address!
mailfromCommand = ('MAIL FROM: <ethanl66@bu.edu>\r\n').encode()
print(mailfromCommand)
clientSocket.send(mailfromCommand)

recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
	print('250 reply not received from server')
	sys.exit(1)

# Send RCPT TO command and print server response.
rcpttoCommand = ('RCPT TO: <lebronjames69696969669696@bu.edu>\r\n').encode()
print(rcpttoCommand)
clientSocket.send(rcpttoCommand)

recv3 = clientSocket.recv(1024).decode()
print (recv3)
if recv3[:3] != '250':
	print('250 reply not received from server')
	sys.exit(1)

# Send DATA command and print server response
dataCommand = 'DATA\r\n'.encode()
print(dataCommand)
clientSocket.send(dataCommand)

recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
	print('354 reply not received from server')
	sys.exit(1)

# Send message data
clientSocket.send(msg)
print(msg)

# Message ends with a single period
clientSocket.send(endmsg)
print(endmsg)

recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
        print('250 reply not received from server')
        sys.exit(1)

# Send QUIT command and get server response
quitCommand = ('QUIT\r\n').encode()
clientSocket.send(quitCommand)
print(quitCommand)

recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
	print('221 reply not received from server')
	sys.exit(1)

# Close client socket
clientSocket.close()

