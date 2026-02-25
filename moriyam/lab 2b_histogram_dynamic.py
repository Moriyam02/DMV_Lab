import matplotlib.pyplot as plt

# Ask user for number of data points
n = int(input("Enter the number of data values: "))

data = []

# Collect user input
for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    data.append(value)

# Ask user for number of bins
bins = int(input("Enter number of bins: "))

# Create histogram
plt.hist(data, bins=bins, color='orange', edgecolor='black')

# Labels and title
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram with Dynamic Input")

plt.grid(axis='y')
plt.show()

