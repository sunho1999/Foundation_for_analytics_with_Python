import cv2
import numpy as np
#cv2.createTrackbar(track_bar_name,window_name,value,count,on_change)Tracker를 생성하는 함수
"""
-value: 초기값
-count: Max값(Min:0)
-on_change:값이 변경될 때 호출되는 Callback 함수
"""

def change_color(x):
    r = cv2.getTrackbarPos("R","Image")
    g = cv2.getTrackbarPos("G","Image")
    b = cv2.getTrackbarPos("B","Image")
    image[:] = [b,g,r]
    cv2.imshow("Image",image)
image = np.zeros((600,400,3),np.uint8)
cv2.namedWindow("Image")

cv2.createTrackbar("R","Image",0,255,change_color)
cv2.createTrackbar("G","Image",0,255,change_color)
cv2.createTrackbar("B","Image",0,255,change_color)

cv2.imshow("Image",image)
cv2.waitKey(0)