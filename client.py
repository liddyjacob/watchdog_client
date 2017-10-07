import socket


port = 50000
host = "18.220.180.253"

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket()

# connect the client
# client.connect((target, port))
client.connect((host, port))

print client.recv(1024)

client.close()

