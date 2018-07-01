import numpy as np
import cv2

def myfunc(i):
    pass # do nothing
    

cv2.namedWindow('title') # create win with win name
cv2.createTrackbar('threshold1', # name of value
                   'title', # win name
                   0, # min
                   120, # max
                   myfunc) # callback func

cv2.createTrackbar('threshold2', # name of value
                   'title', # win name
                   120, # min
                   255, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue

    v1 = cv2.getTrackbarPos('threshold1',  # get the value
                           'title')  # of the win
    
    v2 = cv2.getTrackbarPos('threshold2',  # get the value
                           'title')  # of the win

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, v1, v2) 
    cv2.imshow('title', edge)
        

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()