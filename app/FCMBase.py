class DeviceID():
	device_info=dict()

	def get_data(self,json_data):
		for device,fcm in json_data.iteritems():
			self.device_info[device] =fcm

	def print_data(self):
		for device,fcm in self.device_info.iteritems():
			print device+" "+fcm


class Target_Device():
	device = ""
	fcm_token= ""

	def __init__(self):
		device = " "
		fcm_token = " "

	def target_device(self,device,fcm_token):
		self.device=device
		self.fcm_token = fcm_token