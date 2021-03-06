import cv2

#cv2.getRotaionMatrix2D(center,angle,scale)이미지 회전을 위한 변환 행렬 생성
"""
-center : 회전중심
-angle: 회전 각도
-scale: Scale Factor
"""
import cv2
image =cv2.imread('cat.jpg')
#행과 열 정보만 저장
height,width = image.shape[:2]

M = cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
dst = cv2.warpAffine(image,M,(width,height))
cv2.imshow('Image',dst)
cv2.waitKey(0)