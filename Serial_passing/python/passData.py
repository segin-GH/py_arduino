import time
import serial

arduinoData = serial.Serial('/dev/ttyACM0',1150200)
time.sleep(1)

while True:
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline()
    print(dataPacket)

