import serial

arduinoData = serial.Serial('com3',115200)

while True:

    cmd = input('enter your number : ')
    cmd = cmd + '\r'
    arduinoData.write(cmd.encode())