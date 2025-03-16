import serial
import time

ser=serial.Serial()
ser.port="/dev/ttyUSB0"
ser.baudrate=115200
ser.open()

#every command consists of 4 characters followed by the '\n' character

#send the START command
ser.write(b"STRT\n")
time.sleep(5)
#send the STOP command
ser.write(b"STOP\n")
time.sleep(5)
#send the STOP command
ser.write(b"STRT\n")
time.sleep(5)
#send the FREQ Command; the format is as follows: FREQ\0XXXXXXXX\n where XXXXXXXX is the desired frequency in mHz
des_freq=1.12e3
des_counter=lambda des_freq : int(32e6/(2*des_freq))
ser.write(b"CNTR\0"+bytes("%08d"%des_counter(1.12e3),"ascii")+b"\n")
time.sleep(5)
pass