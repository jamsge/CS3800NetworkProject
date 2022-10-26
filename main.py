#import socket module 
from socket import * 
import sys # In order to terminate the program 
 
serverSocket = socket(AF_INET, SOCK_STREAM) 
# #Prepare a sever socket 
# #Fill in start 
serverSocket.bind(("",3000))
serverSocket.listen(1)
# #Fill in end 
while True: 
    #Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept() #Fill in        
    try: 
        message = connectionSocket.recv(1024)
        # print(message)
        path = message.split()[1][1:].decode("utf8").split("/")
        print(path)
        #Send one HTTP header line into socket 
        #Fill in start 
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        connectionSocket.send("test123".encode())   
        connectionSocket.send("\r\n".encode()) 
         
        connectionSocket.close() 
    except IOError: 
    #     #Send response message for file not found 
    #     #Fill in start         
        connectionSocket.send("HTTP/1.1 404 Not Found".encode())
    #     #Fill in end 
    #     #Close client socket 
    #     #Fill in start 
        connectionSocket.close()
    #     #Fill in end             
    
serverSocket.close() 
sys.exit()#Terminate the program after sending the corresponding data