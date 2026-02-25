import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))

labels = []
sizes = []

for i in range(n):
    label = input(f"Enter category {i+1} name: ")
    size = float(input(f"Enter value for {label}: "))
    labels.append(label)
    sizes.append(size)

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Fruit Pie Chart")
plt.show()
