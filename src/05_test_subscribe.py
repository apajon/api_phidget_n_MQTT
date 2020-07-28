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
from lib import MQTT_client

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

def main():
    ############
    #import config file
    config = ConfigParser.ConfigParser()
    
    print("opening configuration file : config.cfg")
    config.read('config.cfg')

    ############
    #filename from config file
    fh=logger.createLoggerFile(config)
    
    ############
    #connect to mqtt broker
    client=MQTT_client.createClient("Encoder",config)

    client.loop_start() #start the loop
    topic_encoder=config.get('MQTT','topic')
    print ("Subscribing to topic",topic_encoder)
    client.subscribe(topic_encoder)

    #Interupt script by pressing Enter
    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
        pass

    client.loop_stop() #stop the loop

main()