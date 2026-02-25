import matplotlib.pyplot as plt

# Static input data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 18]

# Create line chart
plt.plot(x, y, marker='o', linestyle='--', color='blue')

# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Static Line Chart")

# Show grid
plt.grid(True)

# Display the chart
plt.show()
