import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('gray_image.jpg')
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()
"""
4x4 커널 생성
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
"""
size = 10 #사이즈가 커질수록 bluring이 심해짐
kernel = np.ones((size,size),np.float32)/(size**2)
print(kernel)

dst = cv2.filter2D(image,-1,kernel)
plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
plt.show()


#basic blur
image = cv2.imread('gray_image.jpg')
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()

dst = cv2.blur(image,(4,4))
plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
plt.show()

#Gaussian Blur 커널이 홀수 크키여야함
image = cv2.imread('gray_image.jpg')
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()

dst = cv2.GaussianBlur(image,(5,5),0)
plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
plt.show()