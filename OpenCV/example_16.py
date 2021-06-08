import cv2

#cv2.approxPolyDP(curve,epsilon,closed)근사치 Contour를 구함
"""
-curve: Contour
-epsilon: 최대 거리(클수록 Point 개수 감소)
-closed: 폐곡선 여부
"""

image = cv2.imread('digit_image.png')
image_gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,230,255,0)
thresh = cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image,contours,-1,(0,0,255),4)

contour = contours[0]
epsilon = 0.001*cv2.arcLength(contour,True)
approx = cv2.approxPolyDP(contour,epsilon,True)
image = cv2.drawContours(image,[approx],-1,(0,255,0),4)

cv2.imshow('Image',image)
cv2.waitKey(0)