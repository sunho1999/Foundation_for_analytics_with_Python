import cv2
import numpy as np
#cv.warpAffine(image,M,dszie)이미지의 위치를 변경합니다.
"""
-M: 변환 행렬
-dsize: Manual Size
"""
image = cv2.imread('cat.jpg')
#행과 열 정보만 저장합니다.
height, width = image.shape[:2]

M = np.float32([[1,0,50],[0,1,10]])
dst = cv2.warpAffine(image,M,(width,height))
cv2.imshow('Image',dst)
cv2.waitKey(0)
