from socket import *

def translator(message):
    
    m1 = "Baran Mibarad"
    a1 = "It's raining"

    m2 = "Music morede alaghe to kodam ast?"
    a2 = "What is your favorite music?"
    
    m3 = "Man daram ketabe Dezire ra mikhanam"
    a3 = "I'm reading Desiree"

    m4 = "Man asheghe range sefid hastam"
    a4 = "I love white"

    m5 = "To kheili mehraban hasti"
    a5 = "You're very kind"

    a6 = "Wrong message"

    if message == m1:
        return a1
    elif message == m2: 
        return a2
    elif message == m3: 
        return a3
    elif message == m4: 
        return a4
    elif message == m5: 
        return a5
    else :
        return a6

serverPort = 8080
serverName = '127.0.0.1'
serverSocket = socket(AF_INET, SOCK_DGRAM)  #create UDP socket
serverSocket.bind((serverName, serverPort)) #bind socket to local port number 8080
print ("The server is ready to receive")
while 1:  #loop forever
    message, clientAddress = serverSocket.recvfrom(2048)  #Read from UDP socket into message, getting client’s address (client IP and port)
    message2 = message.decode('utf-8')  #convert message from byte to string
    translatedMessage = translator(message2) #answer to client with specific sentence
    print ("Server answer to ",message2, "is : ", translatedMessage)
    serverSocket.sendto(translatedMessage.encode('utf-8'), clientAddress) #send answer back to this client

