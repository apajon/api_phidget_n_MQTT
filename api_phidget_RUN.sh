# just for test and show case

echo "current tmux sessions"
lxterminal -t "Run Phidget22 encoder reading script" --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/ -e ./05_test_phidget22_recording_wthplt.py 

echo "toto"
lxterminal -t "Run encoder recording script" --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/ -e ./05_test_subscribe.py
