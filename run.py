#run.py
#Run the whole thing

from client import *
import dog_device

HOST = '18.220.180.253' 
PORT = 50000

client = socket.socket()
client.connect((HOST, PORT))

while True:
	button = raw_input(">")
	if button == "quit":
		break
	client_send(HOST, PORT, "DEVICE")	
#	client_send(HOST, PORT, button)

	
client.close()

