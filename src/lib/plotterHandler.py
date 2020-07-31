import json

def on_message(client, userdata, message):
#     print("message topic=",message.topic)
    json_string=str(message.payload.decode("utf-8"))
    json_data=json.loads(json_string)
    
    if client.printLog:
        print("TimeRecording : "+str(json_data["TimeRecording"]))
        print("PositionChange : "+str(json_data["PositionChange"]))
        print("TimeChange : "+str(json_data["TimeChange"]))
        print("IndexTriggered : "+str(json_data["IndexTriggered"]))
        print("----------")
    