import matplotlib.pyplot as plt
import numpy as np
#막대 그래프 그리기

x = np.arange(-9, 10)
plt.bar(x, x ** 2)
plt.show()