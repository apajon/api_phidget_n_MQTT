import time

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
    print("TimeRecording: " + str(t1))

    #print datas from encoder
    print("PositionChange: " + str(positionChange))
    print("TimeChange: " + str(timeChange))
    print("IndexTriggered: " + str(indexTriggered))
    print("----------")

    #write datas from encoder in a logger file fh
    global fh
    fh.write(str(t1) + "," + str(positionChange) + ", " + str(timeChange) + ", " + str(indexTriggered) + "\n")

    #publish datas from encoder in topic
    data = {
        "TimeRecording": t1,
        "PositionChange": positionChange,
        "IndexTriggered" : timeChange
    }
    json_string = json.dumps(data)
    print json_string
    global client
    client.publish("toto/toto",json_string)
