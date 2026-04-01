import matplotlib.pyplot as plt

# Static data
data = [12, 15, 13, 10, 18, 20, 21, 19, 14, 16, 17, 22, 25, 30, 28]

# Create histogram
plt.hist(data, bins=5, color='green', edgecolor='black')

# Labels and title
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram with Static Input")

plt.grid(axis='y')
plt.show()
