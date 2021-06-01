import numpy as np

#단일 객체 저장 및 불러오기
array = np.arange(0,10)
np.save('saved.npy',array)
result = np.load('saved.npy')
print("단일 객체 불러오기: ")
print(result)

#복수 객체 저장 및 불러오기
array1 = np.arange(0,10)
array2 = np.arange(10,20)
#복수저장 savez
np.savez('saved.npz',array1 = array1, array2 =array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print("복수객체 한개씩 불러오기: result1")
print(result1)
print("복수객체 한개씩 불러오기: result2")
print(result2)

#Numpy 원소의 오름차순 정렬
array = np.array([5,9,10,3,1])
array.sort()
#오름차순
print("오름차순 정렬: ")
print(array)
#내림차순
print("내림차순 정렬: ")
print(array[::-1])
array =np.array([[5,9,10,3,1],[8,3,4,2,5]])
print("2차원 기본 행열 출력: ")
print(array)
print("행을 기준으로 정렬: ")
array.sort(axis =0)
print(array)

#균일한 간격으로 데이터 생성
array = np.linspace(0,10,5)
print("np.linspace(a,b,c) a에서 b까지 c의 간격으로 출력: ")
print(array)

#난수의 재연(실행마다 결과 동일)
print("np.random.seed() 난수 고정")
np.random.seed(7)
print(np.random.randint(0,10,(2,3)))

#Numpy 배열객체 복사
array1 = np.arange(0,10)
#일반 복사를 하게되면 복사 한 값을 바꾸면 복사된 값도 바뀜 따라서 copy 이용
array2 = array1.copy()
array2[0] = 99
print(array1)

#중복된 원소 제거
array = np.array([1,1,1,1,1,2,2,3,4])
print("중복된 원소 출력")
print(array)
print("np.unique(리스트 이름)으로 중복 제거")
print(np.unique(array))