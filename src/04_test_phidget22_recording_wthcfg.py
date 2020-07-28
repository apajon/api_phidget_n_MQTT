#!/usr/bin/env python

from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.Encoder import *
import traceback
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

############
#intialize timer
t0 = time.time()

############
#import config file
config = ConfigParser.ConfigParser()

config.read('config.cfg')

############
#filename from config file
filename = config.get('filenameLogger','folderPATH')+config.get('filenameLogger','filename')

# create indented filename
i = 0
while os.path.exists(filename+"%s.txt" % format(i, '02d')):
    i += 1
filename=filename+"%s.txt" % format(i, '02d')

#create repository if not exist
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise 

#create recording file
fh = open(filename, "w")
fh.write("TimeRecording, PositionChange, TimeChange, IndexTriggered \n")

############
#Declare any event handlers here. These will be called every time the associated event occurs.

def onPositionChange(self, positionChange, timeChange, indexTriggered):
    t1=time.time()-t0
    print("TimeRecording: " + str(t1))
    
    print("PositionChange: " + str(positionChange))
    print("TimeChange: " + str(timeChange))
    print("IndexTriggered: " + str(indexTriggered))
    print("----------")

    global fh
    fh.write(str(t1) + "," + str(positionChange) + ", " + str(timeChange) + ", " + str(indexTriggered) + "\n")

def onAttach(self):
    print("Attach!")

def onDetach(self):
    print("Detach!")

############
def main(config_):
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
