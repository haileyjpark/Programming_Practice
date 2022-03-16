from socket import *
import threading, time


def send(sock):
    while True:
        sendData = input('>>> ')
        sock.send(sendData.encode('utf-8'))
        
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('Friend : ', recvData.decode('utf-8'))

port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)

print("waiting for the port number%d ... "%port)

connectionSock, address = serverSock.accept()

print('Connection has been established from :' + str(address))

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
