import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    x_val = float(input(f"Enter x value {i+1}: "))
    y_val = float(input(f"Enter y value {i+1}: "))
    x.append(x_val)
    y.append(y_val)

plt.scatter(x, y, color="blue")
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
