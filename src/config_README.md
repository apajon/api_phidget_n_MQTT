# config_README

____
# SECTIONS
- [[filenameLogger]](#filenameLogger)
- [[encoder]](#encoder)
- [[Logger]](#Logger)
- [[MQTT]](#MQTT)

____
## [filenameLogger]
Section to set config parameters of the Log file used by [phidget22SaveLogMeasures](phidget22SaveLogMeasures.py)

### filename
```bash
filename=$FILENAME
```
Variable to set the file name in which to record the datas. Replace `$FILENAME` with the desired file name. The log file will be named as `$FILENAME#.txt` where # is incremented starting from 00
>example of filename **`Logger_encoder_2p_v3_`**
>
>File names will be : `Logger_encoder_2p_v3_00.txt`, `Logger_encoder_2p_v3_01.txt`, `...`
>

### folderPATH
```bash
folderPATH=$FOLDERPATH
```
Variable to set the root folder path where to save the log file.
Replace `$FOLDERPATH` with the chosen folder.
- If no folder already exists, it will be created.
- use `./` to record in the same folder as the python script
>example of folder path `./20201026_test/`
>
>example of full folder path `home/pi/Document/api_phidget_n_MQTT/src/20201026_test`

### firstLine
```bash
firstLine=TimeRecording, PositionChange, TimeChange, IndexTriggered
```
Variable to set the first line in the logger file, represent each column name in CSV format.
>WARNING : Don't change it unless you know what you do !!!

____
## [encoder]
Section to set the config parameters of phidget22 encoder used in [phidget22GetMeasures](phidget22GetMeasures.py)
### dataInterval
```bash
dataInterval=100
```
Variable in `ms`to set the data interval of the encoder to send measures.
> choose from 8ms to 1000ms

### printLog
```bash
printLog=True
```
BOOL variable to choose to print with `True` or not with `False` the encoder measured values in the terminal by [phidget22GetMeasures](phidget22GetMeasures.py)

### resolution
```bash
resolution=0.02
```
Pidget22 encoder resolution in `mm/pulse`

____
## [Logger]
[phidget22SaveLogMeasures](phidget22SaveLogMeasures.py)

### printLog
```bash
printLog=True
```
BOOL variable to choose to print with `True` or not with `False` the encoder measured values from the MQTT in the terminal by [phidget22SaveLogMeasures](phidget22SaveLogMeasures.py)

____
## [MQTT]
Config parameters of the MQTT server and topic in the MQTT server to publish and subscribe

### broker_address
```bash
broker_address=localhost
```
MQTT server/broker address
- use `localhost` when in local on the same machine as the server MQTT
- use Raspberry IP adress like `192.168.1.10` to access the remote MQTT server on local Network
- use web adresse like `https://monserverMQTT.com` to access the remote MQTT server on Internet


### username and password
```bash
usr=admin
pswd=movitplus
```
login and password of the MQTT server.


### topic publish
```bash
topic_publish=encoder/log
```
topic in the MQTT server to publish on the measures


### topic subscribe
```bash
topic_subscribe=encoder/log
```
topic in the MQTT server to subscribe on to get the measures
