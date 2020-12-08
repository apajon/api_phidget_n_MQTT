# api_phidget_n_MQTT
This project contain src file to receive measures from Phidget22's encoder, send them into a topic of a paho.MQTT server, get back those measures from the paho.MQTT server to save them into a log file and finally plot the measures from the last log.

Made for Python3 but also work in Python2 on raspbian for RaspberryPi 3 or 4 with a virtual Desktop like with VNCserver
____
# Table of content
- [1-Installation procedure](#1-Installation-procedure)
 - [1.1-Get the code](#11-Get-the-code)
 - [1.2-Libraries](#12-Libraries)
   - [1.2.1-Needed Libraries](#121-Needed-Libraries)
   - [1.2.2-Install Libraries](#122-Install-Libraries)
   - [1.2.3 MQTT server installation](#123-MQTT-server-installation)
 - [1.3-Set Desktop scripts](#13-Set-Desktop-scripts)
   - [1.3.1-RUN script](#131-RUN-script)
   - [1.3.2-PLOT script](#132-PLOT-script)
- [2-Code overview](#2-Code-overview)
- [3-Running](#3-Running)
 - [3.1-Get measures](#31-Get-measures)
 - [3.2-Save measures in log file](#32-Save-measures-in-log-file)
 - [3.3-Plot measures in last log file](#33-Plot-measures-in-last-log-file)
 - [3.4-Desktop script](#34-Desktop-script)
____
# 1-Installation procedure
## 1.1-Get the code

To install the software on raspbian virtual Desktop:
- open terminal with **`Ctrl+Alt+T`**
- go in the local folder where you want to install
```bash
cd /PATH
```
>example of PATH **`/home/pi/Documents`**

- clone the repo [**`api_phidget_n_MQTT`**](https://github.com/apajon/api_phidget_n_MQTT)
```bash
git clone --recursive https://github.com/apajon/api_phidget_n_MQTT
cd src/lib_global/
git branch
# verify that main branch is existing
git checkout main
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

## 1.2-Libraries
### 1.2.1-Needed Libraries
- [library phidget installation](####-library-phidget-installation)
- [paho.mqtt.client](####-pahomqttclient-library-in-python)
- [matplotlib installation](####-matplotlib-installation)
- [CSV reader pandas](####-CSV-reader-pandas)

### 1.2.2-Install Libraries
#### library phidget installation
In a terminal go to **`download`** folder and do:
```bash
sudo apt-get install libusb-1.0-0-dev
wget https://www.phidgets.com/downloads/phidget22/libraries/linux/libphidget22.tar.gz
tar -xf libphidget22.tar.gz
```
instruction in README
```bash
./configure
make
sudo make install
sudo cp plat/linux/udev/99-libphidget22.rules /etc/udev/rules.d
```
Then for Python3 :
```bash
pip3 install Phidget22
```
or for Python2 :
```bash
pip2 install Phidget22
```

source web
> https://www.phidgets.com/docs/Language_-_Python_Linux_Terminal#Python%203
https://www.phidgets.com/?view=code_samples&lang=Python

#### paho.mqtt.client library in python
In a terminal run for Python3
```bash
pip3 install paho-mqtt
```
or for Python2
```bash
pip2 install paho-mqtt
```
source web
>http://www.steves-internet-guide.com/into-mqtt-python-client/

#### matplotlib installation
In a terminal run for Python3
```bash
sudo apt update
sudo apt install python3-matplotlib
```
or for Python2
```bash
sudo apt update
sudo apt-get install python-matplotlib
```
source web
>https://matplotlib.org/users/installing.html

#### CSV reader pandas
In a terminal run for Python3
```bash
sudo pip3 install pandas
```
or for Python2
```bash
sudo pip2 install pandas
```
source web
>https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html

### 1.2.3 MQTT server installation
Installation instruction of Mosquitto Server (MQTT) on Raspberry Pi 3 or 4 if not already installed in your system.

Steps to Install and Configure Mosquitto Server on Raspberry Pi 3 or 4 with command lines in a Terminal:

- Step 1: Update the System
```bash
sudo apt-get update
```

- Step 2: Update the System Repositories
```bash
sudo wget http://repo.mosquitto.org/debian/mosq
sudo apt-key add mosquitto-repo.gpg.key
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosq
sudo apt-get update
sudo apt-get install mosquitto
```

- Step 3: Install Three Parts of Mosquitto Proper
```bash
sudo apt-get install mosquitto mosquitto-clients python-mosquitto
```

- Step 4: Stop the Server
```bash
sudo /etc/init.d/mosquitto stop
```

- Step 5: Configuring and Starting the Mosquitto Server
```bash
sudo nano /etc/mosquitto/mosquitto.conf
```

The File Should Look as follows
```
# Place your local configuration in /etc/mosquitto/conf.d/
#
# A full description of the configuration file is at
# /usr/share/doc/mosquitto/examples/mosquitto.conf.example

pid_file /var/run/mosquitto.pid

persistence true
persistence_location /var/lib/mosquitto/

log_dest topic


log_type error
log_type warning
log_type notice
log_type information

connection_messages true
log_timestamp true

include_dir /etc/mosquitto/conf.d
```

- Step 6: Starting the Server
```bash
sudo /etc/init.d/mosquitto start
```

- Step 7: Open Two Terminals using **`Ctrl+Alt+T`**
  - Terminal 1: Type the following:
```bash
mosquitto_sub -d -t hello/world
```
 - Terminal 2: Type the Following:
```bash
mosquitto_pub -d -t hello/world -m "Hello from Terminal window 2!"
```
you can see the message on Terminal 1...

- Step 8 : Set username and password in the Terminal where you installed MQTT server
```bash
sudo mosquitto_passwd -c /etc/mosquitto/passwd $USERNAME
Password: $PASSWORD
```
replace `$USERNAME` and `$PASSWORD` by the wanted username and password.

- Step 9 : Create a configuration file for Mosquitto pointing to the password file we have just created.
```bash
sudo nano /etc/mosquitto/conf.d/default.conf
```
This will open an empty file. Paste the following into it.
```bash
allow_anonymous false
password_file /etc/mosquitto/passwd
```
Save and exit the text editor with `Ctrl+O`, `Enter` and then `Ctrl+X`.
Now restart Mosquitto server and test our changes.
```bash
sudo systemctl restart mosquitto
```
source web
>https://www.youtube.com/watch?v=1CGfGuZqmhc
>
>https://www.vultr.com/docs/how-to-install-mosquitto-mqtt-broker-server-on-ubuntu-16-04

## 1.3-Set Desktop scripts
In test_api_phidget/, there is encoder.desktop you can copy on the desktop and replace the PATH to the python script to run it directly by clicking

!!!Warning!!! use "sudo chmod +x file.py" to give the right to open the file if needed

To set the Desktop script on raspbian virtual Desktop:
- open terminal with **`Ctrl+Alt+T`**
- go in the local folder **`/PATH/api_phidget_n_MQTT`** where you have installed the software
```bash
cd /PATH/api_phidget_n_MQTT
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
- Replace the folder PATH in
```bash
 --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/
```
by the **``PATH/api_phidget_n_MQTT/src``** in your local computer where you cloned the repo
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
- Replace the folder PATH in
```bash
 --working-directory=/home/pi/Documents/api_phidget_n_MQTT/src/
```
by the **``PATH/api_phidget_n_MQTT/src``** in your local computer where you clone the repo
```bash
 --working-directory=PATH/api_phidget_n_MQTT/src
```
- save and close
____
# 2-Code overview
The repo is organised as followed
- **`api_phidget_PLOT.sh`** : script to run simultany `src/phidget22GetMeasures.py` and `src/phidget22SaveLogMeasures.py`, can be put on [Desktop](#131-RUN-script)
- `api_phidget_RUN.sh` : script to run `src/phidget22PlotLastLogMeasures.py`, can be put on [Desktop](#132-PLOT-script)
- `/src` : folder with Python source files
  - `config.cfg` : config file gathering configuration parameters for the whole Python code
  - `config_README.md` : README file about configuration parameters in `config.cfg`
  - `phidget22GetMeasures.py` : code to get measures from the Phidget22 encoder and publish them on a topic of the local paho.MQTT server
  - `phidget22PlotLastLogMeasures.py` : code to plot the measures saved in the last log file
  > WARNING it get the last indented log file beginning by 00 not the last in term of date of recording
  >
  - `phidget22SaveLogMeasures.py` : code to get measures of the Phidget22 encoder published  on a topic of the local paho.MQTT server and save them in a log file
  - `/lib_api_phidget22` : folder with Python homemade library files for phidget22
  - `/lib_global_python.git` : submodule folder with Python homemade library files
____
# 3-Running

- [3.1-Get measures](#31-Get-measures)
- [3.2-Save measures in log file](#32-Save-measures-in-log-file)
- [3.3-Plot measures in last log file](#33-Plot-measures-in-last-log-file)
- [3.4-Desktop script](#34-Desktop-script)
  - [3.4.1-RUN](#341-RUN)
  - [3.4.2-PLOT](#342-PLOT)
- [3.5-GUI](#35-GUI)

## 3.1-Get measures
To get measures from phidget22 encoder connected to the RaspberryPi :
- open terminal with **`Ctrl+Alt+T`**
- go in the local folder where you want to install
```bash
cd /PATH
```
>example of PATH **`/home/pi/Documents`**
>
- go in the **`/src`** folder
```bash
cd /src
```
- launch the python script that get measures from encoder
```bash
python3 phidget22GetMeasures.py
```
- The measures are now published in the internal MQTT server of the raspberry

To stop the Python script you just have to press **`ENTER`** in the terminal.

READ [config_README.md](src/config_README.md) to know where to configure the MQTT topic to publish the measures.

## 3.2-Save measures in log file
When the measures from phidget22 encoder are published on a MQTT server.
You can save those measures into a log file with CSV format:
- open terminal with **`Ctrl+Alt+T`**
- go in the local folder where you want to install
```bash
cd /PATH
```
>example of PATH **`/home/pi/Documents`**
>
- go in the **`/src`** folder
```bash
cd /src
```
- launch the python script that save measures the measures
```bash
python3 phidget22SaveLogMeasures.py
```

To stop the Python script  and end recording measures in the log file you just have to press **`ENTER`** in the terminal.

READ [config_README.md](src/config_README.md) to know where to configure the MQTT topic where to get the the measures from and log file name and folder PATH.

## 3.3-Plot measures in last log file
After saving measures into a log file, you can plot the measures:
- open terminal with **`Ctrl+Alt+T`**
- go in the local folder where you want to install
```bash
cd /PATH
```
>example of PATH **`/home/pi/Documents`**
>
- go in the **`/src`** folder
```bash
cd /src
```
- launch the python script that plot measures
```bash
python3 phidget22PlotLastLogMeasures.py
```
It will open a plot window with the drawn measures.

To stop the Python script close the plot window.

The log file used for plotting measures is located in the chosen folder and is based on the chosen file name.
> WARNING it get the last indented log file beginning by 00 not the last in term of date of recording
>

READ [config_README.md](src/config_README.md) to know where to configure log file name and folder PATH.

## 3.4-Desktop script
### 3.4.1-RUN
On the Desktop `Double-Click` on `api_phidget_RUN.sh` and then `Click` on `Execute in Terminal`. This script will launch two separate terminal with
[3.1-Get measures](#31-Get-measures)
and
[3.2-Save measures in log file](#32-Save-measures-in-log-file).

### 3.4.2-PLOT
On the Desktop `Double-Click` on `api_phidget_RUN.sh` and then `Click` on `Execute in Terminal`. This script will launch terminal and a plot window that does
[3.3-Plot measures in last log file](#33-Plot-measures-in-last-log-file).

## 3.5-GUI
WORK IN PROGRESS
