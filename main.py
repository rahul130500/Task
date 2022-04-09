import cv2
import numpy as np
import glob

counter = 0
video_list = []
for name in glob.glob(r'/home/rahul/Desktop/mywork/Videos/*'):
    val = name
    video_list.append(val)
while(True):
    cap = cv2.VideoCapture(video_list[counter])
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
    if counter == len(video_list)-1:
        counter = 0
    else:
        counter = counter + 1