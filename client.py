import socket

#The job of thd
def client_send(host, port, info):
	client = socket.socket()
	client.connect((host, port))
	client.send(info)

