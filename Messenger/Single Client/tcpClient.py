import socket
def main():
	user = input("Enter Username:")
	host = '10.10.8.232'
	port = 3121
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	message = input(user + "->")
	message = user + ":" + message
	while message != user + ':q':
		s.send(message.encode())
		data = s.recv(1024).decode()
		print (str(data))
		message = user + ":" + input(user + "->")
	s.close()
if __name__ == "__main__":
	main()