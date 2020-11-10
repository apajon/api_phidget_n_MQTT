# Script to launch two python3 sofwares in terminal that
# plot the encoder measures saved in the last log file

#plot last encoder log file
lxterminal -t "Plot last Phidget22 recorded logger" --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/ -e ./phidget22PlotLastLogMeasures.py
