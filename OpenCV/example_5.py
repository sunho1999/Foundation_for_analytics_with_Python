import cv2

#cv2.resize(image,dsize,fx,fy,interpolation)이미지 크기조절
"""
-dsize:Manual Szie
-fx: 가로비율
-fx: 세로비율
-interpolation: 보간법
INTER_CUBIC: 사이즈를 크게 할때 주로 사용
INTER_AREA: 사이즈를 작게 할때 주로 사용
보간법: 사이즈가 변할 때 픽셀 사이의 값을 조절하는 방법
"""
image = cv2.imread('cat.jpg')
cv2.imshow('Image',image)
cv2.waitKey(0)
#2배 크기
expand = cv2.resize(image,None,fx=2.0,fy=2.0,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image',expand)
cv2.waitKey(0)
#비율 줄이기
shrink = cv2.resize(image,None,fx=0.8,fy=0.8,interpolation=cv2.INTER_AREA)
cv2.imshow('Image',shrink)
cv2.waitKey(0)
