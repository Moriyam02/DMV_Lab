import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)

line, = ax.plot([], [], lw=2)

x_data = []
y_data = []

def update(frame):
    x = frame * 0.1
    
    # Zigzag pattern using sine wave with upward motion
    y = 0.5 * x + 2 * np.sign(np.sin(3 * x))
    
    x_data.append(x)
    y_data.append(y)
    
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=200, interval=50)

plt.title("Upward Zigzag Motion")
plt.show()
