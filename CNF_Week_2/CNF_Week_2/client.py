import socket
import threading
import sys
def receive(s):
    while True:
        data = s.recv(1024).decode()
        if not data:
            continue
        if data == 'ATTENDANCE-SUCCESS':
            print(data)
            sys.exit()
        else:
            print(data)
            

def main():
   

    host = input('Enter the Server IP:')
    port = 5000
    s = socket.socket()

    s.connect((host, port))
    
    print('Server connected')

    s.send(input().encode())
    threading.Thread(target = receive, args  = (s,)).start()
    while True:
        s.send(input().encode())

if __name__ == "__main__":
    main()