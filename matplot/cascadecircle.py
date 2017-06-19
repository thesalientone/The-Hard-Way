import numpy as np
import matplotlib.pyplot as plt

N = 50
#x = np.random.rand(N)
# y = np.random.rand(N)
rows = 20
colors = np.random.rand(N)
colors = list(colors)
if rows > 1:
     for count in range(rows - 1):
        colors.extend(colors[0:50])


#
# area = np.pi * (15 * np.random.rand(N)) ** 2
#
# plt.scatter(x, y, s=area, c=colors, alpha=.5)
# plt.show()

x , y = [], []
area = 4
radius = .5
increment = 2 * np.pi / N
offset = 0
for count in range(rows):

    for angle in np.arange(0 + offset, 2 * np.pi + offset, increment):
        x.append(radius * np.cos(angle))
        y.append(radius * np.sin(angle))
    radius *= 1.1
    offset += increment / 2
plt.scatter(x, y, s=area)
plt.axis('equal')
plt.show()
