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
#send the FREQ Command; the format is as follows: FREQ\0XXXXXXXX\n where XXXXXXXX is the desired frequency in mHz
ser.write(b"FREQ\0"+b"00000100\n")
time.sleep(1)
pass