import socket
import threading


def clientchat(c, clients):
    # print('send message after entering s first')
    while True:
        try:
            msg = c.recv(1024).decode()
        except:
            print('user disconnected')

        for key, value in clients.items():
            value.send(msg.encode())
def main():
    host = '10.10.8.232'
    port = 5000
    s = socket.socket()
    s.bind((host, port))
    s.listen()
    clients = {}
    while True:
        c, addr = s.accept()
        message = "User name enter chey bey: \n"
        c.send(message.encode())
        username = c.recv(1).decode()
        conMsg = username + ' got connected'
        print(conMsg)
        if username not in clients:
            clients[username] = c
        for key, value in clients.items():
            value.send(conMsg.encode())
        threading.Thread(target = clientchat, args = (c, clients)).start()


if __name__ == "__main__":
    main() 
 
