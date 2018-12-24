import socket

remote_server = "google.com"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc: 
    soc.connect((remote_server, 80))
    host = soc.getsockname()[0]
    print(host)

    