# Script to launch two python3 sofwares in terminal that
#- connect to a phidget22 encoder and publish the measures on a paho.MQTT server
#- get the measures from the paho.MQTT to save them into a CSV log file

# get and publish measure from encoder
lxterminal -t "Run Phidget22 encoder reading script" --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/ -e ./phidget22GetMeasures.py

# save measures from paho.MQTT server
lxterminal -t "Run encoder recording script" --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/ -e ./phidget22SaveLogMeasures.py
