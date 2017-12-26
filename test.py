#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import smbus
import time

# 打开 /dev/i2c-1
bus = smbus.SMBus(1)
 
while True:
  for i in range(0,4):
	# 向PCF8574写入一个字节
	bus.write_byte( 0x20 , (1<<i) )
	# 延时100ms
	time.sleep(0.1)