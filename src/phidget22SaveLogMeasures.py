#!/usr/bin/env python3

# for Python 2/3 compatibility
try:
    import ConfigParser #Python 2
except ImportError:
    import configparser as ConfigParser #Python 3

from lib_global_python import createLoggerFile as logger
from lib_global_python import MQTT_client
from lib_global_python import loggerHandler

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
    topic_encoder=config.get('MQTT','topic_subscribe')
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
