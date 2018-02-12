#
#pill box server: get info and send order to pill box
#
# pip install playsound
from playsound import playsound
from socket import *
import os
import sys
import time
import datetime
import thread
import pygame

global eat
global eaten

def check():
	while True:
		time.sleep(10)
		now = datetime.datetime.now()
		nowtime = str(now.hour) + ':' + str(now.minute)
		nowtime = nowtime.encode('ascii')
		global eat
		global eaten
		if nowtime == eat and eaten == 0:
			print 'eat!', eat
			pygame.init()
			pygame.mixer.music.load("Cali.mp3")
			pygame.mixer.music.play()
			time.sleep(60)
		print nowtime, len(nowtime), eat

def pillboxserver():
	global eat
	HOST = ''
	PORT = 21567
	BUFSIZ = 1024
	ADDR = (HOST,PORT)
	print time.ctime()
	tcpSerSock = socket(AF_INET, SOCK_STREAM)
	tcpSerSock.bind(ADDR)
	tcpSerSock.listen(5)
	while True:
		print 'waiting for connection...'
		tcpCliSock,addr = tcpSerSock.accept()
		print '...connected from: ',addr

		while True:
		    data = tcpCliSock.recv(BUFSIZ)
		    if not data:
		        break
		    #print "="*20
		    print "[From Client]:",data
		    eat = str(data).encode('ascii')
		    global eaten
		    eaten = 0
		    print eat, len(eat)
		    #message = raw_input("Service>")
		    #tcpCliSock.send(message)
	tcpSerSock.close()

#import RPi.GPIO as GPIO

def boxstatus():
	#GPIO.setmode(GPIO.BCM)
	#GPIO.setup(4, GPIO.IN)
	prev = 0
	global eaten
	while(True):
		input_val = 0 #GPIO.input(4)
		time.sleep(.200)
		if input_val == 0 and input_val != prev:
			print 'close'
		if input_val == 1 and input_val != prev:
			print 'open'
			eaten = 1
		prev = input_val

	
eat = ''
thread.start_new_thread (check, ())
thread.start_new_thread (pillboxserver, ())
boxstatus()
    
    
    
    
    
    
    
    
    
    
    
    
