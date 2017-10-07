#dog_device: the device the dog is activating.
import phys_device

#A generic device to be used 
class Dog_device:
	def __init__(self, desc):
		self.desc = desc


class Outside_device(Dog_device):
	#physical_device - the actual 'button' being used
	def __init__(self, physical_device):
		Dog_device.__init__(self, "Outside_device")
		self.phys_device = physical_device
		


	#Check if the physical device has been activated:
	def check(self):
		phys_device.check()
		#TODO: Check status of button, once implimented

	




class Bowl_device(Dog_device):
	def __init__(self):
		Dog_device.__init__(self, "Bowl_device")



	
