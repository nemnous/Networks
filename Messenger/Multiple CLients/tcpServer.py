import socket
import threading

clients = {}
def clientchat(c, clients):
    while True:
        try:
            msg = c.recv(1024).decode()
        except:
            msg = ''
            for key, value in clients.items():
                if value == c:
                    discUser = key
                    break
            msg = discUser + ' got disconnected'
            print(msg)
            if discUser in clients:
                del clients[discUser]

            for key, value in clients.items():
                value.send(msg.encode())

            break
        # print(clients)
        for key, value in clients.items():
            value.send(msg.encode())
        

def main():
    host = '192.168.137.93'
    port = 5000
    s = socket.socket()
    s.bind((host, port))
    s.listen()
    # clients = {}
    while True:
        c, addr = s.accept()
        message = "User name enter chey bey: \n"
        c.send(message.encode())
        username = c.recv(1024).decode()
        conMsg = username + ' got connected'
        print(conMsg)
        if username not in clients:
            clients[username] = c
        for key, value in clients.items():
            value.send(conMsg.encode())
        threading.Thread(target = clientchat, args = (c, clients)).start()

if __name__ == "__main__":
    main()