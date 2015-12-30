#!/usr/bin/python

import numpy as np
import cv2

camara = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = camara.read()
	# Display the resulting frame
	cv2.imshow('frame',frame)

	key = cv2.waitKey(1) & 0xFF;
	if key == ord('g'):
		print 'Has pulsado g'
		while (True):
			# Our operations on the frame come here
			ret, frame = camara.read()
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			cv2.imshow('frame', gray)
			# Press 'b' back to the original video
			if cv2.waitKey(1) & 0xFF == ord('b'):
				break

	if key == ord('t'):
		print 'Has pulsado t'
		while (True):
			ret, frame = camara.read()
			ret, thresh1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
			cv2.imshow('frame', thresh1)
			if cv2.waitKey(1) & 0xFF == ord('b'):
				break
	
	if key == ord('a'):
		print 'Has pulsado a'
		break
