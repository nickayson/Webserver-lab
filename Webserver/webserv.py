# hello world is http://127.0.0.1:5500/helloworld.html 

#import socket module for the library
from socket import *
import sys # In order to terminate the program

def webServer(port = 5500):
    serverHost = '127.0.0.1' #server host or ip address for html is declared
    serverPort = 5500 #port number for the server is saved

    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    serverSocket.bind((serverHost, serverPort)) #bind the host and port together
    serverSocket.listen(1)

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()#accepts the connection
        try:
            message = connectionSocket.recv(1024)#receive the maximum amount of bits in message

            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read() #read file line
            #Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\n\n".encode())    #gives the ok if connection was good

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            #Send response message for file not found
            print("404 Not Found")
            connectionSocket.send("HTTP/1.1 404 Not Found\n\n".encode()) #sends the 404 not found message if html connection doesnt match up
            #Close client socket
            connectionSocket.close()
            break
    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(5500)