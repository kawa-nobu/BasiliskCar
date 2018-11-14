# coding:utf-8
import RPi.GPIO as GPIO
import time
import struct
import pygame.mixer

device_path = "/dev/input/js0"
EVENT_FORMAT = "LhBB";
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)
#GPIO.setmode( GPIO.BOARD)
#GPIO.setup( 7, GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)#LED
##############################################
GPIO.setup(13, GPIO.OUT)#Ue_1CH.OUT1,2
GPIO.setup(19, GPIO.OUT)#Ue_1CH.OUT3,4
GPIO.setup(26, GPIO.OUT)#Ue_2CH.OUT1,2
GPIO.setup(20, GPIO.OUT)#Ue_2CH.OUT3,4
##############################################
GPIO.setup(17, GPIO.OUT)#Shita_1CH.OUT1,2_2
GPIO.setup(22, GPIO.OUT)#Shita_1CH.OUT1,2
GPIO.setup(23, GPIO.OUT)#Shita_2CH.OUT3,4_2
GPIO.setup(24, GPIO.OUT)#Shita_2CH.OUT3,4
##############################################
GPIO.setup(16, GPIO.OUT)#Reray
GPIO.setup(21, GPIO.OUT)#playled
print('開始')
pygame.mixer.init()
pygame.mixer.music.load("startup.mp3")
pygame.mixer.music.play()
s = 0
GPIO.output(25, True)
try:
  with open(device_path, "rb") as device:
    event = device.read(EVENT_SIZE)
    while event:
      (ds3_time, ds3_val, ds3_type, ds3_num) = struct.unpack(EVENT_FORMAT, event)
      if ds3_type == 1:
        if ds3_num == 13:
          sw = False if ds3_val == 0 else True
          GPIO.output(21,sw)
          GPIO.output(13, sw)
          print('LEDオン')
        if ds3_num == 3:
          GPIO.output(21, True)
          time.sleep(0.1)
          GPIO.output(21, False)
          time.sleep(0.35)
          pygame.mixer.init()
          pygame.mixer.music.load("basilisc.mp3")
          pygame.mixer.music.play(-1)
          print('バジリスクタイム!')
        if ds3_num == 0:
          GPIO.output(21, True)
          time.sleep(0.1)
          GPIO.output(21, False)
          time.sleep(0.35)
          pygame.mixer.init()
          pygame.mixer.music.stop()
          print('バジリスクタイム終了')
        if ds3_num == 4:
          time.sleep(0.35)
          pygame.mixer.init()
          pygame.mixer.music.set_volume(1)
          print('ボリュームアップ')
        if ds3_num == 6:
          time.sleep(0.35)
          pygame.mixer.init()
          pygame.mixer.music.set_volume(0.5)
          print('ボリュームダウン')
        if ds3_num == 16:
          time.sleep(0.2)
          print('LOGO!')
          GPIO.output(16, True)
          time.sleep(0.50)
          GPIO.output(16, False)
          count = 0
        if ds3_num == 5:
          time.sleep(0.4)
          print('on')  
          s = s+1
        if(s>5):
          s = 0
          pygame.mixer.init()
          print('ELECTRICAL COMMUNICATION')
          pygame.mixer.music.load("elect.mp3")
          pygame.mixer.music.play()
          time.sleep(14)
          GPIO.output(22, True)
          time.sleep(1)
          GPIO.output(22, False)
          time.sleep(0.5)
          GPIO.output(17, True)
          time.sleep(1)
          GPIO.output(17, False)
          count = 0
         
         #MortorDriver Switch
      if ds3_type == 2:
        if ds3_num == 19:
          #time.sleep(0.5)
          print('Go')
          sw = False if ds3_val == 0 else True
          GPIO.output(22, sw)
          GPIO.output(24, sw)
          GPIO.output(26, sw)
          GPIO.output(20, sw)
        if ds3_num == 16:
          #time.sleep(0.5)
          print('back')
          sw = False if ds3_val == 0 else True
          GPIO.output(17, sw)
          GPIO.output(23, sw)
          GPIO.output(13, sw)
          GPIO.output(19, sw)
        if ds3_num == 15:
          #time.sleep(0.5)
          print('right rol')
          sw = False if ds3_val == 0 else True
          GPIO.output(22, sw)
          GPIO.output(23, sw)
          GPIO.output(26, sw)
          GPIO.output(19, sw)
        if ds3_num == 14:
          #time.sleep(0.5)
          print('left rol')
          sw = False if ds3_val == 0 else True
          GPIO.output(17, sw)
          GPIO.output(24, sw)
          GPIO.output(13, sw)
          GPIO.output(20, sw)
        if ds3_num == 1:
          #time.sleep(0.5)
          print('right')
        if ds3_num == 2:
          #time.sleep(0.35)
          print('left')


      # print( "{0}, {1}, {2}, {3}".format( ds3_time, ds3_val, ds3_type, ds3_num ) )
      event = device.read(EVENT_SIZE)
finally:
  GPIO.cleanup()