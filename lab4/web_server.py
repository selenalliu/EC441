# import socket library
from socket import *

# Prepare server socket
host = '' # or ''
port = 50069
backlog = 5 # max number of waiting connections

# Create TCP/IP socket stored in var serverSocket
serverSocket = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM means TCP (vs SOCK_DGRAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind((host, port)) # bind socket to host and port
serverSocket.listen(backlog)

while True:
	
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept() # creates new socket client to communicate with client
    size = 1024
    try:
        message = connectionSocket.recv(size) # Reads <= 1024 bytes from client request. Raw HTTP req data sent by the client
        filename = message.split()[1] # Client HTTP req (likely GET)’s. 2nd part (split()[1]) typically contains path to requested file (e.g., /index.html)
        f = open(filename[1:])
        
        # Read file
        outputdata = f.read() #the file to serve

        # Send HTTP status line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) # 200 OK, encode converts string into bytes

        # Send Last-Modified HTTP header line into socket
        connectionSocket.send("Last-Modified: Thu, 17 Oct 2024 20:31:33\r\n".encode()) # hard-coded date

        # Send content of requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n\r\n".encode())

        # Close file and client socket
        f.close()
        connectionSocket.close()

    except IOError: # IOError occurs when file not found/cannot be opened
        
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
     
        # Close client socket
        connectionSocket.close()

serverSocket.close()
