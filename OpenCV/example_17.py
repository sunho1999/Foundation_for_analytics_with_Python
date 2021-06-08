import cv2

#cv2.contourArea(contour)Contour의 면적을 구함
#cv2.arcLength(contour)Contour의 둘레를 구함
#cv2.moments(contour)Contour의 특징을 추출

image =cv2.imread('digit_image.png')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,230,255,0)
thresh = cv2.bitwise_not(thresh)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image,contours,-1,(0,0,255),4)

contour = contours[0]
area = cv2.contourArea(contour)
print(area)
length = cv2.arcLength(contour,True)
print(length)
M = cv2.moments(contour)
print(M)