# hello world is http://127.0.0.1:5500/helloworld.html 

#import socket module for the library
from socket import *
# In order to terminate the program
import sys 

def webServer(port = 5500):
    #server host or ip address for html is declared
    serverHost = '127.0.0.1'   
    #port number for the server is saved 
    serverPort = 5500           

    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    serverSocket.bind((serverHost, serverPort))      
    #bind the host and port together
    serverSocket.listen(1)

    while True:
        #Establish the connection
        print('Ready to serve...')
        #accepts the connection
        connectionSocket, addr = serverSocket.accept()
        try:
            #receive the maximum amount of bits in message
            message = connectionSocket.recv(1024).decode()

            filename = message.split()[1]
            f = open(filename[1:])
            #read file line
            outputdata = f.read() 
            #Send one HTTP header line into socket
            print("HTTP 200 OK")                                        #tells terminal it is all good
            connectionSocket.send("HTTP/1.1 200 OK\n\n".encode())       #gives the ok if connection was good

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            #Send response message for file not found
            print("404 Not Found")                                              #gives terminal not found message
            connectionSocket.send("HTTP/1.1 404 Not Found\n\n".encode())        #sends the 404 not found message if html connection doesnt match up
            #Close client socket
            connectionSocket.close()
            break
    serverSocket.close()
    sys.exit()                                                          #Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(5500)