import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi*10, 500) # PI * 10 너비에, 500개의 점을 균일하게 찍기
fig,axes = plt.subplots(2,1) # 2개의 그래프가 들어가는 Figure 생성 -> 화면 나누기
axes[0].plot(x,np.sin(x)) #첫 번째 그래프는 사인(Sin) 그래프
axes[1].plot(x,np.cos(x)) #두 번째 그래프는 코사인 (Cos) 그래프
plt.show()