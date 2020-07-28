import paho.mqtt.client as mqtt #import the client1
import json
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
#     print("message qos=",message.qos)
#     print("message retain flag=",message.retain)
    json_string=str(message.payload.decode("utf-8"))
    json_data=json.loads(json_string)
    print(json_data)
    print(json_data["president"]["name"])
########################################
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "answer" : [1,2,3]
    }
}
json_string = json.dumps(data)

broker_address="localhost"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
print("setting  password")
client.username_pw_set(username="admin",password="movitplus")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")
client.publish("house/bulbs/bulb1",json_string)
time.sleep(4) # wait
client.loop_stop() #stop the loop
