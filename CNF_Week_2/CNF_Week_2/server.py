import socket
import threading
import csv


s = socket.socket()

ip = '10.10.8.232'
port = 5000

s.bind((ip, port))

s.listen()

path = 'F:/PROGRAMMING/Networks/CNF_Week_2/CNF_Week_2/'

file=open( path +"data.CSV", "r")
reader = csv.reader(file)
# for line in reader:
#     t=line[0],line[1],line[2]
#     print(t)

def receive(client):
	while True:
		msg  = client.recv(1024).decode()
		if msg == '':
			continue
		response = msg.split(" ")
		print(response)
		user = response[1].strip()
		secQues = ''
		secAns = ''
		if response[0] == 'MARK-ATTENDANCE':
			respText = ''
			for line in reader:
				if line[0].strip() == user:
					secQues = line[1]
					secAns = line[2]
					respText = 'SECRETQUESTION-' + line[1]

			if respText == '':
				client.send('ROLLNUMBER-NOTFOUND'.encode())
			else:
				client.send(respText.encode())
				secAnsRecv = client.recv(1024).decode().split(" ")
				# print(secAnsRecv)
				# print(secAns)

				if secAnsRecv[0] == 'SECRETANSWER':
					Resans = True
					while Resans:
						if secAnsRecv[1] == str(secAns):
							# print('True Ans')
							Resans = False
							client.send('ATTENDANCE-SUCCESS'.encode())
						else:
							client.send('ATTENDANCE FAILURE'.encode())
							client.send(secQues.encode())
							secAnsRecv = client.recv(1024).decode().split(" ")


while True:
	client, addr = s.accept()
	threading.Thread(target = receive, args  = (client,)).start()
	