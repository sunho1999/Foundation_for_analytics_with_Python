import cv2
import numpy as np

image_1 = cv2.imread('images.jpg')
image_2 = cv2.imread('cat.jpg')

#이때 이미지 크기가 같아야함
result = cv2.add(image_1, image_2)
cv2.imshow('Image',result)
cv2.waitKey(0)