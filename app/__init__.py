from flask import Flask
from pyfcm import FCMNotification
import config
import FCMBase


app = Flask(__name__)

FCMObject = FCMBase.DeviceID()
FCMTarget = FCMBase.Target_Device()

@app.route('/')
def index():
	return "Service is running"

@app.route('/getdevicefcm')
def getFCMID():
	# Input FCMObject and use it to display in Indra 
	return "Query The DB"

@app.route('/select_target/<device>/<fcmtoken>')
def initialise_target_device(device,fcmtoken):
	FCMTarget.target_device(device,fcmtoken)
	return "FCMTarget initialised"

@app.route('/push_notification')
def send_target():
	MessageDelegator = FCMNotification(api_key=config.API_KEY)
	message = "Hi , From Jayanth"
	response = MessageDelegator.notify_single_device(registration_id=FCMTarget.fcm_token,message_body=message)
	if response['success'] == 1 :
		return "Message Sent"




