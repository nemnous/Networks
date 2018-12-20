import socket
import threading
import sys
import getpass
def receive(s, username):
    while True:
        try: 
            data = s.recv(1024).decode()
            if not data:
                continue
            print(str(data))
        except:
            print("Server Disconnected")
            sys.exit()
            break
        

def main():
    # remote_server = "google.com"
    # with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    #     s.connect((remote_server, 80))
    #     host = s.getsockname()[0]
    print('\n \n \n ****** WELCOME TO NEMNOUS MESSENGER ****** \n \n')

    host = input('Enter the Server IP:')
    port = 5000
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        print('       Retry the connection to server \n       Possible causes' + host + ' is wrong host address')
        sys.exit()
    print(s.recv(1024).decode())
    password = getpass.getpass()
    s.send(password.encode())
    print(s.recv(1024).decode())

    print(s.recv(1024).decode())

    username = input()
    s.send(username.encode())
    threading.Thread(target = receive, args = (s, username)).start()
    while True:
        inp = input('->')
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