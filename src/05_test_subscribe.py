import paho.mqtt.client as mqtt #import the client1
import json
import time
import os
# 
# import sys
# if sys.version_info.major==2:
#     import ConfigParser #Python 2
# if sys.version_info.major==3:
#     import configparser #Python 3
# if sys.version_info.major!=2 and sys.version_info.major!=3:
#     print("bad python version")
#     sys.exit()
# 
# ############
# #intialize timer
# t0 = time.time()
# 
# ############
# #import config file
# config = ConfigParser.ConfigParser()
# 
# config.read('config.cfg')
# 
# ############
# #filename from config file
# filename = config.get('filenameLogger','folderPATH')+config.get('filenameLogger','filename')
# 
# # create indented filename
# i = 0
# while os.path.exists(filename+"%s.txt" % format(i, '02d')):
#     i += 1
# filename=filename+"%s.txt" % format(i, '02d')
# 
# #create repository if not exist
# if not os.path.exists(os.path.dirname(filename)):
#     try:
#         os.makedirs(os.path.dirname(filename))
#     except OSError as exc: # Guard against race condition
#         if exc.errno != errno.EEXIST:
#             raise 
# 
# #create recording file
# fh = open(filename, "w")
# fh.write("TimeRecording, PositionChange, TimeChange, IndexTriggered \n")

############

def on_message(client, userdata, message):
    print("message topic=",message.topic)
    json_string=str(message.payload.decode("utf-8"))
    json_data=json.loads(json_string)
    print("TimeRecording",json_data["TimeRecording"])
    
#     global fh
#     fh.write(str(json_data["time"]) + ", " + str(json_data["Angle"]["mIMUAngle"]) + ", " + str(json_data["Angle"]["fIMUAngle"]) + ", " + str(json_data["Angle"]["seatAngle"]) + "\n")
    
########################################
    
broker_address="localhost"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P2") #create new instance
print("setting  password")
client.username_pw_set(username="admin",password="movitplus")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
topic_test="toto/toto"
print ("Subscribing to topic",topic_test)
client.subscribe(topic_test)
#print("Publishing message to topic","house/bulbs/bulb1")
#client.publish("house/bulbs/bulb1","OFF")
time.sleep(10) # wait
client.loop_stop() #stop the loop
