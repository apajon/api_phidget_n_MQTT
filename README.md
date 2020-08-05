# api_phidget_n_MQTT

<library phidget installation>
sudo apt-get install libusb-1.0-0-dev
wget https://www.phidgets.com/downloads/phidget22/libraries/linux/libphidget22.tar.gz
tar -xf libphidget22.tar.gz
instruction in README
./configure
make
sudo make install
sudo cp plat/linux/udev/99-libphidget22.rules /etc/udev/rules.d
installation python : 	'pip3 install Phidget22'
			or
			'pip install Phidget22'
<source web>
https://www.phidgets.com/docs/Language_-_Python_Linux_Terminal#Python%203
https://www.phidgets.com/?view=code_samples&lang=Python

In test_api_phidget/, there is encoder.desktop you can copy on the desktop and replace the PATH to the python script to run it directly by clicking
!!!Warning!!! use "sudo chmod +x file.py" to give the right to open the file

<paho.mqtt.client library in python>
installation : 	'pip install paho-mqtt'
		or
		'pip3 install paho-mqtt'
<source web>
http://www.steves-internet-guide.com/into-mqtt-python-client/

<matplotlib installation>
sudo apt update
sudo apt install python3-matplotlib
sudo apt-get install python-matplotlib

