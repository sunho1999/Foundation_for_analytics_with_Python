import matplotlib.pyplot as plt
import numpy as np
#누적 막대 그래프 그리기
#x,y,z = [0~1,0~1,0~1 ... 0~1] 10개
x = np.random.rand(10) # 아래 막대
y = np.random.rand(10) # 중간 막대
z = np.random.rand(10) # 위 막대
data = [x, y, z]
x_array = np.arange(10)
for i in range(0, 3): # 누적 막대의 종류가 3개
    plt.bar(
        x_array, # 0부터 10까지의 X 위치에서
        data[i], # 각 높이(10개)만큼 쌓음
        bottom=np.sum(data[:i], axis=0)
    )
plt.show()