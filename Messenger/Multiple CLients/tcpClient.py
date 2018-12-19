import socket
import threading

def receive(s, username):
    while True:
        data = s.recv(1024).decode()
        if not data:
            continue
        print(str(data))

def main():
    host = '192.168.137.93'
    port = 5000
    s = socket.socket()
    s.connect((host, port))
    msg = s.recv(1024).decode()
    print(msg)
    username = input()
    s.send(username.encode())
    threading.Thread(target = receive, args = (s, username)).start()
    while True:
        inp = input()
        message = username + ':' + inp
        # per = inp.split(" ")
        if inp == 'online':
            s.send(inp.encode())
        # elif per[0] = 'private':
            
        else:
            s.send(message.encode())
    s.close()

if __name__ == "__main__":
    main()