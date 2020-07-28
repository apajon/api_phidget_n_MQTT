import time
import json

############
#intialize timer
t0 = time.time()

############
#Declare any event handlers here. These will be called every time the associated event occurs.

def onAttach(self):
    print("Attach!")

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
