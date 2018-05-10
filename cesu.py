#!/usr/bin/python
import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BOARD) #将GPIO引脚设置为BOARD模式
GPIO.setmode(GPIO.BCM)   #将GPIO引脚设置为BCM引脚方式
GPIO.setup(11,GPIO.IN)  #设置GPIO引脚通道 作为输入
#GPIO.setup(13,GPIO.IN) #作为输出

GPIO.add_event_detect(channel, GPIO.RISING)  

def run():
	while(1):
		if GPIO.event_detected(channel):
			print('Button pressed')
	return
	
thread = threading.Thread(target=run)
thread.start()

