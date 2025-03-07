import serial
import time

ser=serial.Serial()
ser.port="/dev/ttyACM0"
ser.baudrate=115200
ser.open()

#every command consists of 4 characters followed by the '\n' character

#send the START command
ser.write(b"STRT\n")
time.sleep(1)
#send the STOP command
ser.write(b"STOP\n")
time.sleep(1)

pass