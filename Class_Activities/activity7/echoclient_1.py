# import the socket library
import socket
#set the name of the server machine
#change it to the name of your machine!
host = 'signals20.bu.edu'
#set port number of server to connect on
#must be same as set in server file
port = 50000
#create TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sets maximum size of a message
size = 1024
#connect to server
s.connect((host,port))
#create message
#change the message with your first name and last name!
message = 'Hello, Selena Liu!'
#encode message
encodedMessage = message.encode()
#send message to server
s.send(encodedMessage)
#get message from server
data = s.recv(size)
#decode message from server
decodedData = data.decode()
#close socket
s.close()
#print message
print('[server]', decodedData)
