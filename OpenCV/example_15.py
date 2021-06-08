import cv2
#cv2.convexHull(contour) Convex Hull알고리즘으로 외각을 구하는 함수
"""
컨벡스 헐 알고리즘은 2차원 평면상에 여러개의 점이 있을 때 
그 점 중에서 일부를 이용하여 볼록 다각형을 만들되 볼록 다각형 내부에 모든 점을 포함시키는 것을 의미한다.
출처: https://www.crocus.co.kr/1288 [Crocus]
"""
image = cv2.imread('digit_image.png')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,230,255,0)
thresh = cv2.bitwise_not(thresh)
contours,hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image,contours,-1,(0,0,255),4)

contour = contours[0]
hull = cv2.convexHull(contour)
image = cv2.drawContours(image,[hull],-1,(255,0,0),4)

cv2.imshow('Image',image)
cv2.waitKey(0)