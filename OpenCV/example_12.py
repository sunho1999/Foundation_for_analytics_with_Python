import cv2
import numpy as np
#cv2.line(image,start,end,color,thickness)하나의 직선을 그리는 함수
"""
-start: 시작좌표(2차원)
-end: 종료좌표(2차원)
-thickness: 선의 두
"""
image = np.full((512,512,3),255,np.uint8)
#(0,0)부터 (255,255) 까지 R,G,B
image = cv2.line(image,(0,0),(255,255),(255,0,0),10)
cv2.imshow("Image",image)
cv2.waitKey(0)

#cv2.rectangle(image,start,end,color,thickness)하나의 사각형을 그리는 함수
image = np.full((512,512,3),255,np.uint8)
#(0,0)부터 (255,255) 까지 R,G,B, thickness가 -1이면 사각형 색이 채워
image = cv2.rectangle(image,(0,0),(255,255),(255,0,0),-1)
cv2.imshow("Image",image)
cv2.waitKey(0)

#cv2.circle(image,center,radian,color,thickness)하나의 원을 그리는 함수
"""
-center: 원의 중심(2차원)
-radian: 반지름
"""
image = np.full((512,512,3),255,np.uint8)
#(0,0)부터 (255,255) 까지 R,G,B, thickness가 -1이면 사각형 색이 채워
image = cv2.circle(image,(255,255),150,(255,0,0),-1)
cv2.imshow("Image",image)
cv2.waitKey(0)

#cv2.polylines(image,points,is_closed,color,thickness)하나의 다각형을 그리는 함수
"""
-points:꼭지점들
-is_closed:닫힌 도형 여부
"""
image = np.full((512,512,3),255,np.uint8)
points = np.array([[15,15],[128,128],[13,444],[400,150]])
image = cv2.polylines(image,[points],True,(0,0,255),2)
cv2.imshow("Image",image)
cv2.waitKey(0)

#cv2.putText(image,text,position,font_type,font_scale,color)하나의 텍스르트를 그리는 함수
"""
-position: 텍스트가 출력될 위치
-font_type: 글씨체
-font_scale: 글씨 크기 가중치
"""
image = np.full((512,512,3),255,np.uint8)
image = cv2.putText(image,"Hello World",(0,200),cv2.FONT_ITALIC,2,(0,255,0))
cv2.imshow("Image",image)
cv2.waitKey(0)