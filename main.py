#import socket module 
from socket import * 
import sys # In order to terminate the program 
import json
 
serverSocket = socket(AF_INET, SOCK_STREAM) 
# #Prepare a sever socket 
# #Fill in start 
serverSocket.bind(("",3001))
serverSocket.listen(1)
# #Fill in end 
while True: 
    #Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept() #Fill in        
    try: 
        message = connectionSocket.recv(5000)
        print(message)
        if (message == b''):
            continue
        path = message.split()[1][1:].decode("utf8").split("/")
        protocol = message.split()[0].decode("utf8")
        print(protocol)
        print(path)
        #Send one HTTP header line into socket 
        #Fill in start 
        connectionSocket.send('\r\nHTTP/1.1 200 OK'.encode())
        connectionSocket.send('\r\nAccess-Control-Allow-Origin: *'.encode())
        connectionSocket.send('\r\nAccess-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept\r\n\r\n'.encode())

        if path[0] == '':
            f = open("index.html")
            outputdata = f.read()       
            print(outputdata)
            connectionSocket.send(outputdata.encode())   
        
        elif path[0] == 'manifest.json' or path[0] == "static":
            f = open(message.split()[1][1:].decode("utf8"))
            outputdata = f.read()
            connectionSocket.send(outputdata.encode())
        
        # REST API routing

        # /shop - GET
        # Return all available items in JSOn form
        elif path[0] == "shop" and protocol == "GET":
            f = open("shop.json")
            outputdata = f.read()
            print(outputdata)
            connectionSocket.send(outputdata.encode())
            f.close()

        # /purchase - POST
        # Take and validate payment/shipping info.
        # If valid info, then return receipt
        # As a bonus, send receipt in an email
        elif path[0] == "purchase" and protocol == "POST":
            shop_f = open("shop.json")
            dictionary = json.load(shop_f)
            print(dictionary)
            shop_f.close()
            payload_length = int(message.decode("utf-8").split("Content-Length: ")[1].split("\r\n")[0])
            print(payload_length)
            payload = json.loads(message[-payload_length:].decode("utf-8"))
            orders_f = open("orders.txt", "a")
            orders_f.write(payload["email"] + "\t" + payload["fullName"] + "\n")
            for id in payload["purchases"]:
                orders_f.write("\t" + id + "\n")
            orders_f.close()

        else:
            raise IOError
         
    except IOError: 
    #     #Send response message for file not found 
    #     #Fill in start         
        connectionSocket.send("HTTP/1.1 404 Not Found".encode())
    #     #Fill in end 
    #     #Close client socket 
    #     #Fill in start 
        connectionSocket.close()
    #     #Fill in end
    
    connectionSocket.close() 

serverSocket.close() 
sys.exit()#Terminate the program after sending the corresponding data
