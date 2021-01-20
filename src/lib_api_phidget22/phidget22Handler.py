from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.Encoder import *
import traceback

import time
import json
import warnings

from ..lib_global_python import MQTT_client


############
class encoderWthHandler(Encoder):
    def __init__(self):
        super().__init__()

        self.t0 = time.time()
        self.t1 = time.time()-self.t0

        self.positionChange = 0
        self.timeChange = 0
        self.indexTriggered = 0

        self.printLog=False
        self.chooseDataInterval=None
        self.isConnected = False
        self.timeWaitForAttachment=5000


        # Assign any event handlers you need before calling open so that no events are missed.
        self.setHandlers()

    def setHandlers(self):
        # Assign any event handlers you need before calling open so that no events are missed.
        self.setOnPositionChangeHandler(self.onPositionChange)
        self.setOnAttachHandler(self.onAttach)
        self.setOnDetachHandler(self.onDetach)

    def setParameters(self,config):
        try:
            # Set addressing parameters to specify
            self.printLog = config.getboolean('encoder', 'printLog')
            self.chooseDataInterval = config.getint('encoder', 'dataInterval')
        except:
            pass

    def onAttach(self):
        print("Attach!")
        
        if self.chooseDataInterval:
            print("set DataInterval as "+str(self.chooseDataInterval)+"ms")
            self.setDataInterval(self.chooseDataInterval)

    def onDetach(self):
        print("Detach!")

    def onPositionChange(self, positionChange, timeChange, indexTriggered):
        #compute duration since the begining ot the script
        self.t1=time.time()-self.t0
        self.positionChange = positionChange
        self.timeChange = timeChange
        self.indexTriggered = indexTriggered
        
        # log results
        if self.printLog:
            #print time duration
            print("TimeRecording: " + str(self.t1))

            #print datas from encoder
            print("PositionChange: " + str(self.positionChange))
            print("TimeChange: " + str(self.timeChange))
            print("IndexTriggered: " + str(self.indexTriggered))
            
            print("----------")

    def setTimeWaitForAttachment(self,value):
        if isinstance(value, int):
            self.timeWaitForAttachment=value
        else:
            print("WARNING : value must be an integer !!!")

    def ConnectToEnco(self, config):
        ############
        # connection to Phidget encoder and wait for measures
        # publish the datas on config/MQTT/topic
        try:
            Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
            # Create your Phidget channels
            # Set addressing parameters to specify
            self.setParameters(config)

            # Open your Phidgets and wait for attachment
            self.openWaitForAttachment(self.timeWaitForAttachment)
            self.isConnected = True
        except PhidgetException as ex:
            self.isConnected = False
            # We will catch Phidget Exceptions here, and print the error informaiton.
            traceback.print_exc()
            print("")
            print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)

    def DisconnectEnco(self):
        self.close()

class encoderWthMQTT(encoderWthHandler):
    def __init__(self,config):
        super().__init__()
        self.clientTopic=None
        try:
            self.clientEncoder = MQTT_client.createClient("Encoder", config)
        except:
            self.clientEncoder = None

    def ConnectToEnco(self, config):
        if self.clientEncoder:
            self.clientTopic = config.get('encoder', 'topic_publish')
        else:
            self.clientTopic=None
        super().ConnectToEnco(config)

    def DisconnectEnco(self):
        super().DisconnectEnco()
        try:
            self.clientEncoder.loop_stop()
        except:
            pass

    def onPositionChange(self, positionChange, timeChange, indexTriggered):
        super().onPositionChange(positionChange, timeChange, indexTriggered)

        if self.clientTopic:
            # publish datas from encoder in topic
            data = {
                "TimeRecording": self.t1,
                "PositionChange": self.positionChange,
                "TimeChange": self.timeChange,
                "IndexTriggered" : self.indexTriggered
            }
            # json_string = json.dumps(data)
            # print json_string
            #publish 'data' in topic as a JSON string
            self.clientEncoder.publish(self.clientTopic,json.dumps(data))

############
#intialize timer
t0 = time.time()

############
#Declare any event handlers here. These will be called every time the associated event occurs.

def onAttach(self):
    print("Attach!")
    
    print("set DataInterval as "+str(self.chooseDataInterval)+"ms")
    self.setDataInterval(self.chooseDataInterval)

def onDetach(self):
    print("Detach!")

def onPositionChange(self, positionChange, timeChange, indexTriggered):
    #compute duration since the begining ot the script
    t1=time.time()-t0
    
    #log results
    if self.printLog:
        #print time duration
        print("TimeRecording: " + str(t1))

        #print datas from encoder
        print("PositionChange: " + str(positionChange))
        print("TimeChange: " + str(timeChange))
        print("IndexTriggered: " + str(indexTriggered))
        
        print("----------")

    #publish datas from encoder in topic
    data = {
        "TimeRecording": t1,
        "PositionChange": positionChange,
        "TimeChange": timeChange,
        "IndexTriggered" : indexTriggered
    }
#     json_string = json.dumps(data)
#     print json_string
    #publish 'data' in topic as a JSON string
    self.client.publish(self.clientTopic,json.dumps(data))
