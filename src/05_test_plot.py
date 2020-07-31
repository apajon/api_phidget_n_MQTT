#!/usr/bin/env python

import sys
if sys.version_info.major==2:
    import ConfigParser #Python 2
if sys.version_info.major==3:
    import configparser #Python 3
if sys.version_info.major!=2 and sys.version_info.major!=3:
    print("bad python version")
    sys.exit()

import numpy as np
import matplotlib.pyplot as plt

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
    #connect to mqtt broker
    client=MQTT_client.createClient("PlotterEncoder",config)
    
    #Set addressing parameters to specify
#     client.printLog=config.getboolean('Logger','printLog')

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
        
    ############
    plt.axis([0, 10, 0, 1])

    for i in range(10):
        y = np.random.random()
        plt.scatter(i, y)
        plt.pause(0.05)

    plt.show()

main()