import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "CS"]
marks = [85, 90, 78, 92]

plt.bar(subjects, marks, color="skyblue")
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
