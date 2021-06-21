import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [1,2,3]
plt.plot(x,y)
plt.title("My plot")
#정보기입
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
#그래프 저장하기
plt.savefig('picture.png')


