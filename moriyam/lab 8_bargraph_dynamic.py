import matplotlib.pyplot as plt

n = int(input("Enter number of subjects: "))

subjects = []
marks = []

for i in range(n):
    name = input(f"Enter subject {i+1} name: ")
    mark = int(input(f"Enter marks for {name}: "))
    subjects.append(name)
    marks.append(mark)

plt.bar(subjects, marks, color="green")
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
