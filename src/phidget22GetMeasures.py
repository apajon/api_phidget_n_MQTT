#!/usr/bin/env python3

from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.Encoder import *
import traceback

import asyncio

# for Python 2/3 compatibility
try:
    import ConfigParser #Python 2
except ImportError:
    import configparser as ConfigParser #Python 3

from lib_api_phidget22 import phidget22Handler as handler
from lib_global_python import MQTT_client

############
def main():

    ############
    #import config file
    config = ConfigParser.ConfigParser()

    print("opening configuration file : config.cfg")
    config.read('config.cfg')

    # print("opening configuration file : config.json")
    # async with open('config.cfg','r') as configfile:
    #     await config.read(configfile)

    ############
    #connect to mqtt broker
    client=MQTT_client.createClient("Encoder",config)

    ############
    #connection to Phidget encoder and wait for measures
    #publish the datas on config/MQTT/topic
    try:
        Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
        #Create your Phidget channels
        encoder0 = Encoder()

        #Set addressing parameters to specify
        encoder0.client=client
        encoder0.clientTopic=config.get('MQTT','topic')
        encoder0.printLog=config.getboolean('encoder','printLog')
        encoder0.chooseDataInterval=config.getint('encoder','dataInterval')

        #Assign any event handlers you need before calling open so that no events are missed.
        encoder0.setOnPositionChangeHandler(handler.onPositionChange)
        encoder0.setOnAttachHandler(handler.onAttach)
        encoder0.setOnDetachHandler(handler.onDetach)

        #Open your Phidgets and wait for attachment
        encoder0.openWaitForAttachment(5000)

        #Do stuff with your Phidgets here or in your event handlers.

        #Change the data interval from the encoder based on config datas
#         encoder0.setDataInterval(config.getint('encoder','dataInterval'))

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
main()
