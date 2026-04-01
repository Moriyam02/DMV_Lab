import numpy as np
import matplotlib.pyplot as plt


x1 = np.random.normal(2, 0.3, 40)
y1 = -x1 + np.random.normal(0, 0.2, 40)


x2 = np.random.normal(6, 0.3, 40)
y2 = -x2 + 8 + np.random.normal(0, 0.2, 40)


x = np.concatenate([x1, x2])
y = np.concatenate([y1, y2])


x_out = np.array([1, 7, 5])
y_out = np.array([7, 0, 6])


plt.figure(figsize=(6, 5))
plt.scatter(x, y, color='blue', label='Clusters')
plt.scatter(x_out, y_out, color='red', label='Outliers')

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot with Clusters, Negative Correlation & Outliers')
plt.legend()
plt.show()

