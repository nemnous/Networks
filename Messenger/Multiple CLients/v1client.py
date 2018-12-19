import socket
import threading

def receive(s, username):
    while True:
        data = s.recv(1024).decode()
        if not data:
            continue
        print (str(data))

# def send(s, username):
#     while True:
#         message = input()
#         s.send(message.encode())

def main():
    host = '10.10.8.232'
    port = 5000
    s = socket.socket()
    s.connect((host, port))
    msg = s.recv(1).decode()
    print(msg)
    username = input()
    s.send(username.encode())
    # threading.Thread(target = send, args = (s, username)).start()

    threading.Thread(target = receive, args = (s, username)).start()

    while True:
        message = username + ':' + input() + '\n'
        s.send(message.encode())
    #     data = s.recv(1024).decode()
    #     print (str(data))

    s.close()
if __name__ == "__main__":
    main()