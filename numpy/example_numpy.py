import numpy as np

array = np.arange(4)
print(array)

array2 = np.zeros((4,4), dtype= float)
print(array2)

array3 = np.ones((3,3), dtype=str)
print(array3)

#0부터 9까지 랜덤하기 초기화 된 배열 만들기
#(0~9까지)
array4 = np.random.randint(0,10,(3,3))
print(array4)

#평균이 0이고 , 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0,1,(3,3))
print(array5)