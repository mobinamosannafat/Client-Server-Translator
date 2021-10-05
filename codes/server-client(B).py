import socket #**
from socket import AF_INET, SOCK_STREAM


serverPortTCP = 12000
serverPortUDP = 8080 ####
serverName = '127.0.0.1'  #local host

# ******** part1 : program B acts like a TCP server ******** #
#create TCP welcoming socket
serverSocket = socket.socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPortTCP))
serverSocket.listen(1) #wating for client
print ("The program(B) is ready to receive")
while 1:  #loop forever
     connectionSocket, addr = serverSocket.accept()  #server waits on accept() for incoming requests, new socket created on return
     clientSentence = connectionSocket.recv(1024) #Read from TCP socket into clientSentence
     clientSentence2=clientSentence.decode('utf-8') #convert clientSentence from byte to string
     print ("( ",clientSentence2, " ) is recieved from client and send to server")

    # ******** part2 : program B acts like a UDP client ******** #
     clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #create UDP socket for server
     clientSocket.sendto(clientSentence,(serverName, serverPortUDP)) #Attach server name, port to message; send into socket
                                                                                      #first encod clientInput (convert string to byte)
     ServrSentence, serverAddress = clientSocket.recvfrom(2048) #read reply characters from socket into ServrSentence
     ServrSentence2 = ServrSentence.decode('utf-8') #first decode answer from server , it should be convert to string to be display 
     print ("( ", ServrSentence2, " ) is recieved from server and send to client")

    # ********** Continuation of the part1 ********** #
     connectionSocket.send(ServrSentence) #read bytes from socket (but not address as in UDP)
     connectionSocket.close() #close connection to this client (but not welcoming socket)

