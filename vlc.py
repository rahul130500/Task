import cv2
import numpy as np
import glob

cap = cv2.VideoCapture('sample.mp4')
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)          
        cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, 1)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
	        break
    else:
	    break
cap.release()

cv2.destroyAllWindows()