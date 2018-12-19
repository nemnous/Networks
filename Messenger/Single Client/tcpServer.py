import socket
def main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, addr = s.accept()
	print ("connection from : " + str(addr))
	while True:
	    data = c.recv(1024).decode()
	    if not data:
	        break
	    print ("from connected user :" + str(data))
	    data = str(data).split(" ")
	    res = float(data[2]) / 67.0

	    print ("sending :" + str(res))
	    c.send(str(res).encode())
	c.close()
if __name__ == "__main__":
	main()