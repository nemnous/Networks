import socket
import os
# def get_my_ip_address(remote_server="google.com"):
    # """
    # Return the/a network-facing IP number for this system.
    # """

# prx = input('1. Proxy Network \n 2. No Proxy Network')
# if prx == 1:
# 	proxyHost = input('Enter Proxy Host')
# 	port = input('Enter Port')
# 	proxyUser = input('Enter Proxy username')
# 	proxyPassWord = input('Enter Proxy Password')
# 	setHTTP = 'HTTP_PROXY=http://' + proxyUser + ':' + proxyPassWord + '@' + proxyHost + ':' + port
# 	setHTTPS = 'HTTPS_PROXY=http://' + proxyUser + ':' + proxyPassWord + '@' + proxyHost + ':' + port
# 	# os.system(HTTP_PROXY=http://nani.botta.123:msit1234@10.10.10.3:3128)
# 	os.system(setHTTP)
# 	os.system(setHTTPS)
# else:
	
remote_server = "google.com"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    s.connect((remote_server, 80))
    print(s.getsockname()[0])