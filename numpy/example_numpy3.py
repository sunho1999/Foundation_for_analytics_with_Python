import numpy as np

# 행렬 수 곱하기
array  = np.random.randint(1,10,size =4).reshape(2,2)
print(array)
result_array = array*10
print("행열 곱하기:")
print(result_array)

#서로다른 형태의 numpy 연산
#numpy는 서로 다른 형태의 배열을 연산할 때 행 우선으로 수행된다.
#브로드캐스트: 형태가 다른 배열을 연산할 수 있록 배열의 형태를 동적으로 변환
array1 = np.arange(0,8).reshape(2,4)
array2 = np.arange(0,8).reshape(2,4)#(1X2)
array3 = np.concatenate([array1,array2],axis=0)
print("array2위에 array1합치기:")
print(array3)
array4 = np.arange(0,4).reshape(4,1) #(4X1)
print("브로드캐스트를 이용해 더하기:")
print(array3+array4)

#numpy의 마스킹 연산, 마스킹: 각원소에 대하여 체크함.
array1 = np.arange(16).reshape(4,4)
print("4X4 기본 행열:")
print(array1)
#마스킹연산을 이용해 array1에서 10보다 작은 수만 100으로 바꿈
#ex)픽셀 값 바꾸기 가능
array2 = array1 < 10
print("array1에서 10보다 작은거 체크:")
print(array2)
array1[array2] = 100
print("true값 바꾸기:")
print(array1)

#numpy의 집계 함수
array = np.arange(16).reshape(4,4)
print("4X4 기본행열:")
print(array)
print("최대값: ",np.max(array))
print("최소값: ",np.min(array))
print("합계: ",np.sum(array))
print("평균값: ",np.mean(array))
print("합계: ",np.sum(array,axis =0))