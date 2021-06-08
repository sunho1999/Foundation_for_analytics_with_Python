import cv2

image = cv2.imread('cat.jpg')

#Numpy Slicing: ROI처리가능
#픽셀 슬라이싱 하기
logo = image[20:150,70:200]
cv2.imshow('Image',logo)
cv2.waitKey(0)

#ROI 단위로 이미지 복사하기d
#슬라이싱한 이미지 픽셀 값에 넣기
image[0:130,0:130] = logo
cv2.imshow('Image',image)
cv2.waitKey(0)