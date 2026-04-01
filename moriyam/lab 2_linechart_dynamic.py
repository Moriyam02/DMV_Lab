import matplotlib.pyplot as plt

# Ask user for number of points
n = int(input("Enter the number of data points: "))

x = []
y = []

# Collect user input
for i in range(n):
    x_value = float(input(f"Enter x value for point {i+1}: "))
    y_value = float(input(f"Enter y value for point {i+1}: "))
    x.append(x_value)
    y.append(y_value)

# Plot the line chart
plt.plot(x, y, marker='o', linestyle='--', color='blue')

# Labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Dynamic User Input Line Chart")

plt.grid(True)
plt.show()
