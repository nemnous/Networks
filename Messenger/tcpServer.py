import socket
import threading
import getpass
clients = {}
def clientchat(c, clients):
    while True:
        try:
            msg = c.recv(1024).decode()
            # nameSplit = msg.split(':')
            # user = nameSplit[0]
            # fileName = user + '.txt'
            priSplit = msg.split(':')

            # request of private message forwarded to the specific user
            if priSplit[0] == 'private':
                if priSplit[1] in clients:
                    clients[priSplit[1]].send(priSplit[2].encode())
                else:
                    c.send((priSplit[1] + ' is offline').encode())
                continue
            # Request of online users send to requested client
            if msg == 'online':
                onl = ''
                for key, value in clients.items():
                    onl += (key + '\n')
                c.send(onl.encode())
                continue
            # Chat log stored in log.txt
            with open('log.txt','a') as f:
                f.write(msg + '\n')
                f.close()
        # closing a client creates an exception which is used to know the other users
        # that the user is disconnected.
        except:
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
        for key, value in clients.items():
            value.send(msg.encode())
        

def main():
    #used to get the ipv4 address that is connected to the network
    remote_server = "google.com"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc: 
        soc.connect((remote_server, 80))
        host = soc.getsockname()[0]
    # print('Connect the client to this host:' + host)
    port = 5000
    print('\n \n \n ****** WELCOME TO NEMNOUS MESSENGER ****** \n \n')
    grpName = input('Enter Group Name:')
    password = getpass.getpass('Set Password for' + grpName)
    # print(password)
    s = socket.socket()
    print('Nemnous Messenger is ONLINE')
    print('\t Room Name:'+grpName)
    print('\t Password:' + password)
    print('\t Host Address:' + host)
    s.bind((host, port))
    s.listen()
    # clients = {}
    while True:
        c, addr = s.accept()
        c.send(('Enter Password for' + grpName).encode())
        if c.recv(1024).decode() != password:
            c.send('Please check your password and try again'.encode())
            c.close()
            continue
        else:
            c.send(('You are now connected to '+grpName).encode())
        message = "Username:"
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