# api_phidget_n_MQTT
This project contain src file to receive measures from Phidget22's encoder, send them into a topic of a paho.MQTT server, get back those measures from the paho.MQTT server to save them into a log file and finally plot the measures from the last log.

Made for Python3 but also work in Python2 on raspbian for RaspberryPi 3 or 4 with a virtual Desktop like with VNCserver
____
# Table of content
- [1-Installation procedure](#1-Installation-procedure)
 - [1.1-Get the files](#11-Get-the-files)
 - [1.2-Install libraries](#12-Install-libraries)
 - [1.3-Set Desktop scripts](#13-Set-Desktop-scripts)
   - [1.3.1-RUN script](#131-RUN-script)
   - [1.3.2-PLOT script](#132-PLOT-script)

____
# 1-Installation procedure
## 1.1-Get the files

To install the software on raspbian virtual Desktop:
- open terminal with **`Ctrl+Alt+T`**
- go in the local folder where you want to install
```bash
cd /PATH
```
>example of PATH **`/home/pi/Documents`**

- clone the repo [**`api_phidget_n_MQTT`**](https://github.com/apajon/api_phidget_n_MQTT)
```bash
git clone https://github.com/apajon/api_phidget_n_MQTT
```
or download it as a .zip file and then extract it
```bash
wget https://github.com/apajon/api_phidget_n_MQTT/archive/master.zip
unzip api_phidget_n_MQTT-master.zip
mv api_phidget_n_MQTT-master api_phidget_n_MQTT
```
Whatever the method, you now have a folder named **`api_phidget_n_MQTT`** in the chosen folder at **`/PATH`**
- install the required [libraries](#intall-libraries)

- *-OPTION-* put [script file](#13-Set-Desktop-scripts) on the desktop

## 1.2-Install libraries

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

<CSV reader pandas>
sudo pip3 install pandas

## 1.3-Set Desktop scripts
To install the software on raspbian virtual Desktop:
- open terminal with **`Ctrl+Alt+T`**
- go in the local folder **`/PATH`** where you have installed the software
```bash
cd /PATH/
```
### 1.3.1-RUN script
- copy the file **`api_phidget_RUN.sh`** on the desktop

- open with a text editor **`api_phidget_RUN.sh`**

- find the lines
```bash
lxterminal -t "Run Phidget22 encoder reading script" --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/ -e ./phidget22GetMeasures.py
```
and
```bash
lxterminal -t "Run encoder recording script" --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/ -e ./phidget22SaveLogMeasures.py
```
- Replace the folder PATH
```bash
 --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/
```
by the **``PATH/api_phidget_n_MQTT/src``** in your local computer where you clone the repo
```bash
 --working-directory=PATH/api_phidget_n_MQTT/src
```
- Save and close

### 1.3.2-PLOT script
- copy the file **`api_phidget_PLOT.sh`** on the desktop
- open with a text editor **`api_phidget_PLOT.sh`**
- find the line
```bash
lxterminal -t "Plot last Phidget22 recorded logger" --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/ -e ./phidget22PlotLastLogMeasures.py
```
- Replace the folder PATH
```bash
 --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/
```
by the **``PATH/api_phidget_n_MQTT/src``** in your local computer where you clone the repo
```bash
 --working-directory=PATH/api_phidget_n_MQTT/src
```
- save and close
