import cv2

img_basic =cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
#cv2.imread(file_name,flag)이미지를 읽어 Numpy 객체로 만드는 함수
"""
-file_name: 읽고자 하는 이미지 파일
-flag: 이미지를 읽는 방법 설정
반환값:Numpy객체 (행,열,색상:기본BGR)
"""

cv2.imshow('Image Basic',img_basic)
#cv2.imshow(title,image)
"""
-title: 윈도우 창의 제목
-image: 출력할 이미지 객
"""

cv2.waitKey(0)
#cv2.waitKey(time)키보드 입력을 처리하는 함수
"""
-time: 입력대기 시간(무한대기:0)
"""

cv2.imwrite('result1.png',img_basic)
#cv2.imwrite(file_name,image) 특정한 이미지를 파일로 저장하는 함수
"""
-file_name: 저장할 이미지 파일 이름
-image: 저장할 이미지 객체
"""
#창을 닫을때 설정
cv2.destroyAllWindows()

#기본 이미지를 그레이로 변환
img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Gray',img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png',img_gray)