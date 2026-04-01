import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create a circle
circle = plt.Circle((0, 5), 0.5, color='red')
ax.add_patch(circle)

# Animation function
def update(frame):
    circle.center = (frame, 5)  # Move circle horizontally
    return circle,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=range(0, 11), interval=100, blit=True
)

plt.title("Moving Circle Animation")
plt.show()
