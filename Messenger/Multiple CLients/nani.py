#CLIENT


import socket
import threading

s=socket.socket()
port=2333

ip="10.1.134.212"

s.connect((ip,port))


def receive(s):
	while True:
		ms = s.recv(1028).decode()
		if len(ms) == 0:
			continue
		print(ms)

threading.Thread(target = receive, args = (s,)).start()

while True:
    print('Enter message')
    ms = input()
    s.send(ms.encode())

