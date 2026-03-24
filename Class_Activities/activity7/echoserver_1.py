# import the socket library
import socket
# set the host name: empty string means local machine
host = ''
#set the port number
#may need to use a different port, if already in use
port = 50000
# maximum number of waiting connections
backlog = 5
#create a TCP/IP socket, stored in variable s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind socket to host and port
s.bind((host,port))
# listen for incoming connection
s.listen(backlog)
#set maximum size of a message
size = 1024
#creates new socket client to communicate with client
client, address = s.accept()
#get data from client
data = client.recv(size)
#send message back to client
client.send(data)
#close socket
client.close()
s.close()

