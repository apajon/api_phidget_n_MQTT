#!/usr/bin/env python

from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.Encoder import *
import traceback


import sys
if sys.version_info.major==2:
    import ConfigParser #Python 2
if sys.version_info.major==3:
    import configparser #Python 3
if sys.version_info.major!=2 and sys.version_info.major!=3:
    print("bad python version")
    sys.exit()

# import paho.mqtt.client as mqtt #import the client

from lib import phidget22Handler as handler
from lib import MQTT_client

############
#import config file
config = ConfigParser.ConfigParser()

print("opening configuration file : config.cfg")
config.read('config.cfg')

############
#connect to mqtt broker
# broker_address="localhost"
# print("MQTT creating new instance")
# client = mqtt.Client("Encoder") #create new instance
# print("MQTT setting  password")
# client.username_pw_set(username="admin",password="movitplus")
# print("MQTT connecting to broker")
# client.connect(broker_address) #connect to broker

client=MQTT_client.createClient("Encoder",config)
client.publish(config.get('MQTT','topic'),"OFF")


############
def main(config_):
    try:
        Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
        #Create your Phidget channels
        encoder0 = Encoder()

        #Set addressing parameters to specify which channel to open (if any)
        encoder0.client=client
        encoder0.clientTopic=config.get('MQTT','topic')

        #Assign any event handlers you need before calling open so that no events are missed.
        encoder0.setOnPositionChangeHandler(handler.onPositionChange)
        encoder0.setOnAttachHandler(handler.onAttach)
        encoder0.setOnDetachHandler(handler.onDetach)

        #Open your Phidgets and wait for attachment
        encoder0.openWaitForAttachment(5000)

        #Do stuff with your Phidgets here or in your event handlers.

        #Change the data interval from the encoder based on config datas
        encoder0.setDataInterval(config_.getint('encoder','dataInterval'))

        #Interupt script by pressing Enter
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

############
main(config)
