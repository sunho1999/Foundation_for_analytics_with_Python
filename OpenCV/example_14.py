import cv2

#cv2.boundingRect(contour) Contour를 포함하는 사각형을 그림
"""
-사각형의 X,Y좌표와 너비,높이를 반환함
"""

image = cv2.imread('digit_image.png')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,230,255,0)
thresh = cv2.bitwise_not(thresh) #색 반전
cv2.imshow('Image',thresh)
cv2.waitKey(0)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image,contours,0,(0,0,255),4) #외각 전부다 표시 -1
cv2.imshow('Image',image)
cv2.waitKey(0)

#첫번째 컨투어
contour = contours[0]
x,y,w,h = cv2.boundingRect(contour)
image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
cv2.imshow('Image',image)
cv2.waitKey(0)