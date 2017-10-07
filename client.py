import socket

#The job of thd
def client_send(port, host, info):
	client = socket.socket()
	client.connect((host, port))
	client.send(info)

