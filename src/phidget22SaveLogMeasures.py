#!/usr/bin/env python3

import sys
if sys.version_info.major==2:
    import ConfigParser #Python 2
if sys.version_info.major==3:
    import configparser as ConfigParser #Python 3
if sys.version_info.major!=2 and sys.version_info.major!=3:
    print("bad python version")
    sys.exit()

from lib import createLoggerFile as logger
from lib import MQTT_client
from lib import loggerHandler

############
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
    client=MQTT_client.createClient("LoggerEncoder",config)
    
    #Set addressing parameters to specify
    client.fh=fh
    client.printLog=config.getboolean('Logger','printLog')

    #attach function to callback
    client.on_message=loggerHandler.on_message
    
    #start the loop
    client.loop_start() 
    
    #subscribe topic
    topic_encoder=config.get('MQTT','topic')
    print ("Subscribing to topic",topic_encoder)
    client.subscribe(topic_encoder)

    #Interupt script by pressing Enter
    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
        print("Logger encoder stopped !")
    finally:
        #stop the loop
        client.loop_stop()

main()