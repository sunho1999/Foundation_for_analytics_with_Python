import matplotlib.pyplot as plt
import numpy as np

#선 그래프그리기
x = np.arange(-9, 10)
y1 = x ** 2
plt.plot(
    x, y1,
    linestyle=":",
    marker="o",
    markersize=8,
    markerfacecolor="blue",
    markeredgecolor="red"
)
plt.show()
