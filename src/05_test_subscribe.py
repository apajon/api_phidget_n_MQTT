import paho.mqtt.client as mqtt #import the client1
import json
import time
import os

import sys
if sys.version_info.major==2:
    import ConfigParser #Python 2
if sys.version_info.major==3:
    import configparser #Python 3
if sys.version_info.major!=2 and sys.version_info.major!=3:
    print("bad python version")
    sys.exit()

from lib import createLoggerFile as logger

# ############
# #intialize timer
# t0 = time.time()
# 
############
#import config file
config = ConfigParser.ConfigParser()

config.read('config.cfg')

############
#filename from config file
fh=logger.createLoggerFile(config)

############

def on_message(client, userdata, message):
#     print("message topic=",message.topic)
    json_string=str(message.payload.decode("utf-8"))
    json_data=json.loads(json_string)
    print("TimeRecording : "+str(json_data["TimeRecording"]))
    print("PositionChange : "+str(json_data["PositionChange"]))
    print("TimeChange : "+str(json_data["TimeChange"]))
    print("IndexTriggered : "+str(json_data["IndexTriggered"]))
    print("----------")
    
    global fh
    fh.write(str(json_data["TimeRecording"]) + ", " + 
             str(json_data["PositionChange"]) + ", " +
             str(json_data["TimeChange"]) + ", " + 
             str(json_data["IndexTriggered"]) + "\n")

########################################
    
broker_address="localhost"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("EncoderLogger") #create new instance
print("setting  password")
client.username_pw_set(username="admin",password="movitplus")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
topic_encoder=config.get('MQTT','topic')
print ("Subscribing to topic",topic_encoder)
client.subscribe(topic_encoder)
#print("Publishing message to topic","house/bulbs/bulb1")
#client.publish("house/bulbs/bulb1","OFF")
time.sleep(10) # wait
client.loop_stop() #stop the loop
