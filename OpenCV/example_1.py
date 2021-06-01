import cv2

image = cv2.imread('cat.jpg')

#픽셀 수 이미지 크기확인
print(image.shape)
print(image.size)
# 이미지 Numpy 객체의 특정 픽셀을 가리킴
px = image[500,100]

#B,G,R 순서로 출력
#Gray Scale: B,G,R로 구분되지 않음
print(px)
#R 값만 출력하기
print(px[2])