import socket
import threading

def receive(s, username):
    while True:
        try: 
            data = s.recv(1024).decode()
        except:
            print("Server Disconnected")
            break
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
        message = username + '>' + inp
        per = inp.split(" ")
        if inp == 'online':
            s.send(inp.encode())
        elif per[0] == 'private':
            print('enter message for ' + per[1])
            s.send((per[0] + ":" + per[1] + ":" + username + '>' + input()).encode())
        else:
            s.send(message.encode())
    s.close()

if __name__ == "__main__":
    main()