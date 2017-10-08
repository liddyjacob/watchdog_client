#run.py
#Run the whole thing

PIN = 29
HOST = '18.220.180.253'
PORT = 64646


from client import *
import dog_device
import time
import mraa

button= mraa.Gpio(PIN)
button.dir(mraa.DIR_OUT)


while True:
    
    state = button.read()
    if state == 1:
        client_send(HOST, PORT, "DEVICE")	
        time.sleep(5)
        state = button.read()

        if state == 1: 
            break;
        
        

	
client.close()

