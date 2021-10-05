import socket
serverName = '127.0.0.1'  #local host
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create TCP socket for server, remote port 12000 
clientSocket.connect((serverName,serverPort))  #connect to server(B) on port 12000
clientInput= input("Enter your sentence: ")
clientSocket.send(clientInput.encode('utf-8')) #No need to attach server name, port  Because the connection has already been established #****
                                               #first encod clientInput (convert string to byte)
modifiedAnswer = clientSocket.recv(1024)       #Receive answer from server 
print ("Server answered: ", modifiedAnswer.decode('utf-8')) #first decode answer from server , it should be convert to string to be display #****
clientSocket.close()
