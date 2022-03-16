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

host = '147.182.224.90'
port = 8081

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((host, port))

print('You are now connected.')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
