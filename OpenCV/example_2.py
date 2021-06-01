import cv2
import time
#Open CV 이미지 연산
image = cv2.imread('cat.jpg')

start_time = time.time()
for i in range(0,100):
    for j in range(0,100):
        image[i,j] = [100,255,255]
print("--- %s seconds ---" %(time.time() - start_time))

start_time = time.time()
image[0:100,0:100] = [0,0,0]
print("--- %s seconds ---" %(time.time()-start_time))
cv2.imshow('Image',image)
cv2.waitKey(0)