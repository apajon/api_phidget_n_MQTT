from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.Encoder import *
import traceback
import time

#Declare any event handlers here. These will be called every time the associated event occurs.

def onPositionChange(self, positionChange, timeChange, indexTriggered):
	print("PositionChange: " + str(positionChange))
	print("TimeChange: " + str(timeChange))
	print("IndexTriggered: " + str(indexTriggered))
	print("----------")

def onAttach(self):
	print("Attach!")

def onDetach(self):
	print("Detach!")

def main():
	try:
		Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
		#Create your Phidget channels
		encoder0 = Encoder()

		#Set addressing parameters to specify which channel to open (if any)

		#Assign any event handlers you need before calling open so that no events are missed.
		encoder0.setOnPositionChangeHandler(onPositionChange)
		encoder0.setOnAttachHandler(onAttach)
		encoder0.setOnDetachHandler(onDetach)

		#Open your Phidgets and wait for attachment
		encoder0.openWaitForAttachment(5000)

		#Do stuff with your Phidgets here or in your event handlers.

		try:
			input("Press Enter to Stop\n")
		except (Exception, KeyboardInterrupt):
			pass

		#Close your Phidgets once the program is done.
		encoder0.close()

	except PhidgetException as ex:
		#We will catch Phidget Exceptions here, and print the error informaiton.
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()
