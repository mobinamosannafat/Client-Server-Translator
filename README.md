# Client Server Translator

This project includes theree python files: 
- Server-Client(B): A TCP-server for program C and a UDP-client for program A. This program is written with the combination of TCP and UDP which receive a message from C, transmit it to A, then receive the answer from A and finally transmit the answer to C.
- Clien(C): A TCP-client which receive a message from user and transmit it to B, then receive answer of message from B and show it to user.
- Server(A): A UDP-client which receive a message from B and choose appropriate answer for it, then send the answer to B.

You can find the source codes in the [codes directory](./codes).
