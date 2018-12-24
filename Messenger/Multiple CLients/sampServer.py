import socket
import threading

s = socket.socket()

ip = '10.1.134.212'
port = 2333

s.bind((ip, port))

s.listen()

client, address = s.accept()
print('client:' + str(client) + 'address:' + str(address))

def receive(client):
    while True:
        ms = client.recv(1028).decode()
        if len(ms) == 0:
            continue
        print(ms)

threading.Thread(target = receive, args = (client,)).start()

while True:
    print('Enter message')
    ms = input()
    client.send(ms.encode())

