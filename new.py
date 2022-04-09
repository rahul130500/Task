import cv2
import numpy as np
import glob

counter = 0
video_list = []
for name in glob.glob(r'/home/rahul/Desktop/mywork/Images/*'):
    val = name
    video_list.append(val)
while(True):
    cap = cv2.imread(video_list[counter])
    cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)          
    cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, 1)
    cv2.imshow('Frame', cap)
    cv2.waitKey(5000)
    if counter == len(video_list)-1:
        counter = 0
    else:
        counter = counter + 1