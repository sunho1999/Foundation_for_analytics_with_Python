import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9, 10)
y = x ** 2
# 라인 스타일로는 '-', ':', '-.', '--' 등이 사용될 수 있습니다.
plt.plot(x, y, linestyle=":", marker="*")
# X축 및 Y축에서 특정 범위를 자를 수도 있습니다.
plt.show()