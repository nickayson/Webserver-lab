# hello world is http://127.0.0.1:5501/helloworld.html 

#import socket module
from socket import *
import sys # In order to terminate the program
serverHost = '127.0.0.1'
serverPort = 5501
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
while True:
#Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024)#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()#Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
        connectionSocket.send("\r\n") 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        #Fill in end
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        #Close client socket
        #Fill in start
        #Fill in end
        connectionSocket.close()
        break
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data